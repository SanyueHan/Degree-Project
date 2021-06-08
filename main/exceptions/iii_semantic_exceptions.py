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
        'win32': f"Error using placeholder\nComparison between placeholder and placeholder is not supported.",
        'darwin': f"Error using placeholder\nComparison between placeholder and placeholder is not supported.\n"
    }


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


class ConversionError1(SemanticException):
    message = {
        'darwin': "Operands to the logical and (&&) and or (||) operators must be convertible to\n"
                  "logical scalar values.\n",
        'win32': "Operands to the logical and (&&) and or (||) operators must be convertible to\n"
                 "logical scalar values.",
    }
