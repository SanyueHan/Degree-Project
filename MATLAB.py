from main.I_lexical.lexical_analyzer import Lexical
from main.II_syntactic.syntactic_analyzer import Syntactic
from main.interpreter import Interpreter
import sys


def script_execute(filename):
    with open(filename, "r") as file:
        program = file.read()

    interpreter = Interpreter()

    token_lists = Lexical.program_analyzer(program)
    ast_root = Syntactic.program_analyzer(token_lists)
    interpreter.interpret_program(ast_root)


def repl_execute(token=False, node=False, var=False):
    """
    command line REPL（Read-Eval-Print Loop）
    """
    interpreter = Interpreter()
    while True:
        statement = input(">> ")
        if statement == "quit()" or statement == "exit()":
            break
        token_list = Lexical.statement_analyzer(statement)
        if token:
            for t in token_list:
                print(t)
        ast_root = Syntactic.statement_analyzer(token_list)
        if ast_root is None:
            continue
        if node:
            ast_root.dump()
        interpreter.interpret_statement(ast_root)
        if var:
            print(interpreter.get_variables())


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        for arg in sys.argv[1:]:
            script_execute(arg)
    else:
        repl_execute()
