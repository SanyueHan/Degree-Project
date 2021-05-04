from main.I_lexical.token_types import TokenType
from main.I_lexical.token import Token
from main.exceptions.lexical_exception import *


def lexer(program):
    row = 1
    result_token_list = []
    lines = [line + '\n' for line in program.split('\n')]
    for line in lines:
        col = 1
        text = ''
        brackets_depth = 0
        last = None
        while line:
            for TYPE in TokenType:
                match = TYPE.value.match(line)
                if match:
                    # if the token before ' is white space or there is no token before ',
                    # it is a CharacterVectorTerminationError,
                    # otherwise it would be considered as a normal transpose character at the lexical analysis stage.
                    if TYPE == TokenType.TRA:
                        if TokenType.WHITESPACE.value.sub('', text) == '':
                            raise CharacterVectorTerminationError(row, col)
                    text = match.group()
                    line = line[len(text):]
                    if TYPE == TokenType.ADD and brackets_depth > 0 and last == TokenType.WHITESPACE:
                        result_token_list.append(Token(t_type=TokenType.EO_STMT, t_text=',', row=row, col=col - 1))
                        result_token_list.append(Token(t_type=TokenType.ADD, t_text=text, row=row, col=col))
                    elif TYPE == TokenType.WHITESPACE and last == TokenType.ADD and brackets_depth > 0 and result_token_list.__getitem__(result_token_list.__len__() - 2).get_type() == TokenType.EO_STMT:  # space - space就要删掉减号前的逗号
                        result_token_list.remove(result_token_list.__getitem__(result_token_list.__len__() - 2))
                    elif TYPE != TokenType.WHITESPACE and TYPE != TokenType.ANNOTATION:
                        result_token_list.append(Token(t_type=TYPE, t_text=text, row=row, col=col))
                    if TYPE == TokenType.L_BRACKET:
                        brackets_depth += 1
                    if TYPE == TokenType.R_BRACKET:
                        brackets_depth -= 1
                    last = TYPE
                    col += len(text)
                    break
            else:   # 抛出异常
                if line[0] in "#$`":
                    raise InvalidCharacterError(row, col)
                elif line[0] == '\"':
                    raise StringTerminationError(row, col)
                else:
                    raise InvalidCharacterError(row, col)
        row += 1
    return result_token_list
