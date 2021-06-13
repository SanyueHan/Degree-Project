from enum import Enum
import re

NUMBER = r"[0-9]+\.[0-9]+|[0-9]+\.|\.[0-9]+|[0-9]+"


class TokenType(Enum):
    """
    https://ww2.mathworks.cn/help/matlab/matlab_prog/matlab-operators-and-special-characters.html
    """

    KEYWORD = "break|case|catch|classdef|continue|elseif|else|end|for|function|global|if|otherwise|parfor|persistent" \
              "|return|spmd|switch|try|while"
    NUMBER_LIT = rf"({NUMBER})[eE][+-]?[0-9]+|{NUMBER}"
    STRING_LIT = r"\"[^\"\n]*\""
    VECTOR_LIT = r"\'[^\'\n]*\'"
    IDENTIFIER = r"[a-zA-Z]+[a-zA-Z0-9_]*"

    # Arithmetic Operators
    ADD = "[+]|-"
    MUL = r"[*]|/|\\|\.\*|\./|\.\\"
    POW = r"\.\^|\^"
    TRA = r"\.'|'"

    # Relational Operators
    REL = ">=|>|<=|<|==|~="

    # Logical Operators
    SCA = r"&&"    # short-circuiting and
    SCO = r"\|\|"  # short-circuiting or
    EWA = r"&"     # element-wise and
    EWO = r"\|"    # element-wise or
    EWN = r"~"     # element-wise not

    # Special Characters
    AT = r"@"
    ELLIPSIS = r"\.\.\."
    DOT = r"\."
    EO_STMT = "[;,\n]"
    COLON = ":"
    L_PAREN = r"\("
    R_PAREN = r"\)"
    L_BRACKET = r"\["
    R_BRACKET = r"]"
    L_BRACE = r"{"
    R_BRACE = r"}"
    ANNOTATION = r"(?<![^\n])%{(?![^\n])[\s\S]*((?<![^\n])%}(?![^\n]))?|%.*"
    EXCLAMATION = r"!"
    QUESTION = r"\?"
    WHITESPACE = r"[ \f\r\t\v]+"  # \s excluding \n
    ASS = r"="
    MISS = r"."


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
