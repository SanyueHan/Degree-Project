import unittest
from utils import package_test_class


I_ENTERING_COMMANDS = "test_cases/language_fundamentals/i_entering_commands/"
II_MATRICES_AND_ARRAYS = "test_cases/language_fundamentals/ii_matrices_and_arrays/"
III_DATA_TYPES = "test_cases/language_fundamentals/iii_data_types/"
IV_OPERATORS_AND_ELEMENTARY_OPERATIONS = "test_cases/language_fundamentals/iv_operators_and_elementary_operations/"
V_LOOPS_AND_CONDITIONAL_STATEMENTS = "test_cases/language_fundamentals/v_loops_and_conditional_statements/"


class TestEnteringCommands(unittest.TestCase):
    pass


class TestMatricesAndArrays(unittest.TestCase):
    pass


class TestDataTypes(unittest.TestCase):
    pass


class TestOperatorAndElementaryOperations(unittest.TestCase):
    pass


class TestLoopsAndConditionalStatements(unittest.TestCase):
    pass


package_test_class(TestMatricesAndArrays, II_MATRICES_AND_ARRAYS)
package_test_class(TestOperatorAndElementaryOperations, IV_OPERATORS_AND_ELEMENTARY_OPERATIONS)
package_test_class(TestLoopsAndConditionalStatements, V_LOOPS_AND_CONDITIONAL_STATEMENTS)


if __name__ == '__main__':
    unittest.main()
