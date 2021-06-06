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


class TestSemanticError(unittest.TestCase):
    directory = "test_cases/error_handling/iii_semantic_error/"


package_test_class(TestLexicalError, error=True)
package_test_class(TestEndMissingError, error=True)
package_test_class(TestIncompleteStatementError, error=True)
package_test_class(TestInvalidExpressionError, error=True)
package_test_class(TestSemanticError, error=True)


if __name__ == "__main__":
    unittest.main()
