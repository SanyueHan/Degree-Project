# from main.exceptions.interpret_exception import InterpretException
import sys

class UnaryOperatorForStrError(Exception):
    def __init__(self, line=0,filename=None, error_statement='',unary_operator=None):
        self.line = line
        self.filename=filename
        self.error_statement=error_statement
        self.unary_operator=unary_operator
        self.message={
            'win32': f"Unary operator '{self.unary_operator}' is not supported for operand of type 'string'.\n"
        }

    def __str__(self):
        return self.message[sys.platform]+f"Error in {self.filename} (line {self.line})\n"+self.error_statement

