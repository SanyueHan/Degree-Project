import unittest
from utils import package_test_class


class TestLexicalError(unittest.TestCase):
    directory = "test_cases/error_handling/i_lexical_error/"


class TestSyntacticError(unittest.TestCase):
    directory = "test_cases/error_handling/ii_syntactic_error/"


package_test_class(TestLexicalError, error=True)
package_test_class(TestSyntacticError, error=True)

if __name__ == "__main__":
    unittest.main()
