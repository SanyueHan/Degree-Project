import sys


class InterpretException(Exception):
    message = {}

    def __init__(self, line=0, column=0):
        self.line = line
        self.column = column

    def __str__(self):
        return f"Line: {self.line} Column: {self.column}\n" + self.message[sys.platform]


class InterpretException2(Exception):
    message = {}

    def __init__(self, line=0, filename='', error_statement=''):
        self.line = line
        self.filename = filename
        self.error_statement = error_statement

    def __str__(self):
        return self.message[
                   sys.platform] + f"Error in {self.filename} (line {self.line})\n" + self.error_statement + "\n"
