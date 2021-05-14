from main.exceptions.interpret_exception import InterpretException


class EndMissingError(InterpretException):
    message = "At least one END is missing. The statement beginning here does not have a\nmatching end."


class InvalidExpressionError(InterpretException):
    def __init__(self, line=0, column=0, error_type=1):
        super().__init__(line, column)
        if error_type == 1:
            self.message = "Invalid expression. Check for missing multiplication operator, missing or\n" \
                           "unbalanced delimiters, or other syntax error. To construct matrices, use\n" \
                           "brackets instead of parentheses."
        elif error_type == 2:
            self.message = "Invalid expression. Check for missing or extra characters."
        elif error_type == 3:
            self.message = "Invalid expression. When calling a function or indexing a variable, use\n" \
                           "parentheses. Otherwise, check for mismatched delimiters."


class InvalidOperatorError(InterpretException):
    message = "Invalid use of operator."


class IncompleteStatementError(InterpretException):
    message = "This statement is incomplete."
