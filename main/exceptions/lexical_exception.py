from main.exceptions.interpret_exception import InterpretException


class InvalidCharacterError(InterpretException):
    message = "Invalid text character. Check for unsupported symbol, invisible character, or\n" \
              "pasting of non-ASCII characters."

    def __init__(self, line, column):
        self.line = line
        self.column = column

    def __str__(self):
        return f"Line: {self.line} Column: {self.column}\n" + self.message
