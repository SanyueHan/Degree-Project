from I_lexical.lexical_analyzer import Lexical
from II_syntactic.syntactic_analyzer import Syntactic
from interpreter import Interpreter
import sys


def script_execute(filename):
    with open(filename) as file:
        program = file.read()

    interpreter = Interpreter()

    token_lists = Lexical.program_analyzer(program)
    ast_root = Syntactic.program_analyzer(token_lists)
    interpreter.interpret_program(ast_root)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        for arg in sys.argv[1:]:
            script_execute(arg)
    else:
        script_execute("test_cases/test_exp_ass.m")
