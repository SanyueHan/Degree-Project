import unittest
import os
from utils import test_method_builder, python_execute, matlab_execute


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


def package_regular_usage_test_class(class_name, directory):
    for test_case in os.listdir(directory):
        python_result = python_execute(directory + test_case)
        matlab_result = matlab_execute(directory + test_case)
        test_method = test_method_builder(python_result, matlab_result)
        setattr(class_name, test_case, test_method)


package_regular_usage_test_class(TestMatricesAndArrays, II_MATRICES_AND_ARRAYS)
package_regular_usage_test_class(TestOperatorAndElementaryOperations, IV_OPERATORS_AND_ELEMENTARY_OPERATIONS)
package_regular_usage_test_class(TestLoopsAndConditionalStatements, V_LOOPS_AND_CONDITIONAL_STATEMENTS)


if __name__ == '__main__':
    unittest.main()
