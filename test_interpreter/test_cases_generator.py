from test_interpreter.utils.IV_operators_and_elementary_operations import binary_operator_samples, \
    prefix_operator_samples, postfix_operator_samples
from test_interpreter.utils.V_loops_and_conditional_statements import if_else_samples, switch_case_samples, \
    for_samples, while_samples


DIRECTORY = "test_cases/regular_usage_cases/"


def entering_commands(path):
    pass


def matrices_and_arrays(path):
    pass


def data_types(path):
    pass


def operators_and_elementary_operations(path):
    with open(path, "w") as file:
        file.write("%% Binary\n")
        file.write(binary_operator_samples(['+', '-', '*', '/', '\\', '.*', './', '.\\',
                                            '>=', '>', '<=', '<', '==', '~=',
                                            '&', '&&', '|', '||']))
        file.write("\n\n")

        file.write("%% Unary\n")
        file.write("% Prefix\n")
        file.write(prefix_operator_samples(['+', '-', '~']))
        file.write("\n")

        file.write("% PostFix\n")
        file.write(postfix_operator_samples([]))
        file.write("\n")


def loops_and_conditional_statements(path):
    with open(path, "w") as file:
        file.write("%% Selection Statements\n")
        file.write("% if-else\n")
        file.write(if_else_samples())
        file.write("% switch case\n")
        file.write(switch_case_samples())
        file.write("\n")

        file.write("%% Iteration Statements\n")
        file.write("% for\n")
        file.write(for_samples())
        file.write("% while")
        file.write(while_samples())


if __name__ == "__main__":
    #entering_commands(DIRECTORY + "I_entering_commands.m")
    #matrices_and_arrays(DIRECTORY + "II_matrices_and_arrays.m")
    #data_types(DIRECTORY + "III_data_types.m")
    operators_and_elementary_operations(DIRECTORY + "IV_operators_and_elementary_operations.m")
    #loops_and_conditional_statements(DIRECTORY + "V_loops_and_conditional_statements.m")
