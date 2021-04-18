import random

NUMBER_RANGE = 100
REPETITION_4 = 10


def random_double():
    return random.randint(-NUMBER_RANGE, NUMBER_RANGE)


def binary_operator_samples(ls):
    return ''.join(
        [f"{random_double()} {operator} {random_double()}\n" for operator in ls for _ in range(REPETITION_4)]
    )


def prefix_operator_samples(ls):
    return ''.join([f"{operator}{random_double()}\n" for operator in ls for _ in range(REPETITION_4)])


def postfix_operator_samples(ls):
    return ''.join([f"{random_double()}{operator}\n" for operator in ls for _ in range(REPETITION_4)])


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


if __name__ == "__main__":
    PATH = '../../test_cases/language_fundamentals/test_iv_operators_and_elementary_operations.m'
    operators_and_elementary_operations(PATH)
