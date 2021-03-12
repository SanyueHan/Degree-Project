from II_syntactic.node import ASTNode
from II_syntactic.node_types import ASTNodeType
from II_syntactic.parser import Parser


class Syntactic:
    @staticmethod
    def statement_analyzer(token_list):
        ast_node = Parser(token_list[:]).parse_assignment_statement()
        if ast_node:
            return ast_node
        ast_node = Parser(token_list[:]).parse_expression_statement()
        if ast_node:
            return ast_node
        ast_node = Parser(token_list[:]).parse_clear_statement()
        if ast_node:
            return ast_node
        # todo: throw unknown statement exception

    @staticmethod
    def program_analyzer(token_lists):
        children = [Syntactic.statement_analyzer(token_list) for token_list in token_lists if token_list]
        ast_root = ASTNode(n_type=ASTNodeType.PROGRAM, children=children)
        return ast_root


if __name__ == "__main__":
    pass
