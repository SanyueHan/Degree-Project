from test_interpreter.test_cases_generator.language_fundamentals.utils.random_expressions import *


def random_statement_list(indentation=0, number=0):
    if number == 0:
        number = random.randint(3, 7)
    return [random_statement(indentation=indentation) for _ in range(number)]


def random_statement(indentation=0):
    factor = random.random()
    if factor < 0.45:
        statement = random_assignment_statement
    elif factor < 0.9:
        statement = random_expression_statement
    elif factor < 0.95:
        statement = random_selection_statement
    else:
        statement = random_iteration_statement
    return statement(indentation=indentation)


def random_assignment_statement(indentation=0):
    return " " * indentation + f"{random_identifier()} = {random_expression()}\n"


def random_expression_statement(indentation=0):
    return " " * indentation + f"{random_expression()}\n"


def random_if_else_statement(indentation=0):
    statements = [
        " " * indentation + f"if {random_expression()}\n",
        *random_statement_list(indentation=indentation + 4),
    ]
    while random.random() < 0.6:
        statements.extend([
            " " * indentation + f"elseif {random_expression()}\n",
            *random_statement_list(indentation=indentation + 4),
        ])
    if random.random() < 0.6:
        statements.extend([
            " " * indentation + f"else\n",
            *random_statement_list(indentation=indentation + 4),
        ])
    statements.append(" " * indentation + "end\n")
    return ''.join(statements)


def random_switch_case_statement(indentation=0):
    case_var = random_identifier()
    case_list = [i for i in range(random.randint(0, 5))]
    random.shuffle(case_list)
    statements = [
        " " * indentation + f"{case_var} = {random.randint(0, 5)}\n",
        " " * indentation + f"switch {case_var}\n"
    ]
    while case_list:
        statements.extend([
            " " * indentation + f"case {case_list.pop()}\n",
            *random_statement_list(indentation=indentation + 4, number=random.randint(3, 5)),
        ])
    if random.random() < 0.5:
        statements.extend([
            " " * indentation + f"otherwise\n",
            *random_statement_list(indentation=indentation + 4, number=random.randint(3, 5)),
        ])
    statements.append(" " * indentation + "end\n")
    return ''.join(statements)


def random_for_statement(indentation=0):
    loop_var = random_identifier()
    return ''.join([
        " " * indentation + f"for {loop_var} = {random_colon_expression()}\n",
        *random_statement_list(indentation=indentation + 4),
        " " * indentation + "end\n"
    ])


def random_while_statement(indentation=0):
    loop_var = random_identifier()
    return ''.join([
        " " * indentation + f"{loop_var} = {random.randint(0, 10)}\n",
        " " * indentation + f"while {loop_var}\n",
        *random_statement_list(indentation=indentation + 4),
        " " * (indentation + 4) + f"{loop_var} = {loop_var} - 1\n",
        " " * indentation + "end\n"
    ])


def random_selection_statement(indentation=0):
    statement = random.choice([random_if_else_statement, random_switch_case_statement])
    return statement(indentation=indentation)


def random_iteration_statement(indentation=0):
    statement = random.choice([random_for_statement, random_while_statement])
    return statement(indentation=indentation)
