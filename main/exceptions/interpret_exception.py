class InterpretException(Exception):
    message = ""

    def __init__(self, line=0, column=0):
        self.line = line
        self.column = column

    def __str__(self):
        return f"Line: {self.line} Column: {self.column}\n" + self.message
