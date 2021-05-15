from main.exceptions.interpret_exception import InterpretException


class InvalidCharacterError(InterpretException):
    message = {
        'darwin': "Invalid text character. Check for unsupported symbol, invisible character, or\n"
                  "pasting of non-ASCII characters.",
        'win32': "Invalid text character. Check for unsupported symbol, invisible character, or pasting of non-ASCII characters."
    }


class StringTerminationError(InterpretException):
    message = {
        'darwin': "String is not terminated properly.",
        'win32': "String is not terminated properly."

    }


class CharacterVectorTerminationError(InterpretException):
    message = {
        'darwin': "Character vector is not terminated properly.",
        'win32': "Character vector is not terminated properly."
    }
