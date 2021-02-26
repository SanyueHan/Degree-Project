from I_lexical.lexical_analyzer import Lexical
from II_syntactic.syntactic_analyzer import Syntactic
from interpreter import Interpreter


def repl_execute(token=False, node=False, var=False):
    """
    command line REPL（Read-Eval-Print Loop）
    support arithmetic, variable declaration and variable assignment
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
        if node:
            if ast_root:
                ast_root.dump()
            else:
                print("ast_root is None")
        interpreter.interpret_statement(ast_root)
        if var:
            print(interpreter.get_variables())


if __name__ == "__main__":
    repl_execute()
