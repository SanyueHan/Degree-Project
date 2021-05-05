from test_interpreter.test_cases_generator.language_fundamentals.utils.random_components import *


def random_binary_expression(operator, recursive=False):
    if recursive:
        a = random_expression()
        b = random_expression()
    else:
        a = random_double()
        b = random_double()
    return f"{a} {operator} {b}"


def random_prefix_expression(operator, recursive=False):
    if recursive:
        a = random_expression()
    else:
        a = random_double()
    return f"{operator}{a}"


def random_postfix_expression(operator, recursive=False):
    if recursive:
        a = random_expression()
    else:
        a = random_double()
    return f"{a}{operator}"


def random_expression():
    factor = random.random()
    if factor < 0.32:
        return random_binary_expression(
            random.choice(['+', '-', '.*', '*', './', '.\\', '/', '\\', '==', '>=', '>', '<=', '<', '~=', '&&', '||']),
            recursive=True
        )
    elif factor < 0.38:
        return random_prefix_expression(
            random.choice(['+', '-', '~']),
            recursive=True
        )
    else:
        return random_double()


def random_colon_expression():
    length = random.randint(3, 7)
    start = random.randint(0, 10)
    return f"{start}:{start+length}"
