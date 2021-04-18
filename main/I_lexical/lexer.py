from main.I_lexical.token_types import TokenType
from main.I_lexical.token import Token
from main.exceptions.lexical_exception import *


def lexer(program):
    row = 0
    result_token_list = []
    lines = [line + '\n' for line in program.split('\n')]
    for line in lines:
        row += 1
        col = 0
        text = ''
        while line:
            for TYPE in TokenType:
                match = TYPE.value.match(line)
                if match:
                    # if the token before ' is white space or there is no token before ',
                    # it is a CharacterVectorTerminationError,
                    # otherwise it would be considered as a normal transpose character at the lexical analysis stage.
                    if TYPE == TokenType.TRA:
                        if TokenType.WHITESPACE.value.sub('', text) == '':
                            raise CharacterVectorTerminationError(row, col + 1)

                    text = match.group()
                    line = line[len(text):]
                    if TYPE != TokenType.WHITESPACE and TYPE != TokenType.ANNOTATION:
                        result_token_list.append(Token(t_type=TYPE, t_text=text, row=row, col=col))
                    col += len(text)
                    break
            else:
                if line[0] in "#$`":
                    raise InvalidCharacterError(row, col + 1)
                elif line[0] == '\"':
                    raise StringTerminationError(row, col + 1)
                else:
                    raise InvalidCharacterError(row, col + 1)

    return result_token_list
