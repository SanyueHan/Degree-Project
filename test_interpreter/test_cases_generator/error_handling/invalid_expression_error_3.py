import random


PATH = "test_interpreter/test_cases/error_handling/ii_syntactic_error/invalid_expression_error_3/test_4_bracket_exp.m"


def generate_test_case():
    return '[' + ''.join(random.choice(",; 01") for _ in range(50)) + ']'


if __name__ == "__main__":
    with open(PATH, "w") as file:
        file.write(generate_test_case())
