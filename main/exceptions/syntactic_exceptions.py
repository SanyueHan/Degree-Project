from main.exceptions.interpret_exception import InterpretException


class IncompleteStatementError(InterpretException):
    message = "At least one END is missing. The statement beginning here does not have a\nmatching end."
