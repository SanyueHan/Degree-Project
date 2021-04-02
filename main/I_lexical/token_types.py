from enum import Enum
import re


class TokenType(Enum):
    KEYWORD = re.compile("break|clear|else|elseif|end|for|function|global|if|return|while")

    # Operators
    ADD = re.compile("[+]|-")
    MUL = re.compile(r"[*]|/|\\|\.\*|\./|\.\\")

    EQL = re.compile("==|~=")
    REL = re.compile(">=|>|<=|<")

    ASS = re.compile(r"=")

    LAN = re.compile(r"&&|&")
    LOR = re.compile(r"\|\||\|")
    LNT = re.compile(r"~")

    CLN = re.compile(":")

    TRA = re.compile(r"\.'|'")

    # Literal
    IDENTIFIER = re.compile(r"[a-zA-Z_]+[a-zA-Z0-9_]*")
    NUMBER_LIT = re.compile(r"[0-9]+\.[0-9]+|[0-9]+\.|\.[0-9]+|[0-9]+")
    STRING_LIT = re.compile(r"\"[^\"]*\"|\'[^\']*\'")

    # Other
    EO_STMT = re.compile("[;,\n]")
    L_PAREN = re.compile(r"\(")
    R_PAREN = re.compile(r"\)")
    L_BRACKET = re.compile(r"\[")
    R_BRACKET = re.compile(r"]")

    WHITESPACE = re.compile(r"\s+")
    ANNOTATION = re.compile("%.*")  # in '.', '\r' or '\n' is automatically excluded


if __name__ == "__main__":
    print(re.findall(TokenType.LAN.value, "a & b, a && b"))
    print(re.findall(TokenType.LOR.value, "c | d; c || d"))
    print(re.findall(TokenType.LNT.value, "~e"))
    print(re.findall(TokenType.MUL.value, r" * / \ .* ./ .\ "))
    print(re.findall(TokenType.NUMBER_LIT.value, "1234, 11.90, .23, 12."))
    print(re.findall(TokenType.STRING_LIT.value, "'apple', 'banana', \"candy\", \"dog\""))
    print(re.findall(TokenType.CLN.value, "1234 : 1234"))
    print(re.findall(TokenType.EO_STMT.value, "1234\nabc;1234,efg"))
    print(re.findall(TokenType.WHITESPACE.value, "1 2\f3\n4\r5\t6\v"))
    print(re.findall(TokenType.ANNOTATION.value, "int a = 10; % this is annotation"))
    print(re.findall(TokenType.IDENTIFIER.value, "Z123 78 ht a12a _1 "))
    print(re.findall(TokenType.KEYWORD.value, "if a==b"))
    print(re.findall(TokenType.ADD.value, "a=3+4-1"))
    print(re.findall(TokenType.EQL.value, r" a=1 b=3  ~= "))
    print(re.findall(TokenType.REL.value, "a>=1 b==1 c<1 d<=1"))
    print(re.findall(TokenType.ASS.value, r"a=1 b==c"))
    print(re.findall(TokenType.L_PAREN.value, r"\ ( ) "))
    print(re.findall(TokenType.R_PAREN.value, r"\ \\ ) ("))
    print(re.findall(TokenType.L_BRACKET.value, r"\ \ ] [ "))
    print(re.findall(TokenType.R_BRACKET.value, r' \ \ ] ['))
