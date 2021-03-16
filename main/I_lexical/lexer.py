from main.I_lexical.token_types import TokenType
from main.I_lexical.token import Token


def lexer(program):
    row = 0
    result_token_list = []
    lines = [line + '\n' for line in program.split('\n') if line]
    for line in lines:
        row += 1
        col = 0
        while line:
            for TYPE in TokenType:
                match = TYPE.value.match(line)
                if match:
                    text = match.group()
                    line = line[len(text):]
                    if TYPE != TokenType.WHITESPACE and TYPE != TokenType.ANNOTATION:
                        result_token_list.append(Token(t_type=TYPE, t_text=text, row=row, col=col))
                    col += len(text)
                    break
            else:
                # todo: raise lexeme unrecognized error
                return None
    return result_token_list


if __name__ == "__main__":
    with open("../../test_cases/test_exp_ass.m", "r") as file:
        code = file.read()
    token_list = lexer(code)
    for t in token_list:
        print(t)
