from II_syntactic.node import ASTNode
from II_syntactic.node_types import ASTNodeType
from II_syntactic.parser import Parser


class Syntactic:
    @staticmethod
    def statement_analyzer(token_list):
        if ast_node := Parser(token_list[:]).parse_declaration_statement():
            return ast_node
        # parsing assignment before parsing expression because of corner case like "a = 1"
        if ast_node := Parser(token_list[:]).parse_assignment_statement():
            return ast_node
        if ast_node := Parser(token_list[:]).parse_expression_statement():
            return ast_node
        # todo: throw unknown statement exception

    @staticmethod
    def program_analyzer(token_lists):
        children = [Syntactic.statement_analyzer(token_list) for token_list in token_lists]
        children = [child for child in children if child]
        ast_root = ASTNode(n_type=ASTNodeType.PROGRAM, children=children)
        return ast_root

