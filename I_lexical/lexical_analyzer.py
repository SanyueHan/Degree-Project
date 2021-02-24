from I_lexical.token_types import TokenType
from I_lexical.token import Token


class Lexical:
    @staticmethod
    def statement_analyzer(statement):
        """
        :param statement: one statement to execute
        :return: a token list
        """
        result_token_list = []
        while statement:
            match = None
            for TYPE in TokenType:
                if match := TYPE.value.match(statement):
                    text = match.group()
                    statement = statement[len(text):]
                    if TYPE != TokenType.WHITESPACE and TYPE != TokenType.ANNOTATION:
                        result_token_list.append(Token(t_type=TYPE, t_text=text))
                    break
            if not match:
                return None
                # todo: raise error if lexeme unrecognized
        return result_token_list

    @staticmethod
    def program_analyzer(program):
        """
        :param program: full source code in a file
        :return: token lists
        """
        statements = []
        for line in program.split('\n'):
            # split multi ';' lines
            while line.count(';') > 1:
                i = line.index(';')
                statements.append(line[:i + 1])
                line = line[i + 1:]
            statements.append(line)
        return [Lexical.statement_analyzer(s) for s in statements]


if __name__ == "__main__":
    statement1 = "5*6 + 10/2"
    token_list = Lexical.statement_analyzer(statement1)
    for token in token_list:
        print(token)
