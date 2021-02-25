from enum import Enum
import re


token_regex = {
    # Keywords: if、else、int
    'INT': "int",

    # Literal: 123, "apple"
    'INT_LIT': "[0-9]+",
    'STR_LIT': r"\".*\"|\'.*\'",

    # Operators: +、-、=
    'PLUS': "[+]",
    'MINUS': "-",
    'STAR': "[*]",
    'SLASH': "/",

    'GE': ">=",
    'GT': ">",
    'EQ': "==",
    'NE': "!=",
    'LE': "<=",
    'LT': "<",

    'SEMICOLON': ";",
    'L_PAREN': r"\(",
    'R_PAREN': r"\)",
    'L_BRACKET': r"\[",
    'R_BRACKET': r"\]",
    'L_BRACE': "{",
    'R_BRACE': "}",

    'ASSIGNMENT': "=",

    # Identifier: age
    'ID': "[a-zA-Z_]([a-zA-Z_]|[0-9])*",

    'WHITESPACE': r"\s+",
    'ANNOTATION': "%.*",  # in '.', '\r' or '\n' is automatically excluded
}

TokenType = Enum('TokenType', [(key, re.compile(token_regex[key])) for key in token_regex])


if __name__ == "__main__":
    # todo: lack 20 test cases
    if int_literal := re.findall(TokenType.INT_LIT.value, "int a = 1234"):
        print(int_literal)
    if str_literal := re.findall(TokenType.STR_LIT.value, "\'apple\', \"banana\""):
        print(str_literal)
    if whitespace := re.findall(TokenType.WHITESPACE.value, "1 2\f3\n4\r5\t6\v"):
        print(whitespace)
    if annotation := re.findall(TokenType.ANNOTATION.value, "int a = 10; % this is annotation"):
        print(annotation)
