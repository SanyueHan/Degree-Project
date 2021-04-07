from main.I_lexical.lexer import lexer
from main.II_syntactic.parser import Parser
from main.II_syntactic.node import ASTTreePrinter
from main.interpreter import Interpreter


def script_execute(filename, print_tokens=False, print_ast=False, print_var=False):
    with open(filename, "r") as file:
        program = file.read()

    token_list = lexer(program)
    if print_tokens:
        for t in token_list:
            print(repr(t))
    ast_root = Parser(token_list).parse_statement_list()
    interpreter = Interpreter()
    if print_ast:
        ASTTreePrinter().print(ast_root)
    interpreter.interpret_statement_list(ast_root)
    if print_var:
        print(interpreter.get_variables())


if __name__ == "__main__":
    script_execute("../test/designed_input/test_unary_operators.m")
