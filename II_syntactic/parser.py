from II_syntactic.node import ASTNode
from II_syntactic.node_types import ASTNodeType
from I_lexical.token_types import TokenType


class Parser:
    r"""
    A single-statement syntax parser
    capable for expression, assignment, and declaration
    the rules supported include (in Extended Backus-Naur-Form):
    program -> exp_stmt | ass_stmt | dcl_stmt

    dcl_stmt -> 'int' id ( = add_exp)? ;?
    ass_stmt -> id = exp ;?
    exp_stmt -> exp ;?

    exp -> lor_exp
    lor_exp -> lnd_exp (|| lnd_exp)*
    lnd_exp -> eql_exp (&& eql_exp)*
    eql_exp -> rel_exp ((!=|==) rel_exp)*
    rel_exp -> add_exp ((<=|<|>=|>) add_exp)*
    add_exp -> mul_exp ((+|-) mul_exp)*
    mul_exp -> pri_exp ((*|/) pri_exp)*
    pri_exp -> id | num_lit | (add_exp)
    """
    def __init__(self, token_list):
        self.tokens = token_list

    def parse_declaration_statement(self):
        node = None
        if self.tokens and self.tokens[0].get_type() == TokenType.INT:
            self.tokens.pop(0)  # remove int
            if self.tokens and self.tokens[0].get_type() == TokenType.ID:
                node = ASTNode(n_text=self.tokens.pop(0).get_text(), n_type=ASTNodeType.DCL_STMT)
                if self.tokens and self.tokens[0].get_type() == TokenType.ASSIGNMENT:
                    self.tokens.pop(0)  # remove '='
                    child = self.parse_additive_expression()
                    if child:
                        node.add_child(child)
                    else:
                        # todo: throw invalid declaration statement exception
                        pass
                if self.tokens:
                    if self.tokens[0].get_type() == TokenType.SEMICOLON:
                        node.stmt = True
                    else:
                        # todo: throw invalid declaration statement exception
                        pass
            else:
                # todo: throw no variable name error
                pass
        return node

    def parse_assignment_statement(self):
        node = None
        if self.tokens and self.tokens[0].get_type() == TokenType.ID:
            node = ASTNode(n_text=self.tokens.pop(0).get_text(), n_type=ASTNodeType.ASS_STMT)
            if self.tokens and self.tokens[0].get_type() == TokenType.ASSIGNMENT:
                self.tokens.pop(0)  # remove '='
                child = self.parse_expression()
                if child:
                    node.add_child(child)
                    if self.tokens:
                        if self.tokens[0].get_type() == TokenType.SEMICOLON:
                            node.stmt = True
                        else:
                            # todo: throw raise invalid assignment statement exception
                            pass
                else:
                    # todo: throw invalid assignment statement exception
                    pass
            else:
                # ID without "=" is an expression statement, not parsed at this function
                node = None
        return node

    def parse_expression_statement(self):
        node = None
        if self.tokens:
            node = ASTNode(n_type=ASTNodeType.EXP_STMT)
            child = self.parse_expression()
            if child:
                node.add_child(child)
                if self.tokens:
                    if self.tokens[0].get_type() == TokenType.SEMICOLON:
                        node.stmt = True
                    else:
                        # todo: throw raise invalid expression statement exception
                        pass
            else:
                # todo: throw raise invalid expression statement exception
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
            while self.tokens and self.tokens[0].get_type() == TokenType.LND:
                token = self.tokens.pop(0)  # logic and symbol
                child = self.parse_equal_expression()
                if child:
                    root = ASTNode(n_type=ASTNodeType.LND_EXP, n_text=token.get_text(), children=[root, child])
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
        root = self.parse_primary_expression()
        if root:
            while self.tokens and self.tokens[0].get_type() == TokenType.MUL:
                token = self.tokens.pop(0)  # multiplicative symbol
                child = self.parse_primary_expression()
                if child:
                    root = ASTNode(n_type=ASTNodeType.MUL_EXP, n_text=token.get_text(), children=[root, child])
                else:
                    # todo: raise invalid multiplicative expression exception
                    pass
        return root

    def parse_primary_expression(self):
        if self.tokens:
            if self.tokens[0].get_type() == TokenType.ID:
                return ASTNode(n_text=self.tokens.pop(0).get_text(), n_type=ASTNodeType.ID)
            if self.tokens[0].get_type() == TokenType.NUM_LIT:
                return ASTNode(n_text=self.tokens.pop(0).get_text(), n_type=ASTNodeType.NUM_LIT)
            if self.tokens[0].get_type() == TokenType.L_PAREN:
                self.tokens.pop(0)  # remove left paren
                node = self.parse_additive_expression()
                if node and self.tokens and self.tokens[0].get_type() == TokenType.R_PAREN:
                    self.tokens.pop(0)  # remove right paren
                else:
                    # todo: raise invalid parens exception
                    pass
                return node
