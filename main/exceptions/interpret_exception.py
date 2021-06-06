import sys


class InterpretException(Exception):
    message = {}

    def __init__(self, line=0, column=0):
        self.line = line
        self.column = column

    def __str__(self):
        return f"Line: {self.line} Column: {self.column}\n" + self.message[sys.platform]


class LexicalException(InterpretException):
    pass


class SyntacticException(InterpretException):
    pass


class SemanticException(InterpretException):
    def __init__(self, placeholder="", line=0):
        self.placeholder = placeholder
        self.line = line

    def __str__(self):
        return self.message[sys.platform].replace("placeholder", self.placeholder)
