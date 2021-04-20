from main.exceptions.interpret_exception import InterpretException


class IncompleteStatementError(InterpretException):
    message = "At least one END is missing. The statement beginning here does not have a\nmatching end."


class InvalidExpressionError(InterpretException):
    message = "Invalid expression. Check for missing multiplication operator, missing or\n" \
              "unbalanced delimiters, or other syntax error. To construct matrices, use\n" \
              "brackets instead of parentheses."
