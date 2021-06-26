import unittest
from test_interpreter.utils import package_test_class


PATH = "test_interpreter/test_cases/language_fundamentals/"


class TestEnteringCommands(unittest.TestCase):
    directory = PATH + "i_entering_commands/"


class TestMatricesAndArrays(unittest.TestCase):
    directory = PATH + "ii_matrices_and_arrays/"


class TestDataTypes(unittest.TestCase):
    directory = PATH + "iii_data_types/"


class TestOperatorAndElementaryOperations(unittest.TestCase):
    directory = PATH + "iv_operators_and_elementary_operations/"


class TestLoopsAndConditionalStatements(unittest.TestCase):
    directory = PATH + "v_loops_and_conditional_statements/"


package_test_class(TestMatricesAndArrays)
package_test_class(TestOperatorAndElementaryOperations)
package_test_class(TestLoopsAndConditionalStatements)


if __name__ == '__main__':
    unittest.main()
