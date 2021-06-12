import unittest
from utils import package_test_class


class CharacterVectorTerminationError(unittest.TestCase):
    directory = "test_cases/error_handling/i_lexical_error/character_vector_termination_error/"


class InvalidCharacterError(unittest.TestCase):
    directory = "test_cases/error_handling/i_lexical_error/invalid_character_error/"


class StringTerminationError(unittest.TestCase):
    directory = "test_cases/error_handling/i_lexical_error/string_termination_error/"


class EndMissingError(unittest.TestCase):
    directory = "test_cases/error_handling/ii_syntactic_error/end_missing_error/"


class IncompleteStatementError(unittest.TestCase):
    directory = "test_cases/error_handling/ii_syntactic_error/incomplete_statement_error/"


class InvalidExpressionError(unittest.TestCase):
    directory = "test_cases/error_handling/ii_syntactic_error/invalid_expression_error/"


class ArrayIndexError(unittest.TestCase):
    directory = "test_cases/error_handling/iii_semantic_error/array_index_error/"


class ComparisonError(unittest.TestCase):
    directory = "test_cases/error_handling/iii_semantic_error/comparison_error/"


class ConcatenationError(unittest.TestCase):
    directory = "test_cases/error_handling/iii_semantic_error/concatenation_error/"


class ConversionError1(unittest.TestCase):
    directory = "test_cases/error_handling/iii_semantic_error/conversion_error_1/"


class ConversionError2(unittest.TestCase):
    directory = "test_cases/error_handling/iii_semantic_error/conversion_error_2/"


class ConversionError3(unittest.TestCase):
    directory = "test_cases/error_handling/iii_semantic_error/conversion_error_3/"


class DivisionError(unittest.TestCase):
    directory = "test_cases/error_handling/iii_semantic_error/division_error/"


class IncorrectDimensionError(unittest.TestCase):
    directory = "test_cases/error_handling/iii_semantic_error/incorrect_dimension_error/"


class IncompatibleSizeError(unittest.TestCase):
    directory = "test_cases/error_handling/iii_semantic_error/incompatible_size_error/"


class OperatorError(unittest.TestCase):
    directory = "test_cases/error_handling/iii_semantic_error/operator_error/"


class RecognitionError(unittest.TestCase):
    directory = "test_cases/error_handling/iii_semantic_error/recognition_error/"


class UnaryOperatorError(unittest.TestCase):
    directory = "test_cases/error_handling/iii_semantic_error/unary_operator_error/"


global_dict = globals().copy()
for obj in global_dict.values():
    if type(obj).__name__ == 'type':  # obj is a class
        if issubclass(obj, unittest.TestCase):
            package_test_class(obj, error=True)


if __name__ == "__main__":
    unittest.main()
