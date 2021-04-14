from main.I_lexical.lexer import lexer
from main.I_lexical.token import TokenListPrinter
from main.II_syntactic.parser import Parser
from main.II_syntactic.node import ASTTreePrinter
from main.III_semantic.interpreter import Interpreter


def repl_execute(print_tokens=False, print_ast=False, print_var=False):
    """
    command line REPL（Read-Eval-Print Loop）
    """
    interpreter = Interpreter()
    while True:
        program = input(">> ")
        if program == "quit()" or program == "exit()":
            break

        # lexical analysis
        token_list = lexer(program)
        if print_tokens:
            TokenListPrinter.print(token_list)

        # syntactic analysis
        ast_root = Parser(token_list).parse_statement_list()
        if print_ast:
            ASTTreePrinter().print(ast_root)

        # semantic analysis and execution
        interpreter.interpret_statement_list(ast_root)
        if print_var:
            print(interpreter.get_variables())


if __name__ == "__main__":
    repl_execute()
