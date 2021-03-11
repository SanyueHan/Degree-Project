from I_lexical.token_types import TokenType
from I_lexical.token import Token


class Lexical:
    @staticmethod
    def statement_analyzer(statement, row=1, col=0):
        """
        :param row: row of the statement in source code
        :param col: starting col of this statement (several statements could be written in one row separated by ';')
        :param statement: one statement to execute
        :return: a token list
        """
        result_token_list = []
        while statement:
            match = None
            for TYPE in TokenType:
                match = TYPE.value.match(statement)
                if match:
                    text = match.group()
                    statement = statement[len(text):]
                    if TYPE != TokenType.WHITESPACE and TYPE != TokenType.ANNOTATION:
                        result_token_list.append(Token(t_type=TYPE, t_text=text, row=row, col=col))
                    col += len(text)
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
        row = 0
        result_token_lists = []
        for line in program.split('\n'):
            row += 1
            col = 0
            while line.count(';') > 1:
                i = line.index(';')
                col += i + 1
                result_token_lists.append(Lexical.statement_analyzer(line[:i + 1], row, col))
                line = line[i + 1:]
            result_token_lists.append(Lexical.statement_analyzer(line, row, col))
        return result_token_lists


if __name__ == "__main__":
    statement1 = "5*6 + 10/2"
    token_list = Lexical.statement_analyzer(statement1)
    for token in token_list:
        print(token)
