from II_syntactic.node import ASTNode
from II_syntactic.node_types import ASTNodeType
from I_lexical.token_types import TokenType


class Parser:
    r"""
    grammar rules in EBNF (Extended Backus-Naur-Form):
    statement ::= ass_stmt | exp_stmt | clr_stmt

    ass_stmt ::= id ('='|'+='|'-='|'*='|'/=') exp ';'?
    exp_stmt ::= exp ';'?
    clr_stmt ::= 'clear' id_lst ';'?

    exp ::= lor_exp
    lor_exp ::= lan_exp ('||' lan_exp)*
    lan_exp ::= eql_exp ('&&' eql_exp)*
    eql_exp ::= rel_exp (('!='|'==') rel_exp)*
    rel_exp ::= add_exp (('<='|'<'|'>='|'>') add_exp)*
    add_exp ::= mul_exp (('+'|'-') mul_exp)*
    mul_exp ::= uny_exp (('*'|'/') uny_exp)*
    uny_exp ::= ('+'|'-'|'~')* pri_exp
    pri_exp ::= id | num_lit | '('exp')'

    id_list ::= id*
    stmt_list ::= stmt*
    """
    def __init__(self, token_list):
        self.tokens = token_list

    def parse_assignment_statement(self):
        if not (self.tokens and self.tokens[0].get_type() == TokenType.ID):
            return None
        node = ASTNode(n_text=self.tokens.pop(0).get_text(), n_type=ASTNodeType.ASS_STMT)

        if not (self.tokens and self.tokens[0].get_type() == TokenType.ASS):
            # no error because the statement may be an expression statement started by an ID
            return None
        self.tokens.pop(0)  # remove '='

        child = self.parse_expression()
        if not child:
            # todo: throw invalid assignment statement exception
            pass
        node.add_child(child)

        if self.tokens:  # semicolon is optional
            if self.tokens[0].get_type() == TokenType.SEMICOLON:
                node.add_child(ASTNode(n_text=";"))
            else:
                # todo: throw invalid assignment statement exception
                pass
        return node

    def parse_expression_statement(self):
        node = ASTNode(n_type=ASTNodeType.EXP_STMT)

        child = self.parse_expression()
        if not child:
            # todo: throw invalid expression statement exception
            return None
        node.add_child(child)

        if self.tokens:  # semicolon is optional
            if self.tokens[0].get_type() == TokenType.SEMICOLON:
                node.add_child(ASTNode(n_text=";"))
            else:
                # todo: throw invalid expression statement exception
                return None
        return node

    def parse_clear_statement(self):
        if not (self.tokens and self.tokens[0].get_type() == TokenType.CLR):
            return None
        node = ASTNode(n_text=self.tokens.pop(0).get_text(), n_type=ASTNodeType.CLR_STMT)

        # todo: parse identifier list

        if self.tokens:  # semicolon is optional
            if self.tokens[0].get_type() == TokenType.SEMICOLON:
                node.add_child(ASTNode(n_text=";"))
            else:
                # todo: throw invalid clear statement exception
                pass
        return node

    def parse_expression(self):
        return self.parse_logic_or_expression()

    def parse_logic_or_expression(self):
        root = self.parse_logic_and_expression()
        if root:
            while self.tokens and self.tokens[0].get_type() == TokenType.LOR:
                token = self.tokens.pop(0)  # logic or symbol
                child = self.parse_logic_and_expression()
                if child:
                    root = ASTNode(n_type=ASTNodeType.LOR_EXP, n_text=token.get_text(), children=[root, child])
                else:
                    # todo: raise invalid logic or expression exception
                    pass
        return root

    def parse_logic_and_expression(self):
        root = self.parse_equal_expression()
        if root:
            while self.tokens and self.tokens[0].get_type() == TokenType.LAN:
                token = self.tokens.pop(0)  # logic and symbol
                child = self.parse_equal_expression()
                if child:
                    root = ASTNode(n_type=ASTNodeType.LAN_EXP, n_text=token.get_text(), children=[root, child])
                else:
                    # todo: raise invalid logic and expression exception
                    pass
        return root

    def parse_equal_expression(self):
        root = self.parse_relational_expression()
        if root:
            while self.tokens and self.tokens[0].get_type() == TokenType.EQL:
                token = self.tokens.pop(0)  # equal symbol
                child = self.parse_relational_expression()
                if child:
                    root = ASTNode(n_type=ASTNodeType.EQL_EXP, n_text=token.get_text(), children=[root, child])
                else:
                    # todo: raise invalid equal expression exception
                    pass
        return root

    def parse_relational_expression(self):
        root = self.parse_additive_expression()
        if root:
            while self.tokens and self.tokens[0].get_type() == TokenType.REL:
                token = self.tokens.pop(0)  # relational symbol
                child = self.parse_additive_expression()
                if child:
                    root = ASTNode(n_type=ASTNodeType.REL_EXP, n_text=token.get_text(), children=[root, child])
                else:
                    # todo: raise invalid relational expression exception
                    pass
        return root

    def parse_additive_expression(self):
        root = self.parse_multiplicative_expression()
        if root:
            while self.tokens and self.tokens[0].get_type() == TokenType.ADD:
                token = self.tokens.pop(0)  # additive symbol
                child = self.parse_multiplicative_expression()
                if child:
                    root = ASTNode(n_type=ASTNodeType.ADD_EXP, n_text=token.get_text(), children=[root, child])
                else:
                    # todo: raise invalid additive expression exception
                    pass
        return root

    def parse_multiplicative_expression(self):
        root = self.parse_unary_expression()
        if root:
            while self.tokens and self.tokens[0].get_type() == TokenType.MUL:
                token = self.tokens.pop(0)  # multiplicative symbol
                child = self.parse_unary_expression()
                if child:
                    root = ASTNode(n_type=ASTNodeType.MUL_EXP, n_text=token.get_text(), children=[root, child])
                else:
                    # todo: raise invalid multiplicative expression exception
                    pass
        return root

    def parse_unary_expression(self):
        if self.tokens and self.tokens[0].get_type() in (TokenType.ADD, TokenType.LNT):
            token = self.tokens.pop(0)  # unary symbol
            child = self.parse_unary_expression()
            if child:
                return ASTNode(n_type=ASTNodeType.UNY_EXP, n_text=token.get_text(), children=[child])
            else:
                # todo: raise invalid unary expression exception
                pass
        else:
            return self.parse_primary_expression()

    def parse_primary_expression(self):
        if not self.tokens:
            return None

        if self.tokens[0].get_type() == TokenType.ID:
            return ASTNode(n_text=self.tokens.pop(0).get_text(), n_type=ASTNodeType.ID)
        if self.tokens[0].get_type() == TokenType.NUM_LIT:
            return ASTNode(n_text=self.tokens.pop(0).get_text(), n_type=ASTNodeType.NUM_LIT)
        if self.tokens[0].get_type() == TokenType.STR_LIT:
            return ASTNode(n_text=self.tokens.pop(0).get_text(), n_type=ASTNodeType.STR_LIT)
        if self.tokens[0].get_type() == TokenType.L_PAREN:
            self.tokens.pop(0)  # remove left paren
            node = self.parse_additive_expression()
            if node and self.tokens and self.tokens[0].get_type() == TokenType.R_PAREN:
                self.tokens.pop(0)  # remove right paren
            else:
                # todo: raise invalid parens exception
                pass
            return node

