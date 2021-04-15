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
