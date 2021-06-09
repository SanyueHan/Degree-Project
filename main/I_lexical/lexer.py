from main.I_lexical.token_types import TokenType
from main.I_lexical.token import Token
from main.exceptions.i_lexical_exception import *


def lexer(program):
    row = 1
    result_token_list = []
    lines = [line + '\n' for line in program.split('\n')]
    for line in lines:
        col = 1
        token_text = ''
        token_type = None
        brackets_depth = 0
        while line:
            for TYPE in TokenType:
                match = TYPE.value.match(line)
                if match:
                    # if the token before ' is white space or there is no token before ',
                    # it is a CharacterVectorTerminationError,
                    # otherwise it would be considered as a normal transpose character at the lexical analysis stage.
                    if TYPE == TokenType.TRA:
                        if TokenType.WHITESPACE.value.sub('', token_text) == '':
                            raise CharacterVectorTerminationError(row, col)
                    # preprocess: replace comma for space in some array construction cases
                    if brackets_depth > 0 and TYPE == TokenType.ADD and token_type == TokenType.WHITESPACE:
                        result_token_list.append(Token(t_type=TokenType.EO_STMT, t_text=',', row=row, col=col - 1))
                    if brackets_depth > 0 and TYPE == TokenType.WHITESPACE and token_type == TokenType.ADD \
                            and result_token_list[-2].get_type() == TokenType.EO_STMT:  # space - space就要删掉减号前的逗号
                        result_token_list.pop(-2)
                    if TYPE == TokenType.L_BRACKET:
                        brackets_depth += 1
                    if TYPE == TokenType.R_BRACKET:
                        brackets_depth -= 1

                    token_text = match.group()
                    token_type = TYPE
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
