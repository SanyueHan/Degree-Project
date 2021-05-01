from main.exceptions.interpret_exception import InterpretException
#词法异常

class InvalidCharacterError(InterpretException):
    message = "Invalid text character. Check for unsupported symbol, invisible character, or\n" \
              "pasting of non-ASCII characters."


class StringTerminationError(InterpretException):
    message = "String is not terminated properly."


class CharacterVectorTerminationError(InterpretException):
    message = "Character vector is not terminated properly."
