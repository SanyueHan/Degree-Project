import re
from main.I_lexical.token_types import TokenType
from main.I_lexical.token import Token
from main.exceptions.i_lexical_exception import *


def lexer(code):
    token_regex = '|'.join(f'(?P<{token_type.name}>{token_type.value})' for token_type in TokenType)
    row = 1
    last_newline_end = 0
    result_token_list = []
    for match in re.finditer(token_regex, code):
        match_type = TokenType[match.lastgroup]
        match_text = match.group()
        col = match.start() - last_newline_end + 1
        if match_type == TokenType.TRA:
            if not result_token_list or result_token_list[-1].get_type() in (TokenType.EO_STMT, TokenType.WHITESPACE):
                raise CharacterVectorTerminationError(row, col)
        if match_type == TokenType.ANNOTATION:
            if match_text[:2] == "%{" and match_text[-2:] != "%}":
                raise AnnotationBlockTerminationError(row+match_text.count('\n'), len(match_text.split('\n')[-1])+1)
        if match_type == TokenType.MISS:
            if match_text[0] == '"':
                raise StringTerminationError(row, col)
            else:  # "#$`"
                raise InvalidCharacterError(row, col)
        result_token_list.append(Token(t_type=match_type, t_text=match_text, row=row, col=col))
        if '\n' in match_text:
            row += match_text.count('\n')
            last_newline_end = match.end()-len(match_text.split('\n')[-1])  # consider multi-line annotation
    return result_token_list
