import unittest
from test_interpreter.utils import package_test_class


PATH1 = "test_interpreter/test_cases/error_handling/i_lexical_error/"


class AnnotationBlockTerminationError(unittest.TestCase):
    directory = PATH1 + "annotation_block_termination_error/"


class CharacterVectorTerminationError(unittest.TestCase):
    directory = PATH1 + "character_vector_termination_error/"


class InvalidCharacterError(unittest.TestCase):
    directory = PATH1 + "invalid_character_error/"


class StringTerminationError(unittest.TestCase):
    directory = PATH1 + "string_termination_error/"


global_dict = globals().copy()
for obj in global_dict.values():
    if type(obj).__name__ == 'type':  # obj is a class
        if issubclass(obj, unittest.TestCase):
            package_test_class(obj, error=True)
