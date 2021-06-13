from main.I_lexical.token import Token
from main.I_lexical.token_types import TokenType
from main.II_syntactic.node import ASTNode
from main.II_syntactic.node_types import ASTNodeType
from main.exceptions.ii_syntactic_exceptions import *


SEL_CLAUSES_MAP = {
    'if': ('elseif', 'else'),
    'switch': ('case', 'otherwise')
}


SEL_TERMINATOR_MAP = {
    'if': ('elseif', 'else', 'end'),
    'elseif': ('elseif', 'else', 'end'),
    'else': ('end', ),
    'case': ('case', 'otherwise', 'end'),
    'otherwise': ('end', )
}


NON_PREFIX_OPERATOR_TOKENS = {
    TokenType.MUL,
    TokenType.POW,
    TokenType.TRA,
    TokenType.REL,
    TokenType.SCA,
    TokenType.SCO,
    TokenType.EWA,
    TokenType.EWO,
    TokenType.EWN,
    TokenType.DOT,
    TokenType.COLON
}


def space_comma_convertor(token_list):
    """
    replace comma for space in some bracket expression cases
    """
    brackets_depth = 0
    for i in range(len(token_list)):
        this_type = token_list[i].get_type()
        last_type = token_list[i-1].get_type() if i else None
        next_type = token_list[i+1].get_type() if i+1 < len(token_list) else None

        if brackets_depth > 0:
            if this_type == TokenType.ADD and last_type == TokenType.WHITESPACE and next_type != TokenType.WHITESPACE:
                token_list[i-1].text = ','
                token_list[i-1].type = TokenType.EO_STMT
        if this_type == TokenType.L_BRACKET:
            brackets_depth += 1
        if this_type == TokenType.R_BRACKET:
            brackets_depth -= 1
    return token_list


class Parser:
    """
    https://ww2.mathworks.cn/help/matlab/matlab_prog/operator-precedence.html
    """

    def __init__(self, token_list):
        self.tokens = space_comma_convertor(token_list)
        if self.tokens:
            last = self.tokens[-1]
            self.tokens.append(Token(
                t_type=TokenType.EO_STMT,
                t_text='\n',
                row=last.row,
                col=last.col + len(last.text)
            ))
        self.last_token = None
        self.statement_cases = [
            self.parse_expression_statement,
            self.parse_selection_statement,
            self.parse_iteration_statement,
        ]
        self.primary_cases = {
            TokenType.NUMBER_LIT: self.parse_number_literal,
            TokenType.STRING_LIT: self.parse_string_literal,
            TokenType.VECTOR_LIT: self.parse_vector_literal,
            TokenType.L_PAREN: self.parse_paren_expression,
            TokenType.L_BRACKET: self.parse_bracket_expression,
            TokenType.IDENTIFIER: self.parse_identifier_expression,
        }

    def get_token(self, index=0):
        i = 0
        meaningful_tokens = []
        while len(meaningful_tokens) <= index:
            if len(self.tokens) > i:
                if self.tokens[i].get_type() not in (TokenType.WHITESPACE, TokenType.ANNOTATION):
                    meaningful_tokens.append(self.tokens[i])
                i += 1
            else:
                return None
        return meaningful_tokens[-1] if meaningful_tokens else None

    def get_token_type(self, index=0):
        token = self.get_token(index)
        if token:
            return token.get_type()

    def pop(self):
        if self.tokens:
            self.last_token = self.tokens.pop(0)
        else:
            return None

    def pop_token(self):
        self.pop()
        while self.last_token.get_type() in (TokenType.WHITESPACE, TokenType.ANNOTATION):
            self.pop()
        return self.last_token

    def complete_statement(self, node):
        if self.get_token_type() != TokenType.EO_STMT:
            token = self.get_token()
            raise InvalidExpressionError1(token.row, token.col)
        token = self.pop_token()
        node.add_child(ASTNode(n_type=ASTNodeType.EO_STMT,
                               n_text=token.get_text(),
                               n_line=token.row))
        return node

    def parse_statement_list(self, terminators=('None', )):
        """
        when parse program, terminators use it default value, only if no token left will the parsing stop
        when parse code blocks like selection, iteration, function, terminators will be some specified keywords
        """
        node = ASTNode(n_type=ASTNodeType.STMT_LIST)
        while str(self.get_token()) not in terminators:
            if self.get_token() is None:
                # indicates a invalid code block error, but raise outside the block
                return None
            if self.get_token_type() == TokenType.EO_STMT:
                self.pop_token()
                continue
            node.add_child(self.parse_statement())
        return node

    def parse_statement(self):
        for stmt in self.statement_cases:
            node = stmt()
            if node:
                return node

    def parse_expression_statement(self):
        expression = self.parse_expression()
        if expression is None:
            return None
        node = ASTNode(n_type=ASTNodeType.EXP_STMT,
                       children=[expression])
        return self.complete_statement(node)

    def parse_selection_statement(self):
        if self.get_token().get_text() not in ("if", 'switch'):
            return None
        node = ASTNode(n_type=ASTNodeType.SEL_STMT,
                       n_text=self.get_token().get_text(),
                       n_line=self.get_token().get_line())

        start_token = self.pop_token()

        # firstly a if/switch
        clause = self.parse_selection_clause(start_token.get_text())
        if clause is None:
            raise EndMissingError(start_token.row, start_token.col)
        node.add_child(clause)

        a, b = SEL_CLAUSES_MAP[start_token.get_text()]
        # then unlimited elseif/case
        while self.get_token().get_text() == a:
            clause = self.parse_selection_clause(self.pop_token().get_text())
            if clause is None:
                raise EndMissingError(start_token.row, start_token.col)
            node.add_child(clause)

        # finally sometimes a else/otherwise
        if self.get_token().get_text() == b:
            clause = self.parse_selection_clause(self.pop_token().get_text())
            if clause is None:
                raise EndMissingError(start_token.row, start_token.col)
            node.add_child(clause)

        self.pop_token()  # remove 'end'

        return self.complete_statement(node)

    def parse_selection_clause(self, clause):
        node = ASTNode(n_type=ASTNodeType.SEL_ClS,
                       n_text=clause)

        if clause not in ('else', 'otherwise'):
            expression = self.parse_logic_or_expression()
            node.add_child(expression)

        if clause != 'switch':
            statement_list = self.parse_statement_list(terminators=SEL_TERMINATOR_MAP[clause])
            if statement_list is None:
                # exception raised outside
                return None
            node.add_child(statement_list)
        else:
            # remove redundant EO_STMT tokens after switch before the first case
            while self.get_token_type() == TokenType.EO_STMT:
                self.pop_token()

        return node

    def parse_iteration_statement(self):
        if self.get_token().get_text() not in ('while', 'for'):
            return None
        node = ASTNode(n_type=ASTNodeType.ITR_STMT,
                       n_text=self.get_token().get_text(),
                       n_line=self.get_token().get_line())
        start_token = self.pop_token()

        clause = self.parse_iteration_clause(start_token.get_text())
        if clause is None:
            raise EndMissingError(start_token.row, start_token.col)
        node.add_child(clause)

        self.pop_token()  # remove 'end'

        return self.complete_statement(node)

    def parse_iteration_clause(self, clause):
        node = ASTNode(n_type=ASTNodeType.ITR_CLS,
                       n_text=clause)

        expression = self.parse_logic_or_expression() if clause == 'while' else self.parse_assignment_expression()
        if expression is None:
            # exception raised outside
            return None
        node.add_child(expression)

        statement_list = self.parse_statement_list(terminators=('end', ))
        if statement_list is None:
            # exception raised outside
            return None
        node.add_child(statement_list)

        return node

    def parse_identifier_list(self):
        node = ASTNode(n_type=ASTNodeType.IDENT_LIST_EXP)
        while self.get_token_type() == TokenType.IDENTIFIER:
            token = self.pop_token()
            node.add_child(ASTNode(n_type=ASTNodeType.IDENTIFIER_EXP,
                                   n_text=token.get_text(),
                                   n_line=token.get_text()))
        return node

    def parse_expression(self):
        node = self.parse_assignment_expression()
        if node:
            return node
        node = self.parse_logic_or_expression()
        if node:
            return node

    def parse_assignment_expression(self):
        if self.get_token_type() != TokenType.IDENTIFIER or self.get_token_type(1) != TokenType.ASS:
            return None
        token = self.pop_token()
        identifier = ASTNode(n_type=ASTNodeType.IDENTIFIER_EXP,
                             n_text=token.get_text(),
                             n_line=token.get_line())
        token = self.pop_token()
        node = ASTNode(n_type=ASTNodeType.ASS_EXP,
                       n_text=token.get_text(),
                       n_line=token.get_line(),
                       children=[identifier, self.parse_logic_or_expression()])
        return node

    def parse_logic_or_expression(self):
        root = self.parse_logic_and_expression()
        while self.get_token_type() == TokenType.SCO:
            token = self.pop_token()  # '|'
            child = self.parse_logic_and_expression()
            root = ASTNode(n_type=ASTNodeType.BOP_EXP,
                           n_text=token.get_text(),
                           n_line=token.get_line(),
                           children=[root, child])
        return root

    def parse_logic_and_expression(self):
        root = self.parse_level_8_expression()
        while self.get_token_type() == TokenType.SCA:
            token = self.pop_token()  # '&'
            child = self.parse_level_8_expression()
            root = ASTNode(n_type=ASTNodeType.BOP_EXP,
                           n_text=token.get_text(),
                           n_line=token.get_line(),
                           children=[root, child])
        return root

    def parse_level_8_expression(self):
        """
        binary relational operators (left associate):
        """
        root = self.parse_level_7_expression()
        while self.get_token_type() == TokenType.REL:
            token = self.pop_token()  # relational symbol
            child = self.parse_level_7_expression()
            root = ASTNode(n_type=ASTNodeType.BOP_EXP,
                           n_text=token.get_text(),
                           n_line=token.get_line(),
                           children=[root, child])
        return root

    def parse_level_7_expression(self):
        """
        binary/trinary colon operator (left associate): :
        """
        root = self.parse_level_6_expression()
        while self.get_token_type() == TokenType.COLON:
            token = self.pop_token()  # ':'
            node1 = self.parse_level_6_expression()
            root = ASTNode(n_type=ASTNodeType.CLN_EXP,
                           n_text=token.get_text(),
                           n_line=token.get_line(),
                           children=[root, node1])
            if self.get_token_type() == TokenType.COLON:
                self.pop_token()  # the second ':'
                node2 = self.parse_level_6_expression()
                root.add_child(node2)
        return root

    def parse_level_6_expression(self):
        """
        binary additive operators (left associate): + -
        """
        root = self.parse_level_5_expression()
        while self.get_token_type() == TokenType.ADD:
            token = self.pop_token()  # additive symbol
            child = self.parse_level_5_expression()
            root = ASTNode(n_type=ASTNodeType.BOP_EXP,
                           n_text=token.get_text(),
                           n_line=token.get_line(),
                           children=[root, child])
        return root

    def parse_level_5_expression(self):
        """
        binary multiplicative operators (left associate): .* ./ .\\ * / \\
        """
        root = self.parse_level_4_expression()
        while self.get_token_type() == TokenType.MUL:
            token = self.pop_token()  # multiplicative symbol
            child = self.parse_level_4_expression()
            root = ASTNode(n_type=ASTNodeType.BOP_EXP,
                           n_text=token.get_text(),
                           n_line=token.get_line(),
                           children=[root, child])
        return root

    def parse_level_4_expression(self, next_level=None):
        """
        unary prefix operators: + - ~
        """
        if self.get_token_type() in (TokenType.ADD, TokenType.EWN):
            token = self.pop_token()  # unary operator symbol
            child = self.parse_level_4_expression()
            return ASTNode(n_type=ASTNodeType.UOP_EXP,
                           n_text=token.get_text(),
                           n_line=token.get_line(),
                           children=[child])
        return self.parse_level_2_expression() if next_level is None else next_level()

    def parse_level_2_expression(self):
        """
        unary postfix operators: .' '
        binary operators (left associate): .^ ^
        """
        root = self.parse_primary_expression()
        while self.get_token_type() in (TokenType.TRA, TokenType.POW):
            if self.get_token_type() == TokenType.TRA:
                token = self.pop_token()  # transpose symbol
                root = ASTNode(n_type=ASTNodeType.UOP_EXP,
                               n_text=token.get_text(),
                               n_line=token.get_line(),
                               children=[root])
            else:
                token = self.pop_token()  # power symbol
                child = self.parse_level_4_expression(next_level=self.parse_primary_expression)
                root = ASTNode(n_type=ASTNodeType.BOP_EXP,
                               n_text=token.get_text(),
                               n_line=token.get_line(),
                               children=[root, child])
        return root

    def parse_primary_expression(self):
        if self.get_token_type() == TokenType.KEYWORD:
            # not parsed as expression,
            # instead, parsed by other statement parser method following expression statement
            return None
        if self.get_token_type() in self.primary_cases:
            return self.primary_cases[self.get_token_type()]()

        token = self.get_token()
        if self.get_token_type() == TokenType.EO_STMT:
            raise InvalidExpressionError2(token.row, token.col)
        if self.get_token_type() in NON_PREFIX_OPERATOR_TOKENS:
            raise InvalidOperatorError(token.row, token.col)
        raise InvalidExpressionError3(token.row, token.col)

    def parse_number_literal(self):
        token = self.pop_token()
        return ASTNode(n_type=ASTNodeType.NUMBER_LIT_EXP,
                       n_text=token.get_text(),
                       n_line=token.get_line())

    def parse_string_literal(self):
        token = self.pop_token()
        return ASTNode(n_type=ASTNodeType.STRING_LIT_EXP,
                       n_text=token.get_text().strip('\"'),
                       n_line=token.get_line())

    def parse_vector_literal(self):
        token = self.pop_token()
        return ASTNode(n_type=ASTNodeType.VECTOR_LIT_EXP,
                       n_text=token.get_text().strip('\''),
                       n_line=token.get_line())

    def parse_paren_expression(self):
        self.pop_token()  # remove left paren
        node = self.parse_logic_or_expression()
        if node and self.get_token_type() == TokenType.R_PAREN:
            self.pop_token()  # remove right paren
        else:
            token = self.get_token()
            raise InvalidExpressionError3(token.row, token.col)
        return node

    def parse_bracket_expression(self):
        token = self.pop_token()  # remove left bracket
        node = ASTNode(n_type=ASTNodeType.ARRAY_LIST_EXP,
                       n_line=token.get_line())
        while self.get_token_type() != TokenType.R_BRACKET:
            if self.get_token_type() == TokenType.EO_STMT:
                self.pop_token()  # remove unnecessary delimiters

            if self.get_token_type() is None:
                self.pop_token()
                raise IncompleteStatementError(self.last_token.row, self.last_token.col)

            child = self.parse_logic_or_expression()
            node.add_child(child)

            while self.get_token_type() == TokenType.EO_STMT:
                token = self.pop_token()  # EO_STMT
                node.add_child(ASTNode(n_type=ASTNodeType.EO_STMT,
                                       n_text=token.get_text(),
                                       n_line=token.get_line()))
        self.pop_token()  # remove right bracket
        return node

    def parse_identifier_expression(self):
        token = self.pop_token()
        root = ASTNode(n_type=ASTNodeType.IDENTIFIER_EXP,
                       n_text=token.get_text(),
                       n_line=token.get_line())
        if self.get_token_type() == TokenType.L_PAREN:
            self.pop_token()  # remove left paren
            node = self.parse_index_list()
            self.pop_token()  # remove right paren
            root.add_child(node)
        return root

    def parse_index_list(self):
        root = ASTNode(n_type=ASTNodeType.INDEX_LIST_EXP)
        while self.get_token_type() != TokenType.R_PAREN:
            if self.get_token_type() == TokenType.COLON:
                token = self.pop_token()  # COLON
                root.add_child(ASTNode(n_type=ASTNodeType.CLN_EXP,
                                       n_text=token.get_text(),
                                       n_line=token.get_line()))
            else:
                child = self.parse_logic_or_expression()
                root.add_child(child)

            if str(self.get_token()) == ",":
                # one argument finished, continue to parse another argument
                self.pop_token()
            else:
                if self.get_token_type() != TokenType.R_PAREN:
                    token = self.get_token()
                    raise InvalidExpressionError3(token.row, token.col)
        return root
