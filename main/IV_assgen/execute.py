import os
from main.I_lexical.lexer import lexer
from main.I_lexical.token import TokenListPrinter
from main.II_syntactic.parser import Parser
from main.II_syntactic.node import ASTTreePrinter
from main.III_semantic.interpreter import Interpreter
from main.exceptions.interpret_exception import InterpretException

from main.IV_assgen.asmgen import Asmgen

with open("test_zy.m", "r") as file:
    program = file.read()

token_list = lexer(program)
ast_root = Parser(token_list).parse_statement_list()


asm = Asmgen(ast_root)
code = asm.generate()
print(code)