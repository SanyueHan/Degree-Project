from test_interpreter.test_cases_generator.language_fundamentals.utils.random_components import *


class RandomExpressionGenerator(RandomComponentGenerator):
    def __init__(self, exp=0):
        self.max_recur_depth_exp = exp
        self.variables = []

    @staticmethod
    def random_colon_expression():
        length = random.randint(3, 7)
        start = random.randint(0, 5)
        return f"{start}:{start + length}"

    def random_binary_expression(self, operator, current_recur_depth=0):
        if current_recur_depth < self.max_recur_depth_exp:
            a = self.random_expression(current_recur_depth=current_recur_depth+1)
            b = self.random_expression(current_recur_depth=current_recur_depth+1)
        else:
            a = self.random_terminator()
            b = self.random_terminator()
        return f"{a} {operator} {b}"

    def random_prefix_expression(self, operator, current_recur_depth=0):
        if current_recur_depth < self.max_recur_depth_exp:
            a = self.random_expression(current_recur_depth+1)
        else:
            a = self.random_terminator()
        return f"{operator}{a}"

    def random_postfix_expression(self, operator, current_recur_depth=0):
        if current_recur_depth < self.max_recur_depth_exp:
            a = self.random_expression(current_recur_depth+1)
        else:
            a = self.random_terminator()
        return f"{a}{operator}"

    def random_expression(self, current_recur_depth=0):
        factor = random.random()
        if factor < 0.36:
            return self.random_binary_expression(
                random.choice(['+', '-', '.*', '*', './', '.\\', '/', '\\', '.^', '^',
                               '==', '>=', '>', '<=', '<', '~=',
                               '&&', '||']),
                current_recur_depth=current_recur_depth
            )
        elif factor < 0.42:
            return self.random_prefix_expression(
                random.choice(['+', '-', '~']),
                current_recur_depth=current_recur_depth
            )
        else:
            return self.random_terminator()

    def random_terminator(self):
        if self.variables:
            return random.choice([self.random_variable, self.random_double])()
        else:
            return self.random_double()

    def random_variable(self):
        """
        this method will never be called in this class,
        however, the RandomStatementGenerator which inherited from this class need to have random_terminator defined,
        so that it can use local variables added by assignment statements without overwrite random expression
        """
        return random.choice(self.variables)
