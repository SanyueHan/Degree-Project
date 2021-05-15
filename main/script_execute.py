import os
from main.I_lexical.lexer import lexer
from main.I_lexical.token import TokenListPrinter
from main.II_syntactic.parser import Parser
from main.II_syntactic.node import ASTTreePrinter
from main.III_semantic.interpreter import Interpreter
from main.exceptions.interpret_exception import InterpretException


def script_execute(path, print_tokens=False, print_ast=False, print_var=False):
    """
    path: relative path from current working directory to the script
    print_tokens: whether to print lexical analysis result or not
    print_ast: whether to print syntactic analysis result or not
    print_var: whether to print executing result or not
    """
    with open(path, "r") as file:
        program = file.read()

    try:
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
    except InterpretException as e:
        print(os.getcwd() + '/' + path)
        print(e, end='')


if __name__ == "__main__":
    script_execute("../test_interpreter/test_cases/language_fundamentals/ii_matrices_and_arrays/test_float_question.m")
