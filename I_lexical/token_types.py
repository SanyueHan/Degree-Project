from enum import Enum
import re


class TokenType(Enum):
    # Keywords
    INT = re.compile("int")

    # Identifier
    ID = re.compile("[a-zA-Z_]([a-zA-Z_]|[0-9])*")

    # Literal
    NUM_LIT = re.compile(r"-?([0-9]+\.[0-9]+|[0-9]+)")
    STR_LIT = re.compile(r"\".*\"|\'.*\'")

    # Logical Operators
    LAN = re.compile(r"&&")
    LOR = re.compile(r"\|\|")

    # Relational Operators
    EQL = re.compile("==|!=")
    REL = re.compile(">=|>|<=|<")

    # Arithmetic Operators
    ADD = re.compile("[+]|-")
    MUL = re.compile("[*]|/")

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
    # todo: lack 14 test cases
    if number_literal := re.findall(TokenType.NUM_LIT.value, "1234, 11.90"):
        print(number_literal)
    if string_literal := re.findall(TokenType.STR_LIT.value, "\'apple\', \"banana\""):
        print(string_literal)
    if logic_and := re.findall(TokenType.LAN.value, "&&"):
        print(logic_and)
    if logic_or := re.findall(TokenType.LOR.value, "||"):
        print(logic_or)
    if whitespace := re.findall(TokenType.WHITESPACE.value, "1 2\f3\n4\r5\t6\v"):
        print(whitespace)
    if annotation := re.findall(TokenType.ANNOTATION.value, "int a = 10; % this is annotation"):
        print(annotation)
