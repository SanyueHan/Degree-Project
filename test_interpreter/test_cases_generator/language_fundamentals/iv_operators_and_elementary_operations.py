import random

REPETITION = 20
DIRECTORY = '../../test_cases/language_fundamentals/iv_operators_and_elementary_operations/'


def random_double():
    choice = random.choice(['fp', 'sc', 'inf'])
    if choice == 'fp':
        return (random.random()-0.5) * 100000000
    if choice == 'sc':
        return f"{(random.random()-0.5) * 10000}e{random.choice(['+', '-', ''])+str(random.randint(0, 100))}"
    return choice


def create_binary_operator_cases(operator):
    return ''.join([f"{random_double()} {operator} {random_double()}\n" for _ in range(REPETITION)])


def create_prefix_operator_cases(operator):
    return ''.join([f"{operator}{random_double()}\n" for _ in range(REPETITION)])


def create_postfix_operator_cases(operator):
    return ''.join([f"{random_double()}{operator}\n" for _ in range(REPETITION)])


if __name__ == "__main__":
    with open(DIRECTORY+"test_1_arithmetic_operations.m", 'w') as file_1:
        # Basic Arithmetics
        file_1.write("\n% Addition\n")
        file_1.write(create_binary_operator_cases('+'))
        file_1.write("\n% Subtraction\n")
        file_1.write(create_binary_operator_cases('-'))
        file_1.write("\n% Multiplication\n")
        file_1.write(create_binary_operator_cases('.*'))
        file_1.write(create_binary_operator_cases('*'))
        file_1.write("\n% Division\n")
        file_1.write(create_binary_operator_cases('./'))
        file_1.write(create_binary_operator_cases('.\\'))
        file_1.write(create_binary_operator_cases('/'))
        file_1.write(create_binary_operator_cases('\\'))
        file_1.write("\n% Powers\n")
        file_1.write("\n% Transpose\n")
        file_1.write(create_postfix_operator_cases('.\''))
        file_1.write(create_postfix_operator_cases('\''))
        file_1.write("\n% Array Sign\n")
        file_1.write(create_prefix_operator_cases('-'))
        file_1.write(create_prefix_operator_cases('+'))
    with open(DIRECTORY+"test_2_relational_operations.m", 'w') as file_2:
        file_2.write(create_binary_operator_cases('=='))
        file_2.write(create_binary_operator_cases('>='))
        file_2.write(create_binary_operator_cases('>'))
        file_2.write(create_binary_operator_cases('<='))
        file_2.write(create_binary_operator_cases('<'))
        file_2.write(create_binary_operator_cases('~='))
    with open(DIRECTORY+"test_3_logical_operations.m", 'w') as file_3:
        file_3.write(create_binary_operator_cases('&&'))
        file_3.write(create_binary_operator_cases('||'))
        file_3.write(create_prefix_operator_cases('~'))
    with open(DIRECTORY+"test_4_set_operations.m", 'w') as file_4:
        pass
    with open(DIRECTORY+"test_5_bitwise_operations.m", 'w') as file_5:
        pass
