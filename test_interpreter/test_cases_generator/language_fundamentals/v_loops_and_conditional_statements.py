import random

REPETITION_5 = 3
FIRST_CHAR = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
OTHER_CHAR = FIRST_CHAR + "0123456789"


def random_identifier():
    return random.choice(FIRST_CHAR) + ''.join(random.choice(OTHER_CHAR) for _ in range(random.randint(1, 9)))


def random_integer():
    return random.randint(-10, 10)


def random_relational_expression():
    return str(random_integer()) + random.choice(['>=', '>', '<=', '<', '==', '~=']) + str(random_integer())


def if_else_samples():
    pass


def switch_case_samples():
    pass


def for_samples():
    iter_var = random_identifier()
    return '\n'.join([
        f"for {iter_var}={random.randint(-10, 0)}:{random.randint(0, 10)}",
        f"    {iter_var}",
        f"end\n"
    ])


def while_samples():
    pass


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
