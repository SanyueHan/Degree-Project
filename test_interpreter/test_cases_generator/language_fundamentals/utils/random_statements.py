from test_interpreter.test_cases_generator.language_fundamentals.utils.random_expressions import *


class RandomStatementGenerator(RandomExpressionGenerator):
    def __init__(self, exp=0, stmt=0):
        super().__init__(exp)
        self.max_recur_depth_stmt = stmt

    def random_statement_list(self, indentation=0, number=0):
        if number == 0:
            number = random.randint(3, 5)
        return [self.random_statement(indentation=indentation) for _ in range(number)]

    def random_statement(self, indentation=0):
        terminators = [self.random_assignment_statement,
                       self.random_expression_statement]
        reproducers = [self.random_selection_statement,
                       self.random_iteration_statement]
        if indentation < self.max_recur_depth_stmt * 4:
            factor = random.random()
            if factor < 0.9:
                return random.choice(terminators)(indentation=indentation)
            else:
                return random.choice(reproducers)(indentation=indentation)
        else:
            return random.choice(terminators)(indentation=indentation)

    def random_assignment_statement(self, indentation=0):
        identifier = self.random_identifier()
        statement = " " * indentation + f"{identifier} = {self.random_expression()}\n"
        if indentation == 0:
            # if this statement is ensured to be executed, then add it to assigned variables
            self.variables.append(identifier)
        return statement

    def random_expression_statement(self, indentation=0):
        return " " * indentation + f"{self.random_expression()}\n"

    def random_selection_statement(self, indentation=0):
        statement = random.choice([self.random_if_else_statement, self.random_switch_case_statement])
        return statement(indentation=indentation)

    def random_iteration_statement(self, indentation=0):
        statement = random.choice([self.random_for_statement, self.random_while_statement])
        return statement(indentation=indentation)

    def random_for_statement(self, indentation=0):
        loop_var = self.random_identifier()
        return ''.join([
            " " * indentation + f"for {loop_var} = {self.random_colon_expression()}\n",
            *self.random_statement_list(indentation=indentation + 4),
            " " * indentation + "end\n"
        ])

    def random_while_statement(self, indentation=0):
        loop_var = self.random_identifier()
        return ''.join([
            " " * indentation + f"{loop_var} = {random.randint(0, 5)}\n",
            " " * indentation + f"while {loop_var}\n",
            *self.random_statement_list(indentation=indentation + 4),
            " " * (indentation + 4) + f"{loop_var} = {loop_var} - 1\n",
            " " * indentation + "end\n"
        ])

    def random_if_else_statement(self, indentation=0):
        statements = [
            " " * indentation + f"if {self.random_expression()}\n",
            *self.random_statement_list(indentation=indentation + 4),
        ]
        while random.random() < 0.4:
            statements.extend([
                " " * indentation + f"elseif {self.random_expression()}\n",
                *self.random_statement_list(indentation=indentation + 4),
            ])
        if random.random() < 0.6:
            statements.extend([
                " " * indentation + f"else\n",
                *self.random_statement_list(indentation=indentation + 4),
            ])
        statements.append(" " * indentation + "end\n")
        return ''.join(statements)

    def random_switch_case_statement(self, indentation=0):
        case_var = self.random_identifier()
        case_list = random.sample([i for i in range(5)], random.randint(2, 3))
        statements = [
            " " * indentation + f"{case_var} = {random.randint(0, 5)}\n",
            " " * indentation + f"switch {case_var}\n"
        ]
        while case_list:
            statements.extend([
                " " * (indentation + 4) + f"case {case_list.pop()}\n",
                *self.random_statement_list(indentation=indentation + 8),
            ])
        if random.random() < 0.5:
            statements.extend([
                " " * (indentation + 4) + f"otherwise\n",
                *self.random_statement_list(indentation=indentation + 8),
            ])
        statements.append(" " * indentation + "end\n")
        return ''.join(statements)
