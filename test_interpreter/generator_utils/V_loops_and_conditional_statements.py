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
