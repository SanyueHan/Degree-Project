from main.I_lexical.token_types import TokenType
from main.I_lexical.token import Token
from main.exceptions.i_lexical_exception import *


def lexer(program):
    row = 1
    result_token_list = []
    lines = [line + '\n' for line in program.split('\n')]
    for line in lines:
        col = 1
        while line:
            for TYPE in TokenType:
                match = TYPE.value.match(line)
                if match:
                    # if the token before ' is white space or there is no token before ',
                    # it is a CharacterVectorTerminationError,
                    # otherwise it would be considered as a normal transpose character at the lexical analysis stage.
                    if TYPE == TokenType.TRA:
                        if not result_token_list or result_token_list[-1].get_type() == TokenType.WHITESPACE:
                            raise CharacterVectorTerminationError(row, col)

                    token_text = match.group()
                    result_token_list.append(Token(t_type=TYPE, t_text=token_text, row=row, col=col))
                    line = line[len(token_text):]
                    col += len(token_text)
                    break
            else:
                if line[0] == '"':
                    raise StringTerminationError(row, col)
                else:  # line[0] in "#$`"
                    raise InvalidCharacterError(row, col)
        row += 1
    return result_token_list
