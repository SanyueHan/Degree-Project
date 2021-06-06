from main.exceptions.interpret_exception import *


class UnaryOperatorError(SemanticException):
    message = {
        'win32': f"Unary operator placeholder is not supported for operand of type 'string'.",
        'darwin': f"Unary operator placeholder is not supported for operand of type 'string'.\n"
    }


class OperatorError(SemanticException):
    message = {
        'win32': f"Operator placeholder is not supported for operands of type 'string'.",
        'darwin': f"Operator placeholder is not supported for operands of type 'string'.\n"
    }


class ComparisonError(SemanticException):
    message = {
        'win32': f"Error using placeholder1\nComparison between placeholder2 and placeholder3 is not supported.",
        'darwin': f"Error using placeholder1\nComparison between placeholder2 and placeholder3 is not supported.\n"
    }

    def __init__(self, placeholder1="", placeholder2="", placeholder3="", line=0):
        self.placeholder1 = placeholder1
        self.placeholder2 = placeholder2
        self.placeholder3 = placeholder3
        self.line = line

    def __str__(self):
        return self.message[sys.platform]\
            .replace("placeholder1", self.placeholder1) \
            .replace("placeholder2", self.placeholder2) \
            .replace("placeholder3", self.placeholder3)


class DivisionError(SemanticException):
    message = {
        'win32': f"Error using placeholder\nArguments must be numeric, char, or logical.",
        'darwin': f"Error using placeholder\nArguments must be numeric, char, or logical.\n"
    }


class RecognitionError(SemanticException):
    message = {
        'win32': f"Unrecognized function or variable placeholder.",
        'darwin': f"Unrecognized function or variable placeholder.\n"
    }


class ConcatenationError(SemanticException):
    message = {
        'win32': f"Error using placeholder\nDimensions of arrays being concatenated are not consistent.",
        'darwin': f"Error using placeholder\nDimensions of arrays being concatenated are not consistent.\n"
    }


# windows平台此处message过长，出现180列换行问题，需要修改
class IncorrectDimensionError(SemanticException):
    message = {
        'win32': "Error using *\nIncorrect dimensions for matrix multiplication. Check that the number of "
                 "columns in the first matrix matches the number of rows in the second matrix. To "
                 "perform elementwise\nmultiplication, use '.*'.",
        'darwin': "Error using *\nIncorrect dimensions for matrix multiplication. Check that the number of\n"
                  "columns in the first matrix matches the number of rows in the second matrix. To\n"
                  "perform elementwise multiplication, use '.*'.\n",
    }

    def __init__(self, line=0):
        self.line = line

    def __str__(self):
        return self.message[sys.platform]
