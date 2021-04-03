from main.I_lexical.token_types import TokenType
from main.II_syntactic.node import ASTNode
from main.II_syntactic.node_types import ASTNodeType


MUL_OPERATOR_MAP = {
    '*': ASTNodeType.MML_EXP,
    '/': ASTNodeType.MRD_EXP,
    '\\': ASTNodeType.MRD_EXP,
    '.*': ASTNodeType.BSO_EXP,
    './': ASTNodeType.BSO_EXP,
    '.\\': ASTNodeType.BSO_EXP,
}

SEL_TERMINATOR_MAP = {
    'if': ('elseif', 'else', 'end'),
    'elseif': ('elseif', 'else', 'end'),
    'else': ('end', )
}


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

    id_list ::= identifier*

    ass_exp ::= id '=' cln_exp
    cln_exp ::= lor_exp (':' lor_exp)*
    lor_exp ::= lan_exp (('||'|'|') lan_exp)*
    lan_exp ::= eql_exp (('&&'|'&') eql_exp)*
    eql_exp ::= rel_exp (('~='|'==') rel_exp)*
    rel_exp ::= add_exp (('<='|'<'|'>='|'>') add_exp)*
    add_exp ::= mul_exp (('+'|'-') mul_exp)*
    mul_exp ::= uny_exp (('*'|'/') uny_exp)*
    uny_exp ::= ('+'|'-'|'~')* pri_exp
    pri_exp ::= identifier | number_lit | string_lit | '('cln_exp')' | '[' array_list ']'

    identifier ::=
    number_lit ::=
    string_lit ::=
    array_list ::= (cln_exp exp_stmt*)*
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
            TokenType.IDENTIFIER: self.parse_identifier_expression,
            TokenType.NUMBER_LIT: self.parse_number_literal,
            TokenType.STRING_LIT: self.parse_string_literal,
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
        if self.get_token(0).get_type() != TokenType.IDENTIFIER or self.get_token(1).get_type() != TokenType.ASS:
            return None
        node = ASTNode(n_type=ASTNodeType.ASS_STMT)

        assignment_expression = self.parse_assignment_expression()
        if assignment_expression is None:
            # todo: throw invalid expression statement exception
            return None
        node.add_child(assignment_expression)

        if self.get_token().get_type() != TokenType.EO_STMT:
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

        if self.get_token().get_type() != TokenType.EO_STMT:
            # todo: throw invalid statement exception
            return None
        node.add_child(ASTNode(n_type=ASTNodeType.EO_STMT, n_text=self.tokens.pop(0).get_text()))

        return node

    def parse_clear_statement(self):
        if self.get_token().get_text() != "clear":
            return None
        self.tokens.pop(0)  # remove 'clear'
        node = ASTNode(n_type=ASTNodeType.CLR_STMT)
        node.add_child(self.parse_identifier_list())

        if self.get_token().get_type() != TokenType.EO_STMT:
            # todo: throw invalid statement exception
            return None
        node.add_child(ASTNode(n_type=ASTNodeType.EO_STMT, n_text=self.tokens.pop(0).get_text()))

        return node

    def parse_selection_statement(self):
        if self.get_token().get_text() != "if":
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

        node.add_child(self.parse_statement_list(terminators=SEL_TERMINATOR_MAP[clause]))

        return node

    def parse_iteration_statement(self):
        if self.get_token(0).get_text() not in ('while', 'for'):
            return None

        node = ASTNode(n_type=ASTNodeType.ITR_STMT)

        node.add_child(self.parse_iteration_clause(self.tokens.pop(0).get_text()))

        if self.get_token().get_text() != 'end':
            # todo: throw invalid statement exception
            return None
        self.tokens.pop(0)  # remove 'end'

        if self.get_token().get_type() != TokenType.EO_STMT:
            # todo: throw invalid statement exception
            return None
        node.add_child(ASTNode(n_type=ASTNodeType.EO_STMT, n_text=self.tokens.pop(0).get_text()))

        return node

    def parse_iteration_clause(self, clause):
        node = ASTNode(n_type=ASTNodeType.ITR_CLS, n_text=clause)

        expression = self.parse_colon_expression() if clause == 'while' else self.parse_assignment_expression()
        if expression is None:
            # todo: throw exception
            return None
        node.add_child(expression)

        node.add_child(self.parse_statement_list(terminators=('end', )))

        return node

    def parse_jump_statement(self):
        pass

    def parse_identifier_list(self):
        node = ASTNode(n_type=ASTNodeType.ID_LIST)
        while self.get_token().get_type() == TokenType.IDENTIFIER:
            node.add_child(ASTNode(n_type=ASTNodeType.IDENTIFIER, n_text=self.tokens.pop(0).get_text()))
        return node

    def parse_assignment_expression(self):
        identifier = ASTNode(n_type=ASTNodeType.IDENTIFIER, n_text=self.tokens.pop(0).get_text())
        node = ASTNode(n_type=ASTNodeType.ASS_EXP, n_text=self.tokens.pop(0).get_text(), children=[identifier])
        expression = self.parse_colon_expression()
        if expression is None:
            # todo: throw invalid assignment statement exception
            return None
        node.add_child(expression)
        return node

    def parse_colon_expression(self):
        root = self.parse_logic_or_expression()
        if root is None:
            return None
        while self.get_token().get_type() == TokenType.CLN:
            token = self.tokens.pop(0)  # ':'
            node1 = self.parse_logic_or_expression()
            if node1 is None:
                # todo: raise invalid colon expression exception
                return None
            if self.get_token().get_type() == TokenType.CLN:
                # colon expression with three value
                token = self.tokens.pop(0)  # ':'
                node2 = self.parse_logic_or_expression()
                if node2 is None:
                    # todo: raise invalid colon expression exception
                    return None
                root = ASTNode(n_type=ASTNodeType.CLN_EXP, n_text=token.get_text(), children=[root, node1, node2])
            else:
                # colon expression with two value
                root = ASTNode(n_type=ASTNodeType.CLN_EXP, n_text=token.get_text(), children=[root, node1])
        return root

    def parse_logic_or_expression(self):
        root = self.parse_logic_and_expression()
        if root is None:
            return None

        while self.get_token().get_type() == TokenType.LOR:
            token = self.tokens.pop(0)  # '|'
            child = self.parse_logic_and_expression()
            if child is None:
                # todo: raise invalid logic or expression exception
                return None
            root = ASTNode(n_type=ASTNodeType.BSO_EXP, n_text=token.get_text(), children=[root, child])
        return root

    def parse_logic_and_expression(self):
        root = self.parse_equal_expression()
        if root is None:
            return None

        while self.get_token().get_type() == TokenType.LAN:
            token = self.tokens.pop(0)  # '&'
            child = self.parse_equal_expression()
            if child is None:
                # todo: raise invalid logic and expression exception
                return None
            root = ASTNode(n_type=ASTNodeType.BSO_EXP, n_text=token.get_text(), children=[root, child])
        return root

    def parse_equal_expression(self):
        root = self.parse_relational_expression()
        if root is None:
            return None

        while self.get_token().get_type() == TokenType.EQL:
            token = self.tokens.pop(0)  # equal symbol
            child = self.parse_relational_expression()
            if child is None:
                # todo: raise invalid equal expression exception
                return None
            root = ASTNode(n_type=ASTNodeType.BSO_EXP, n_text=token.get_text(), children=[root, child])
        return root

    def parse_relational_expression(self):
        root = self.parse_additive_expression()
        if root is None:
            return None

        while self.get_token().get_type() == TokenType.REL:
            token = self.tokens.pop(0)  # relational symbol
            child = self.parse_additive_expression()
            if child is None:
                # todo: raise invalid relational expression exception
                return None
            root = ASTNode(n_type=ASTNodeType.BSO_EXP, n_text=token.get_text(), children=[root, child])
        return root

    def parse_additive_expression(self):
        root = self.parse_multiplicative_expression()
        if root is None:
            return None

        while self.get_token().get_type() == TokenType.ADD:
            token = self.tokens.pop(0)  # additive symbol
            child = self.parse_multiplicative_expression()
            if child is None:
                # todo: raise invalid additive expression exception
                return None
            root = ASTNode(n_type=ASTNodeType.BSO_EXP, n_text=token.get_text(), children=[root, child])
        return root

    def parse_multiplicative_expression(self):
        root = self.parse_prefix_expression()
        if root is None:
            return None

        while self.get_token().get_type() == TokenType.MUL:
            token = self.tokens.pop(0)  # multiplicative symbol
            child = self.parse_prefix_expression()
            if child is None:
                # todo: raise invalid multiplicative expression exception
                return None
            root = ASTNode(n_type=MUL_OPERATOR_MAP[token.get_text()], n_text=token.get_text(), children=[root, child])
        return root

    def parse_prefix_expression(self):
        """
        unary operator
        right associate
        """
        if self.get_token().get_type() in (TokenType.ADD, TokenType.LNT):
            token = self.tokens.pop(0)  # unary operator symbol
            child = self.parse_prefix_expression()
            if child is None:
                # todo: raise invalid unary expression exception
                return None
            return ASTNode(n_type=ASTNodeType.PRE_EXP, n_text=token.get_text(), children=[child])
        return self.parse_postfix_expression()

    def parse_postfix_expression(self):
        """
        unary operator
        left associate
        """
        root = self.parse_primary_expression()
        if root is None:
            return None

        while self.get_token().get_type() == TokenType.TRA:
            token = self.tokens.pop(0)  # transpose symbol
            root = ASTNode(n_type=ASTNodeType.PST_EXP, n_text=token.get_text(), children=[root])
        return root

    def parse_primary_expression(self):
        if not self.tokens:
            return None
        if self.get_token().get_type() not in self.primary_cases:
            return None
        return self.primary_cases[self.tokens[0].get_type()]()

    def parse_identifier_expression(self):
        if self.get_token(1).get_type() == TokenType.L_PAREN:
            return self.parse_array_expression()
        else:
            return ASTNode(n_type=ASTNodeType.IDENTIFIER, n_text=self.tokens.pop(0).get_text())

    def parse_number_literal(self):
        return ASTNode(n_type=ASTNodeType.NUMBER_LIT, n_text=self.tokens.pop(0).get_text())

    def parse_string_literal(self):
        return ASTNode(n_type=ASTNodeType.STRING_LIT, n_text=self.tokens.pop(0).get_text())

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
        self.tokens.pop(0)  # remove left bracket
        node = self.parse_array_list()
        if node and self.get_token().get_type() == TokenType.R_BRACKET:
            self.tokens.pop(0)  # remove right bracket
        else:
            # todo: raise invalid bracket expression exception
            return None
        return node

    def parse_array_list(self):
        node = ASTNode(n_type=ASTNodeType.ARRAY_LIST)
        while self.get_token().get_type() != TokenType.R_BRACKET:
            child = self.parse_colon_expression()
            if child is None:
                # todo:
                return None
            node.add_child(child)
            while self.get_token().get_type() == TokenType.EO_STMT:
                node.add_child(ASTNode(n_type=ASTNodeType.EO_STMT, n_text=self.tokens.pop(0).get_text()))
        return node

    def parse_array_expression(self):
        root = ASTNode(n_type=ASTNodeType.ARR_EXP)
        root.add_child(ASTNode(n_type=ASTNodeType.IDENTIFIER, n_text=self.tokens.pop(0).get_text()))
        self.tokens.pop(0)  # remove left paren
        node = self.parse_index_list()
        if node and self.get_token().get_type() == TokenType.R_PAREN:
            self.tokens.pop(0)  # remove right paren
        else:
            # todo: raise invalid array expression exception
            return None
        root.add_child(node)
        return root

    def parse_index_list(self):
        root = ASTNode(n_type=ASTNodeType.INDEX_LIST)
        while True:
            if self.get_token().get_type() == TokenType.CLN:
                root.add_child(ASTNode(n_type=ASTNodeType.CLN_EXP, n_text=self.tokens.pop(0).get_text()))
            else:
                child = self.parse_colon_expression()
                if child is None:
                    # todo:
                    return None
                root.add_child(child)

            if str(self.get_token()) == ",":
                self.tokens.pop(0)  # remove ','
            else:
                break
        return root
