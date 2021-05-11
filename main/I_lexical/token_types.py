from enum import Enum
import re

NUMBER = r"[0-9]+\.[0-9]+|[0-9]+\.|\.[0-9]+|[0-9]+"


class TokenType(Enum):
    """
    https://ww2.mathworks.cn/help/matlab/matlab_prog/matlab-operators-and-special-characters.html
    """

    KEYWORD = re.compile("break|case|catch|classdef|continue|elseif|else|end|for|function|"
                         "global|if|otherwise|parfor|persistent|return|spmd|switch|try|while")
    NUMBER_LIT = re.compile(rf"({NUMBER})[eE][+-]?[0-9]+|{NUMBER}")
    STRING_LIT = re.compile(r"\"[^\"]*\"")
    VECTOR_LIT = re.compile(r"\'[^\']*\'")
    IDENTIFIER = re.compile(r"[a-zA-Z]+[a-zA-Z0-9_]*")

    # Arithmetic Operators
    ADD = re.compile("[+]|-")
    MUL = re.compile(r"[*]|/|\\|\.\*|\./|\.\\")
    POW = re.compile(r"\.\^|\^")
    TRA = re.compile(r"\.'|'")

    # Relational Operators
    REL = re.compile(">=|>|<=|<|==|~=")

    # Logical Operators
    SCA = re.compile(r"&&")    # short-circuiting and
    SCO = re.compile(r"\|\|")  # short-circuiting or
    EWA = re.compile(r"&")     # element-wise and
    EWO = re.compile(r"\|")    # element-wise or
    EWN = re.compile(r"~")     # element-wise not

    # Special Characters
    AT = re.compile(r"@")
    ELLIPSIS = re.compile(r"\.\.\.")
    DOT = re.compile(r"\.")
    EO_STMT = re.compile("[;,\n]")
    COLON = re.compile(":")
    L_PAREN = re.compile(r"\(")
    R_PAREN = re.compile(r"\)")
    L_BRACKET = re.compile(r"\[")
    R_BRACKET = re.compile(r"]")
    L_BRACE = re.compile(r"{")
    R_BRACE = re.compile(r"}")
    ANNOTATION = re.compile(r"%{[\s\S]*%}|%.*")  # in '.', '\r' or '\n' is automatically excluded
    EXCLAMATION = re.compile(r"!")
    QUESTION = re.compile(r"\?")
    WHITESPACE = re.compile(r"\s+")
    ASS = re.compile(r"=")


if __name__ == "__main__":
    print(re.findall(TokenType.KEYWORD.value, "elseif else if"))
    print(re.findall(TokenType.NUMBER_LIT.value, "1.234e003  1.23e 1234, 11.90, .23, 12."))
    print(re.findall(TokenType.STRING_LIT.value, "'apple', 'banana', \"candy\", \"dog\""))
    print(re.findall(TokenType.VECTOR_LIT.value, "\'vector literal\'"))
    print(re.findall(TokenType.IDENTIFIER.value, "Z123 78 ht a12a _1  "))
    # Arithmetic Operators
    print(re.findall(TokenType.ADD.value, "3+4-1"))
    print(re.findall(TokenType.MUL.value, r" * / \ .* ./ .\ "))
    print(re.findall(TokenType.POW.value, "a^b c.^d"))
    print(re.findall(TokenType.TRA.value, "M' C.'"))
    # Relational Operators
    print(re.findall(TokenType.REL.value, "a>=1 b==1 c<1 d<=1"))
    # Logical Operators
    print(re.findall(TokenType.SCA.value, "a && b"))
    print(re.findall(TokenType.SCO.value, "c || d"))
    print(re.findall(TokenType.EWA.value, "a & b"))
    print(re.findall(TokenType.EWO.value, "a | b"))
    print(re.findall(TokenType.EWN.value, "~e"))
    # Special Characters
    print(re.findall(TokenType.AT.value, "@abc"))
    print(re.findall(TokenType.ELLIPSIS.value, "..."))
    print(re.findall(TokenType.DOT.value, "."))
    print(re.findall(TokenType.EO_STMT.value, "1234\nabc;1234,efg"))
    print(re.findall(TokenType.COLON.value, "1234 : 1234"))
    print(re.findall(TokenType.L_PAREN.value, r"\ ( ) "))
    print(re.findall(TokenType.R_PAREN.value, r"\ \\ ) ("))
    print(re.findall(TokenType.L_BRACKET.value, r"\ \ ] [ "))
    print(re.findall(TokenType.R_BRACKET.value, r" \ \ ] ["))
    print(re.findall(TokenType.L_BRACE.value, r"  {  "))
    print(re.findall(TokenType.R_BRACE.value, R"  }  "))
    print(re.findall(TokenType.ANNOTATION.value, "not ann % ann 1\n not ann %{ ann 2 \n ann3 %} not ann"))
    print(re.findall(TokenType.EXCLAMATION.value, "!"))
    print(re.findall(TokenType.QUESTION.value, "?"))
    print(re.findall(TokenType.WHITESPACE.value, "1 2\f3\n4\r5\t6\v"))
    print(re.findall(TokenType.ASS.value, r"a=1"))
