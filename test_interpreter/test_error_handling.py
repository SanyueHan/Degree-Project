import unittest
from utils import package_test_class


I_LEXICAL_ERROR = "test_cases/error_handling/i_lexical_error/"
II_SYNTACTIC_ERROR = "test_cases/error_handling/ii_syntactic_error/"


class TestLexicalError(unittest.TestCase):
    pass


class TestSyntacticError(unittest.TestCase):
    pass


package_test_class(TestLexicalError, I_LEXICAL_ERROR, error=True)
package_test_class(TestSyntacticError, II_SYNTACTIC_ERROR, error=True)

if __name__ == "__main__":
    unittest.main()
