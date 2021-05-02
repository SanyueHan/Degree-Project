import unittest
from utils import package_test_class


class TestEnteringCommands(unittest.TestCase):
    directory = "test_cases/language_fundamentals/i_entering_commands/"


class TestMatricesAndArrays(unittest.TestCase):
    directory = "test_cases/language_fundamentals/ii_matrices_and_arrays/"


class TestDataTypes(unittest.TestCase):
    directory = "test_cases/language_fundamentals/iii_data_types/"


class TestOperatorAndElementaryOperations(unittest.TestCase):
    directory = "test_cases/language_fundamentals/iv_operators_and_elementary_operations/"


class TestLoopsAndConditionalStatements(unittest.TestCase):
    directory = "test_cases/language_fundamentals/v_loops_and_conditional_statements/"


package_test_class(TestMatricesAndArrays)
package_test_class(TestOperatorAndElementaryOperations)
package_test_class(TestLoopsAndConditionalStatements)


if __name__ == '__main__':
    unittest.main()
