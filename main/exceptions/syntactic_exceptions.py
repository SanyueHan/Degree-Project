from main.exceptions.interpret_exception import InterpretException


class EndMissingError(InterpretException):
    message = {
        'darwin': "At least one END is missing. The statement beginning here does not have a\nmatching end."
    }


class InvalidExpressionError1(InterpretException):
    message = {
        'darwin': "Invalid expression. Check for missing multiplication operator, missing or\n"
                  "unbalanced delimiters, or other syntax error. To construct matrices, use\n"
                  "brackets instead of parentheses."
    }


class InvalidExpressionError2(InterpretException):
    message = {
        'darwin': "Invalid expression. Check for missing or extra characters."
    }


class InvalidExpressionError3(InterpretException):
    message = {
        'darwin': "Invalid expression. When calling a function or indexing a variable, use\n"
                  "parentheses. Otherwise, check for mismatched delimiters."
    }


class InvalidOperatorError(InterpretException):
    message = {
        'darwin': "Invalid use of operator."
    }


class IncompleteStatementError(InterpretException):
    message = {
        'darwin': "This statement is incomplete."
    }
