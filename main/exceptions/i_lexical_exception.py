from main.exceptions.interpret_exception import LexicalException


class AnnotationBlockTerminationError(LexicalException):
    message = {
        'darwin': "Unterminated %{ block. Use %} to terminate.",
        'win32': "Unterminated %{ block. Use %} to terminate."
    }


class CharacterVectorTerminationError(LexicalException):
    message = {
        'darwin': "Character vector is not terminated properly.",
        'win32': "Character vector is not terminated properly."
    }


class InvalidCharacterError(LexicalException):
    message = {
        'darwin': "Invalid text character. Check for unsupported symbol, invisible character, or\n"
                  "pasting of non-ASCII characters.",
        'win32': "Invalid text character. Check for unsupported symbol, invisible character, or pasting of non-ASCII "
                 "characters."
    }


class StringTerminationError(LexicalException):
    message = {
        'darwin': "String is not terminated properly.",
        'win32': "String is not terminated properly."
    }



