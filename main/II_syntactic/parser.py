from main.I_lexical.token_types import TokenType
from main.II_syntactic.node import ASTNode
from main.II_syntactic.node_types import ASTNodeType
from main.II_syntactic.mul_map import MUL_MAP


class Parser:
    r"""
    grammar rules in EBNF (Extended Backus-Naur-Form):
    stmt_list ::= stmt*
    stmt ::= ass_stmt | exp_stmt | clr_stmt | sel_stmt | itr_stmt | jmp_stmt | eo_stmt

    ass_stmt ::= ass_exp eo_stmt
    exp_stmt ::= cln_exp eo_stmt
    clr_stmt ::= 'clear' id_list eo_stmt
    sel_stmt ::= 'if' cln_exp stmt_list ('elseif' cln_exp stmt_list)* ('else' stmt_list)? 'end' eo_stmt
    itr_stmt ::= 'while' cln_exp stmt_list
    jmp_stmt ::=

    id_list ::= id*

    ass_exp ::= id '=' cln_exp
    cln_exp ::= lor_exp (':' lor_exp)*
    lor_exp ::= lan_exp ('||' lan_exp)*
    lan_exp ::= eql_exp ('&&' eql_exp)*
    eql_exp ::= rel_exp (('!='|'==') rel_exp)*
    rel_exp ::= add_exp (('<='|'<'|'>='|'>') add_exp)*
    add_exp ::= mul_exp (('+'|'-') mul_exp)*
    mul_exp ::= uny_exp (('*'|'/') uny_exp)*
    uny_exp ::= ('+'|'-'|'~')* pri_exp
    pri_exp ::= id | num_lit | str_lit | '('cln_exp')'
    """
    def __init__(self, token_list):
        self.tokens = token_list
        self.statement_cases = [
            self.parse_assignment_statement,
            self.parse_expression_statement,
            self.parse_clear_statement,
            self.parse_selection_statement,
            self.parse_iteration_statement,
            self.parse_jump_statement,
        ]
        self.primary_cases = {
            TokenType.ID: self.parse_identifier,
            TokenType.NUM_LIT: self.parse_number_literal,
            TokenType.STR_LIT: self.parse_string_literal,
            TokenType.L_PAREN: self.parse_paren_expression,
            TokenType.L_BRACKET: self.parse_bracket_expression,
        }

    def get_token(self, index=0):
        if len(self.tokens) > index:
            return self.tokens[index]

    def parse_statement_list(self, terminators=('None', )):
        """
        when parse program, terminators use it default value, only if no token left will the parsing stop
        when parse code blocks like selection, iteration, function, terminators will be some specified keywords
        """
        node = ASTNode(n_type=ASTNodeType.STMT_LIST)
        while str(self.get_token()) not in terminators:
            if self.get_token() is None:
                # todo: raise invalid code block error
                return None
            if self.tokens[0].get_type() == TokenType.EO_STMT:
                self.tokens.pop(0)
                continue
            node.add_child(self.parse_statement())
        return node

    def parse_statement(self):
        for stmt in self.statement_cases:
            node = stmt()
            if node:
                return node
        else:
            # todo: throw unknown statement exception
            return None

    def parse_assignment_statement(self):
        if self.get_token(0).get_type() != TokenType.ID or self.get_token(1).get_type() != TokenType.ASS:
            return None
        node = ASTNode(n_type=ASTNodeType.ASS_STMT)

        assignment_expression = self.parse_assignment_expression()
        if assignment_expression is None:
            # todo: throw invalid expression statement exception
            return None
        node.add_child(assignment_expression)

        if self.get_token(0).get_type() != TokenType.EO_STMT:
            # todo: throw invalid statement exception
            return None
        node.add_child(ASTNode(n_type=ASTNodeType.EO_STMT, n_text=self.tokens.pop(0).get_text()))

        return node

    def parse_expression_statement(self):
        node = ASTNode(n_type=ASTNodeType.EXP_STMT)

        expression = self.parse_colon_expression()
        if expression is None:
            # todo: throw invalid expression statement exception
            return None
        node.add_child(expression)

        if self.get_token(0).get_type() != TokenType.EO_STMT:
            # todo: throw invalid statement exception
            return None
        node.add_child(ASTNode(n_type=ASTNodeType.EO_STMT, n_text=self.tokens.pop(0).get_text()))

        return node

    def parse_clear_statement(self):
        if self.get_token(0).get_text() != "clear":
            return None
        self.tokens.pop(0)  # remove 'clear'
        node = ASTNode(n_type=ASTNodeType.CLR_STMT)
        node.add_child(self.parse_identifier_list())

        if self.get_token(0).get_type() != TokenType.EO_STMT:
            # todo: throw invalid statement exception
            return None
        node.add_child(ASTNode(n_type=ASTNodeType.EO_STMT, n_text=self.tokens.pop(0).get_text()))

        return node

    def parse_selection_statement(self):
        if self.get_token(0).get_text() != "if":
            return None
        node = ASTNode(n_type=ASTNodeType.SEL_STMT)

        node.add_child(self.parse_selection_clause(self.tokens.pop(0).get_text()))

        while self.get_token().get_text() == 'elseif':
            elseif_clause = self.parse_selection_clause(self.tokens.pop(0).get_text())
            node.add_child(elseif_clause)

        if self.get_token().get_text() == 'else':
            node.add_child(self.parse_selection_clause(self.tokens.pop(0).get_text()))

        if self.get_token().get_text() != 'end':
            # todo: throw invalid statement exception
            return None
        self.tokens.pop(0)  # remove 'end'

        if self.get_token().get_type() != TokenType.EO_STMT:
            # todo: throw invalid statement exception
            return None
        node.add_child(ASTNode(n_type=ASTNodeType.EO_STMT, n_text=self.tokens.pop(0).get_text()))

        return node

    def parse_selection_clause(self, clause):
        node = ASTNode(n_type=ASTNodeType.SEL_ClS, n_text=clause)

        if clause != 'else':
            expression = self.parse_colon_expression()
            if expression is None:
                # todo: throw exception
                return None
            node.add_child(expression)

        terminators_map = {
            'if': ('elseif', 'else', 'end'),
            'elseif': ('elseif', 'else', 'end'),
            'else': ('end', )
        }

        node.add_child(self.parse_statement_list(terminators=terminators_map[clause]))

        return node

    def parse_iteration_statement(self):
        if self.get_token(0).get_text() not in ('while', 'for'):
            return None

        node = ASTNode(n_type=ASTNodeType.ITR_STMT)

        if self.get_token(0).get_text() == 'while':
            node.add_child(self.parse_while_clause(self.tokens.pop(0).get_text()))
        else:
            node.add_child(self.parse_for_clause(self.tokens.pop(0).get_text()))

        if self.get_token().get_text() != 'end':
            # todo: throw invalid statement exception
            return None
        self.tokens.pop(0)  # remove 'end'

        if self.get_token().get_type() != TokenType.EO_STMT:
            # todo: throw invalid statement exception
            return None
        node.add_child(ASTNode(n_type=ASTNodeType.EO_STMT, n_text=self.tokens.pop(0).get_text()))

        return node

    def parse_while_clause(self, clause):
        node = ASTNode(n_type=ASTNodeType.WHL_CLS, n_text=clause)

        expression = self.parse_colon_expression()
        if expression is None:
            # todo: throw exception
            return None
        node.add_child(expression)

        node.add_child(self.parse_statement_list(terminators=('end', )))

        return node

    def parse_for_clause(self, clause):
        pass

    def parse_jump_statement(self):
        pass

    def parse_identifier_list(self):
        node = ASTNode(n_type=ASTNodeType.ID_LIST)
        while self.get_token().type == TokenType.ID:
            node.add_child(ASTNode(n_type=ASTNodeType.ID, n_text=self.tokens.pop(0).get_text()))
        return node

    def parse_assignment_expression(self):
        identifier = ASTNode(n_type=ASTNodeType.ID, n_text=self.tokens.pop(0).get_text())
        node = ASTNode(n_type=ASTNodeType.ASS_EXP, n_text=self.tokens.pop(0).get_text(), children=[identifier])
        expression = self.parse_colon_expression()
        if expression is None:
            # todo: throw invalid assignment statement exception
            return None
        node.add_child(expression)
        return node

    def parse_colon_expression(self):
        return self.parse_logic_or_expression()

    def parse_logic_or_expression(self):
        root = self.parse_logic_and_expression()
        if root:
            while self.get_token(0).get_type() == TokenType.LOR:
                token = self.tokens.pop(0)  # logic or symbol
                child = self.parse_logic_and_expression()
                if child:
                    root = ASTNode(n_type=ASTNodeType.BSO_EXP, n_text=token.get_text(), children=[root, child])
                else:
                    # todo: raise invalid logic or expression exception
                    return None
        return root

    def parse_logic_and_expression(self):
        root = self.parse_equal_expression()
        if root:
            while self.get_token(0).get_type() == TokenType.LAN:
                token = self.tokens.pop(0)  # logic and symbol
                child = self.parse_equal_expression()
                if child:
                    root = ASTNode(n_type=ASTNodeType.BSO_EXP, n_text=token.get_text(), children=[root, child])
                else:
                    # todo: raise invalid logic and expression exception
                    return None
        return root

    def parse_equal_expression(self):
        root = self.parse_relational_expression()
        if root:
            while self.get_token(0).get_type() == TokenType.EQL:
                token = self.tokens.pop(0)  # equal symbol
                child = self.parse_relational_expression()
                if child:
                    root = ASTNode(n_type=ASTNodeType.BSO_EXP, n_text=token.get_text(), children=[root, child])
                else:
                    # todo: raise invalid equal expression exception
                    return None
        return root

    def parse_relational_expression(self):
        root = self.parse_additive_expression()
        if root:
            while self.get_token(0).get_type() == TokenType.REL:
                token = self.tokens.pop(0)  # relational symbol
                child = self.parse_additive_expression()
                if child:
                    root = ASTNode(n_type=ASTNodeType.BSO_EXP, n_text=token.get_text(), children=[root, child])
                else:
                    # todo: raise invalid relational expression exception
                    return None
        return root

    def parse_additive_expression(self):
        root = self.parse_multiplicative_expression()
        if root:
            while self.get_token(0).get_type() == TokenType.ADD:
                token = self.tokens.pop(0)  # additive symbol
                child = self.parse_multiplicative_expression()
                if child:
                    root = ASTNode(n_type=ASTNodeType.BSO_EXP, n_text=token.get_text(), children=[root, child])
                else:
                    # todo: raise invalid additive expression exception
                    return None
        return root

    def parse_multiplicative_expression(self):
        root = self.parse_unary_expression()
        if root:
            while self.get_token(0).get_type() == TokenType.MUL:
                token = self.tokens.pop(0)  # multiplicative symbol
                child = self.parse_unary_expression()
                if child:
                    root = ASTNode(n_type=MUL_MAP[token.get_text()], n_text=token.get_text(), children=[root, child])
                else:
                    # todo: raise invalid multiplicative expression exception
                    return None
        return root

    def parse_unary_expression(self):
        if self.get_token(0).get_type() in (TokenType.ADD, TokenType.LNT):
            token = self.tokens.pop(0)  # unary operator symbol
            child = self.parse_unary_expression()
            if child:
                return ASTNode(n_type=ASTNodeType.USO_EXP, n_text=token.get_text(), children=[child])
            else:
                # todo: raise invalid unary expression exception
                return None
        else:
            return self.parse_primary_expression()

    def parse_primary_expression(self):
        if not self.tokens:
            return None
        return self.primary_cases[self.tokens[0].get_type()]()

    def parse_identifier(self):
        return ASTNode(n_type=ASTNodeType.ID, n_text=self.tokens.pop(0).get_text())

    def parse_number_literal(self):
        return ASTNode(n_type=ASTNodeType.NUM_LIT, n_text=self.tokens.pop(0).get_text())

    def parse_string_literal(self):
        return ASTNode(n_type=ASTNodeType.STR_LIT, n_text=self.tokens.pop(0).get_text())

    def parse_paren_expression(self):
        self.tokens.pop(0)  # remove left paren
        node = self.parse_colon_expression()
        if node and self.get_token().get_type() == TokenType.R_PAREN:
            self.tokens.pop(0)  # remove right paren
        else:
            # todo: raise invalid parens exception
            return None
        return node

    def parse_bracket_expression(self):
        pass
