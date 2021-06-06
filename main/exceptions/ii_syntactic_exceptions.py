from main.exceptions.interpret_exception import SyntacticException


class EndMissingError(SyntacticException):
    message = {
        'darwin': "At least one END is missing. The statement beginning here does not have a\nmatching end.",
        'win32': "At least one END is missing. The statement beginning here does not have a matching end."
    }


class InvalidExpressionError1(SyntacticException):
    message = {
        'darwin': "Invalid expression. Check for missing multiplication operator, missing or\n"
                  "unbalanced delimiters, or other syntax error. To construct matrices, use\n"
                  "brackets instead of parentheses.",
        'win32': "Invalid expression. Check for missing multiplication operator, missing or unbalanced delimiters, "
                 "or other syntax error. To construct matrices, use brackets instead of parentheses. "
    }


class InvalidExpressionError2(SyntacticException):
    message = {
        'darwin': "Invalid expression. Check for missing or extra characters.",
        'win32': "Invalid expression. Check for missing or extra characters."
    }


class InvalidExpressionError3(SyntacticException):
    message = {
        'darwin': "Invalid expression. When calling a function or indexing a variable, use\n"
                  "parentheses. Otherwise, check for mismatched delimiters.",
        'win32': "Invalid expression. When calling a function or indexing a variable, use parentheses. "
                 "Otherwise, check for mismatched delimiters."
    }


class InvalidOperatorError(SyntacticException):
    message = {
        'darwin': "Invalid use of operator.",
        'win32': "Invalid use of operator."
    }


class IncompleteStatementError(SyntacticException):
    message = {
        'darwin': "This statement is incomplete.",
        'win32': "This statement is incomplete."
    }
