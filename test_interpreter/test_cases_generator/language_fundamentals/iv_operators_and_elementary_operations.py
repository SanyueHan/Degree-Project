"""
https://ww2.mathworks.cn/help/matlab/operators-and-elementary-operations.html
"""


from test_interpreter.test_cases_generator.language_fundamentals.utils.random_expressions import *


REPETITION = 20
DIRECTORY = '../../test_cases/language_fundamentals/iv_operators_and_elementary_operations/'


def batch_binary_operation_statements(operator):
    return ''.join([random_binary_expression(operator)+'\n' for _ in range(REPETITION)])


def batch_prefix_operation_statements(operator):
    return ''.join([random_prefix_expression(operator)+'\n' for _ in range(REPETITION)])


def batch_postfix_operation_statements(operator):
    return ''.join([random_postfix_expression(operator)+'\n' for _ in range(REPETITION)])


if __name__ == "__main__":
    with open(DIRECTORY+"test_1_arithmetic_operations.m", 'w') as file_1:
        # Basic Arithmetics
        file_1.write("\n% Addition\n")
        file_1.write(batch_binary_operation_statements('+'))
        file_1.write("\n% Subtraction\n")
        file_1.write(batch_binary_operation_statements('-'))
        file_1.write("\n% Multiplication\n")
        file_1.write(batch_binary_operation_statements('.*'))
        file_1.write(batch_binary_operation_statements('*'))
        file_1.write("\n% Division\n")
        file_1.write(batch_binary_operation_statements('./'))
        file_1.write(batch_binary_operation_statements('.\\'))
        file_1.write(batch_binary_operation_statements('/'))
        file_1.write(batch_binary_operation_statements('\\'))
        file_1.write("\n% Powers\n")
        file_1.write("\n% Transpose\n")
        file_1.write(batch_postfix_operation_statements('.\''))
        file_1.write(batch_postfix_operation_statements('\''))
        file_1.write("\n% Array Sign\n")
        file_1.write(batch_prefix_operation_statements('-'))
        file_1.write(batch_prefix_operation_statements('+'))
    with open(DIRECTORY+"test_2_relational_operations.m", 'w') as file_2:
        file_2.write(batch_binary_operation_statements('=='))
        file_2.write(batch_binary_operation_statements('>='))
        file_2.write(batch_binary_operation_statements('>'))
        file_2.write(batch_binary_operation_statements('<='))
        file_2.write(batch_binary_operation_statements('<'))
        file_2.write(batch_binary_operation_statements('~='))
    with open(DIRECTORY+"test_3_logical_operations.m", 'w') as file_3:
        file_3.write(batch_binary_operation_statements('&&'))
        file_3.write(batch_binary_operation_statements('||'))
        file_3.write(batch_prefix_operation_statements('~'))
    with open(DIRECTORY+"test_4_set_operations.m", 'w') as file_4:
        pass
    with open(DIRECTORY+"test_5_bitwise_operations.m", 'w') as file_5:
        pass
