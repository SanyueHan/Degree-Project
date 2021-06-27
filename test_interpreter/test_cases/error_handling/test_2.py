import unittest
from test_interpreter.utils import package_test_class


PATH2 = "test_interpreter/test_cases/error_handling/ii_syntactic_error/"


class EndMissingError(unittest.TestCase):
    directory = PATH2 + "end_missing_error/"


class IncompleteStatementError(unittest.TestCase):
    directory = PATH2 + "incomplete_statement_error/"


class InvalidExpressionError1(unittest.TestCase):
    directory = PATH2 + "invalid_expression_error_1/"


class InvalidExpressionError2(unittest.TestCase):
    directory = PATH2 + "invalid_expression_error_2/"


class InvalidExpressionError3(unittest.TestCase):
    directory = PATH2 + "invalid_expression_error_3/"


class InvalidOperatorError(unittest.TestCase):
    directory = PATH2 + "invalid_operator_error/"


global_dict = globals().copy()
for obj in global_dict.values():
    if type(obj).__name__ == 'type':  # obj is a class
        if issubclass(obj, unittest.TestCase):
            package_test_class(obj, error=True)
