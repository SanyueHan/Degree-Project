from I_lexical.lexical_analyzer import Lexical
from II_syntactic.syntactic_analyzer import Syntactic


def test_lexical_analyzer(statement):
    token_list = Lexical.statement_analyzer(statement)
    for token in token_list:
        print(token.get_type(), token.get_text())


def test_syntactic_analyzer(statement):
    token_list = Lexical.statement_analyzer(statement)
    node = Syntactic.statement_analyzer(token_list)
    print(statement)
    if node:
        node.dump()
    print()


if __name__ == '__main__':
    statements1 = [
        "1;",
        "1+2;",
        "1+2+3;",
        "1+2+3*4;",
        "1+2+3*4/5;",
        "int a = 6;",
        "a = 7;",
        "int b = a+8;",
        "int c = a+b+5*6*(7+8*9+10);"
    ]
    statements2 = [
        "1",
        "2+3",
        "4*5",
        "int a = 6",
        "int b = a+(7+8)"
    ]
    for s in statements1:
        test_syntactic_analyzer(s)
    for s in statements2:
        test_syntactic_analyzer(s)
