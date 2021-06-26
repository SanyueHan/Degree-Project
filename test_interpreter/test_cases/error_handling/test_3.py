import unittest
from test_interpreter.utils import package_test_class


PATH3 = "test_interpreter/test_cases/error_handling/iii_semantic_error/"


class ArrayIndexError(unittest.TestCase):
    directory = PATH3 + "array_index_error/"


class ComparisonError(unittest.TestCase):
    directory = PATH3 + "comparison_error/"


class ConcatenationError(unittest.TestCase):
    directory = PATH3 + "concatenation_error/"


class ConversionError1(unittest.TestCase):
    directory = PATH3 + "conversion_error_1/"


class ConversionError2(unittest.TestCase):
    directory = PATH3 + "conversion_error_2/"


class ConversionError3(unittest.TestCase):
    directory = PATH3 + "conversion_error_3/"


class DivisionError(unittest.TestCase):
    directory = PATH3 + "division_error/"


class IncompatibleSizeError(unittest.TestCase):
    directory = PATH3 + "incompatible_size_error/"


class IncorrectDimensionError(unittest.TestCase):
    directory = PATH3 + "incorrect_dimension_error/"


class OperatorError(unittest.TestCase):
    directory = PATH3 + "operator_error/"


class RecognitionError(unittest.TestCase):
    directory = PATH3 + "recognition_error/"


class UnaryOperatorError(unittest.TestCase):
    directory = PATH3 + "unary_operator_error/"


global_dict = globals().copy()
for obj in global_dict.values():
    if type(obj).__name__ == 'type':  # obj is a class
        if issubclass(obj, unittest.TestCase):
            package_test_class(obj, error=True)
