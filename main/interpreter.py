from main.II_syntactic.node_types import ASTNodeType


class Interpreter:
    def __init__(self):
        self.interpret = {
            ASTNodeType.STMT_LIST: self.interpret_statement_list,
            ASTNodeType.ASS_STMT: self.interpret_assignment_statement,
            ASTNodeType.EXP_STMT: self.interpret_expression_statement,
            ASTNodeType.CLR_STMT: self.interpret_clear_statement,
            ASTNodeType.SEL_STMT: self.interpret_selection_statement,
            ASTNodeType.ITR_STMT: self.interpret_iteration_statement,
            ASTNodeType.JMP_STMT: self.interpret_jump_statement,
        }
        self.evaluate = {
            ASTNodeType.ASS_EXP: self.evaluate_assignment_expression,
            ASTNodeType.LOR_EXP: self.evaluate_logic_or_expression,
            ASTNodeType.LAN_EXP: self.evaluate_logic_and_expression,
            ASTNodeType.EQL_EXP: self.evaluate_equal_expression,
            ASTNodeType.REL_EXP: self.evaluate_relational_expression,
            ASTNodeType.ADD_EXP: self.evaluate_additive_expression,
            ASTNodeType.MUL_EXP: self.evaluate_multiplicative_expression,
            ASTNodeType.UNY_EXP: self.evaluate_unary_expression,
            ASTNodeType.PRI_EXP: self.evaluate_primary_expression,
            ASTNodeType.NUM_LIT: self.evaluate_number_literal,
            ASTNodeType.STR_LIT: self.evaluate_string_literal,
            ASTNodeType.ID: self.evaluate_identifier,
        }
        self.variables = {}

    def interpret_statement_list(self, root):
        for child in root.get_children():
            self.interpret_statement(child)

    def interpret_statement(self, node):
        result = self.interpret[node.get_type()](node)
        # if statement does not ended with a semicolon, the result is printed
        if result:
            var = result[0]
            value = result[1]
            if isinstance(value, float):
                if int(value) == value:
                    print(f"\n{var} =\n\n     {int(value)}\n")
                else:
                    print(f"\n{var} =\n\n     {value:.4f}\n")
            else:
                print(f"\n{var} =\n\n     {value}\n")

    def interpret_assignment_statement(self, node):
        res = self.evaluate_assignment_expression(node.get_child(0))

        return res if node.get_child(1).get_text() != ';' else None

    def interpret_expression_statement(self, node):
        var_name = "ans"
        child = node.get_child(0)
        self.variables[var_name] = self.evaluate[child.get_type()](child)

        return (var_name, self.variables[var_name]) if node.get_child(1).get_text() != ';' else None

    def interpret_clear_statement(self, node):
        variables = [child.get_text() for child in node.get_child(0).get_children()]
        self.del_variables(var_list=variables if variables else None)

    def evaluate_assignment_expression(self, node):
        var_name = node.get_child(0).get_text()
        value = self.evaluate[node.get_child(1).get_type()](node.get_child(1))
        self.variables[var_name] = value
        return var_name, value

    def interpret_selection_statement(self, node):
        for clause in node.get_children():
            if self.interpret_clause(clause):
                break

    def interpret_clause(self, node):
        if node.get_text() == 'else':
            self.interpret_statement_list(node.get_child(0))
        else:
            expression = node.get_child(0)
            if self.evaluate[expression.get_type()](expression):
                self.interpret_statement_list(node.get_child(1))
                return True
            else:
                return False

    def interpret_iteration_statement(self, node):
        pass

    def interpret_jump_statement(self, node):
        pass

    def evaluate_logic_or_expression(self, node):
        child0 = node.get_child(0)
        child1 = node.get_child(1)
        return 1 if self.evaluate[child0.get_type()](child0) or self.evaluate[child1.get_type()](child1) else 0

    def evaluate_logic_and_expression(self, node):
        child0 = node.get_child(0)
        child1 = node.get_child(1)
        return 1 if self.evaluate[child0.get_type()](child0) and self.evaluate[child1.get_type()](child1) else 0

    def evaluate_equal_expression(self, node):
        child0 = node.get_child(0)
        child1 = node.get_child(1)
        if node.get_text() == "==":
            return 1 if self.evaluate[child0.get_type()](child0) == self.evaluate[child1.get_type()](child1) else 0
        else:
            return 1 if self.evaluate[child0.get_type()](child0) != self.evaluate[child1.get_type()](child1) else 0

    def evaluate_relational_expression(self, node):
        child0 = node.get_child(0)
        child1 = node.get_child(1)
        if node.get_text() == ">=":
            return 1 if self.evaluate[child0.get_type()](child0) >= self.evaluate[child1.get_type()](child1) else 0
        elif node.get_text() == ">":
            return 1 if self.evaluate[child0.get_type()](child0) > self.evaluate[child1.get_type()](child1) else 0
        elif node.get_text() == "<=":
            return 1 if self.evaluate[child0.get_type()](child0) <= self.evaluate[child1.get_type()](child1) else 0
        else:
            return 1 if self.evaluate[child0.get_type()](child0) < self.evaluate[child1.get_type()](child1) else 0

    def evaluate_additive_expression(self, node):
        child0 = node.get_child(0)
        child1 = node.get_child(1)
        if node.get_text() == "+":
            return self.evaluate[child0.get_type()](child0) + self.evaluate[child1.get_type()](child1)
        else:
            return self.evaluate[child0.get_type()](child0) - self.evaluate[child1.get_type()](child1)

    def evaluate_multiplicative_expression(self, node):
        child0 = node.get_child(0)
        child1 = node.get_child(1)
        if node.get_text() == "*":
            return self.evaluate[child0.get_type()](child0) * self.evaluate[child1.get_type()](child1)
        else:
            return self.evaluate[child0.get_type()](child0) / self.evaluate[child1.get_type()](child1)

    def evaluate_unary_expression(self, node):
        child = node.get_child()
        if node.get_text() == "+":
            return self.evaluate[child.get_type()](child)
        elif node.get_text() == "-":
            return -self.evaluate[child.get_type()](child)
        else:
            return 0 if self.evaluate[child.get_type()](child) else 1

    def evaluate_primary_expression(self, node):
        # will not be used since in AST it is optimised to skip single-child node
        pass

    @staticmethod
    def evaluate_number_literal(node):
        """
        By default, MATLAB® stores all numeric variables as double-precision floating-point values.
        """
        return float(node.get_text())

    @staticmethod
    def evaluate_string_literal(node):
        return node.get_text()

    def evaluate_identifier(self, node):
        var_name = node.get_text()
        if var_name in self.variables:
            return self.variables[var_name]
        else:
            # todo: raise unknown variable exception
            pass

    def get_variables(self):
        return self.variables

    def del_variables(self, var_list=None):
        if var_list:
            for var in var_list:
                # todo: check exist and raise error
                del self.variables[var]
        else:
            self.variables = {}
