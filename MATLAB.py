from main.I_lexical.lexer import lexer
from main.II_syntactic.parser import Parser
from main.interpreter import Interpreter
import sys


def script_execute(filename, token=False, node=False, var=False):
    with open(filename, "r") as file:
        program = file.read()

    token_list = lexer(program)
    if token:
        for t in token_list:
            print(t)
    ast_root = Parser(token_list).parse_statement_list()
    interpreter = Interpreter()
    if node:
        ast_root.dump()
    interpreter.interpret_statement_list(ast_root)
    if var:
        print(interpreter.get_variables())


def repl_execute(token=False, node=False, var=False):
    """
    command line REPL（Read-Eval-Print Loop）
    """
    interpreter = Interpreter()
    while True:
        program = input(">> ")
        if program == "quit()" or program == "exit()":
            break
        token_list = lexer(program)
        if token:
            for t in token_list:
                print(t)
        ast_root = Parser(token_list).parse_statement_list()
        if node:
            ast_root.dump()
        interpreter.interpret_statement_list(ast_root)
        if var:
            print(interpreter.get_variables())


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        for arg in sys.argv[1:]:
            script_execute(arg)
    else:
        repl_execute()
