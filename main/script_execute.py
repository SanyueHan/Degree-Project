from main.I_lexical.lexer import lexer
from main.I_lexical.token import TokenListPrinter
from main.II_syntactic.parser import Parser
from main.II_syntactic.node import ASTTreePrinter
from main.III_semantic.interpreter import Interpreter


def script_execute(filename, print_tokens=False, print_ast=False, print_var=False):
    with open(filename, "r") as file:
        program = file.read()

    # lexical analysis
    token_list = lexer(program)
    if print_tokens:
        TokenListPrinter.print(token_list)

    # syntactic analysis
    ast_root = Parser(token_list).parse_statement_list()
    interpreter = Interpreter()
    if print_ast:
        ASTTreePrinter().print(ast_root)

    # semantic analysis and execution
    interpreter.interpret_statement_list(ast_root)
    if print_var:
        print(interpreter.get_variables())
