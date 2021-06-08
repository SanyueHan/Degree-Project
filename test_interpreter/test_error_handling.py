import unittest
from utils import package_test_class


class TestLexicalError(unittest.TestCase):
    directory = "test_cases/error_handling/i_lexical_error/"


class TestEndMissingError(unittest.TestCase):
    directory = "test_cases/error_handling/ii_syntactic_error/end_missing_error/"


class TestIncompleteStatementError(unittest.TestCase):
    directory = "test_cases/error_handling/ii_syntactic_error/incomplete_statement_error/"


class TestInvalidExpressionError(unittest.TestCase):
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

"""
package_test_class(TestLexicalError, error=True)
package_test_class(TestEndMissingError, error=True)
package_test_class(TestIncompleteStatementError, error=True)
package_test_class(TestInvalidExpressionError, error=True)
"""
package_test_class(ArrayIndexError, error=True)
package_test_class(ComparisonError, error=True)
package_test_class(ConcatenationError, error=True)
package_test_class(ConversionError1, error=True)
package_test_class(ConversionError2, error=True)
package_test_class(ConversionError3, error=True)
package_test_class(DivisionError, error=True)
package_test_class(IncorrectDimensionError, error=True)
package_test_class(IncompatibleSizeError, error=True)
package_test_class(OperatorError, error=True)
package_test_class(RecognitionError, error=True)
package_test_class(UnaryOperatorError, error=True)


if __name__ == "__main__":
    unittest.main()
