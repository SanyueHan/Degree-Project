from main.II_syntactic.node import ASTNode
from main.II_syntactic.node_types import ASTNodeType
from main.I_lexical.token_types import TokenType


class Parser:
    r"""
    grammar rules in EBNF (Extended Backus-Naur-Form):
    stmt_list ::= stmt*
    stmt ::= ass_stmt | exp_stmt | clr_stmt | sel_stmt | itr_stmt | jmp_stmt

    ass_stmt ::= ass_exp eo_stmt
    exp_stmt ::= exp eo_stmt
    clr_stmt ::= 'clear' id_list eo_stmt
    sel_stmt ::= 'if' exp stmt_list eo_stmt? ('elseif' exp stmt_list)* ('else' stmt_list)? 'end' eo_stmt
    itr_stmt ::=
    jmp_stmt ::=

    id_list ::= id*

    ass_exp ::= id '=' exp
    exp ::= lor_exp
    lor_exp ::= lan_exp ('||' lan_exp)*
    lan_exp ::= eql_exp ('&&' eql_exp)*
    eql_exp ::= rel_exp (('!='|'==') rel_exp)*
    rel_exp ::= add_exp (('<='|'<'|'>='|'>') add_exp)*
    add_exp ::= mul_exp (('+'|'-') mul_exp)*
    mul_exp ::= uny_exp (('*'|'/') uny_exp)*
    uny_exp ::= ('+'|'-'|'~')* pri_exp
    pri_exp ::= id | num_lit | str_lit | '('exp')'
    """
    def __init__(self, token_list):
        self.tokens = token_list

    def get_token(self, index=0):
        if len(self.tokens) > index:
            return self.tokens[index]

    def parse_statement_list(self):
        ast_root = ASTNode(n_type=ASTNodeType.STMT_LIST)
        while self.tokens and self.tokens[0].get_text() not in {'else', 'elseif', 'end'}:
            if self.tokens[0].get_type() == TokenType.EO_STMT:
                self.tokens.pop(0)
                continue
            ast_root.add_child(self.parse_statement())
        return ast_root

    def parse_statement(self):
        assignment_statement = self.parse_assignment_statement()
        if assignment_statement:
            return assignment_statement

        expression_statement = self.parse_expression_statement()
        if expression_statement:
            return expression_statement

        clear_statement = self.parse_clear_statement()
        if clear_statement:
            return clear_statement

        selection_statement = self.parse_selection_statement()
        if selection_statement:
            return selection_statement

        iteration_statement = self.parse_iteration_statement()
        if iteration_statement:
            return iteration_statement

        jump_statement = self.parse_jump_statement()
        if jump_statement:
            return jump_statement

        # todo: throw unknown statement exception

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

        expression = self.parse_expression()
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

        node.add_child(self.parse_clause(self.tokens.pop(0).get_text()))

        while self.get_token().get_text() == 'elseif':
            elseif_clause = self.parse_clause(self.tokens.pop(0).get_text())
            node.add_child(elseif_clause)

        if self.get_token().get_text() == 'else':
            node.add_child(self.parse_clause(self.tokens.pop(0).get_text()))

        if self.get_token().get_text() != 'end':
            # todo: throw invalid statement exception
            return None
        self.tokens.pop(0)  # remove 'end'

        if self.get_token().get_type() != TokenType.EO_STMT:
            # todo: throw invalid statement exception
            return None
        node.add_child(ASTNode(n_type=ASTNodeType.EO_STMT, n_text=self.tokens.pop(0).get_text()))

        return node

    def parse_clause(self, clause):
        node = ASTNode(n_type=ASTNodeType.ClS, n_text=clause)

        if clause != 'else':
            expression = self.parse_expression()
            if expression is None:
                # todo: throw exception
                return None
            node.add_child(expression)

        node.add_child(self.parse_statement_list())

        return node

    def parse_elseif_clause(self):
        pass

    def parse_else_clause(self):
        pass

    def parse_iteration_statement(self):
        """
        only while statement currently
        """
        if self.get_token(0).get_text() != "while":
            return None

    def parse_jump_statement(self):
        pass

    def parse_identifier_list(self):
        node = ASTNode(n_type=ASTNodeType.ID_LIST)
        while self.get_token().type == TokenType.ID:
            node.add_child(ASTNode(n_text=self.tokens.pop(0).get_text(), n_type=ASTNodeType.ID))
        return node

    def parse_assignment_expression(self):
        identifier = ASTNode(n_type=ASTNodeType.ID, n_text=self.tokens.pop(0).get_text())
        node = ASTNode(n_type=ASTNodeType.ASS_EXP, n_text=self.tokens.pop(0).get_text(), children=[identifier])
        expression = self.parse_expression()
        if expression is None:
            # todo: throw invalid assignment statement exception
            return None
        node.add_child(expression)
        return node

    def parse_expression(self):
        return self.parse_logic_or_expression()

    def parse_logic_or_expression(self):
        root = self.parse_logic_and_expression()
        if root:
            while self.get_token(0).get_type() == TokenType.LOR:
                token = self.tokens.pop(0)  # logic or symbol
                child = self.parse_logic_and_expression()
                if child:
                    root = ASTNode(n_type=ASTNodeType.LOR_EXP, n_text=token.get_text(), children=[root, child])
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
                    root = ASTNode(n_type=ASTNodeType.LAN_EXP, n_text=token.get_text(), children=[root, child])
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
                    root = ASTNode(n_type=ASTNodeType.EQL_EXP, n_text=token.get_text(), children=[root, child])
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
                    root = ASTNode(n_type=ASTNodeType.REL_EXP, n_text=token.get_text(), children=[root, child])
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
                    root = ASTNode(n_type=ASTNodeType.ADD_EXP, n_text=token.get_text(), children=[root, child])
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
                    root = ASTNode(n_type=ASTNodeType.MUL_EXP, n_text=token.get_text(), children=[root, child])
                else:
                    # todo: raise invalid multiplicative expression exception
                    return None
        return root

    def parse_unary_expression(self):
        if self.get_token(0).get_type() in (TokenType.ADD, TokenType.LNT):
            token = self.tokens.pop(0)  # unary symbol
            child = self.parse_unary_expression()
            if child:
                return ASTNode(n_type=ASTNodeType.UNY_EXP, n_text=token.get_text(), children=[child])
            else:
                # todo: raise invalid unary expression exception
                return None
        else:
            return self.parse_primary_expression()

    def parse_primary_expression(self):
        if not self.tokens:
            return None

        if self.tokens[0].get_type() == TokenType.ID:
            return ASTNode(n_type=ASTNodeType.ID, n_text=self.tokens.pop(0).get_text())
        if self.tokens[0].get_type() == TokenType.NUM_LIT:
            return ASTNode(n_type=ASTNodeType.NUM_LIT, n_text=self.tokens.pop(0).get_text())
        if self.tokens[0].get_type() == TokenType.STR_LIT:
            return ASTNode(n_type=ASTNodeType.STR_LIT, n_text=self.tokens.pop(0).get_text())
        if self.tokens[0].get_type() == TokenType.L_PAREN:
            self.tokens.pop(0)  # remove left paren
            node = self.parse_additive_expression()
            if node and self.tokens and self.tokens[0].get_type() == TokenType.R_PAREN:
                self.tokens.pop(0)  # remove right paren
            else:
                # todo: raise invalid parens exception
                return None
            return node
