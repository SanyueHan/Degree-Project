from enum import Enum
import re


class TokenType(Enum):
    # Keywords: if、else、int
    INT = re.compile("int")

    # Identifier: age
    ID = re.compile("[a-zA-Z_]([a-zA-Z_]|[0-9])*")

    # Literal: 123, "apple"
    NUM_LIT = re.compile(r"[0-9]+\.[0-9]+|[0-9]+")
    STR_LIT = re.compile(r"\".*\"|\'.*\'")

    # Logical Operators
    AND = re.compile(r"&&")
    OR = re.compile(r"\|\|")

    # Relational Operators
    EQ = re.compile("==")
    NE = re.compile("!=")
    GE = re.compile(">=")
    GT = re.compile(">")
    LE = re.compile("<=")
    LT = re.compile("<")

    # Arithmetic Operators
    PLUS = re.compile("[+]")
    MINUS = re.compile("-")
    STAR = re.compile("[*]")
    SLASH = re.compile("/")

    # Other
    ASSIGNMENT = re.compile("=")
    SEMICOLON = re.compile(";")
    L_PAREN = re.compile(r"\(")
    R_PAREN = re.compile(r"\)")
    L_BRACKET = re.compile(r"\[")
    R_BRACKET = re.compile(r"]")
    L_BRACE = re.compile("{")
    R_BRACE = re.compile("}")

    WHITESPACE = re.compile(r"\s+")
    ANNOTATION = re.compile("%.*")  # in '.', '\r' or '\n' is automatically excluded


if __name__ == "__main__":
    # todo: lack 20 test cases
    if number_literal := re.findall(TokenType.NUM_LIT.value, "1234, 11.90"):
        print(number_literal)
    if string_literal := re.findall(TokenType.STR_LIT.value, "\'apple\', \"banana\""):
        print(string_literal)
    if and_operator := re.findall(TokenType.AND.value, "&&"):
        print(and_operator)
    if or_operator := re.findall(TokenType.OR.value, "||"):
        print(or_operator)
    if whitespace := re.findall(TokenType.WHITESPACE.value, "1 2\f3\n4\r5\t6\v"):
        print(whitespace)
    if annotation := re.findall(TokenType.ANNOTATION.value, "int a = 10; % this is annotation"):
        print(annotation)
