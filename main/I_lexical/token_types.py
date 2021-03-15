from enum import Enum
import re


class TokenType(Enum):
    KEYWORD = re.compile("break|clear|else|elseif|end|for|function|global|if|return|while")
    ID = re.compile("[a-zA-Z_]([a-zA-Z_]|[0-9])*")

    # Logical Operators
    LAN = re.compile(r"&")
    LOR = re.compile(r"\|")
    LNT = re.compile(r"~")

    # Relational Operators
    EQL = re.compile("==|!=")
    REL = re.compile(">=|>|<=|<")

    # Assignment Operators
    ASS = re.compile(r"=")

    # Arithmetic Operators
    ADD = re.compile("[+]|-")
    MUL = re.compile("[*]|/")

    # Literal
    NUM_LIT = re.compile(r"[0-9]+\.[0-9]+|[0-9]+\.|\.[0-9]+|[0-9]+")
    STR_LIT = re.compile(r"\".*\"|\'.*\'")

    # Other
    EO_STMT = re.compile("[;,\n]")
    L_PAREN = re.compile(r"\(")
    R_PAREN = re.compile(r"\)")
    L_BRACKET = re.compile(r"\[")
    R_BRACKET = re.compile(r"]")

    WHITESPACE = re.compile(r"\s+")
    ANNOTATION = re.compile("%.*")  # in '.', '\r' or '\n' is automatically excluded


if __name__ == "__main__":
    # todo: lack 10 test cases
    print(re.findall(TokenType.LAN.value, "a & b"))
    print(re.findall(TokenType.LOR.value, "c | d"))
    print(re.findall(TokenType.LNT.value, "~e"))
    print(re.findall(TokenType.ASS.value, "int age = 5"))
    print(re.findall(TokenType.NUM_LIT.value, "1234, 11.90, .23, 12."))
    print(re.findall(TokenType.STR_LIT.value, "\'apple\', \"banana\""))
    print(re.findall(TokenType.EO_STMT.value, "1234\nabc;1234,efg"))
    print(re.findall(TokenType.WHITESPACE.value, "1 2\f3\n4\r5\t6\v"))
    print(re.findall(TokenType.ANNOTATION.value, "int a = 10; % this is annotation"))
