from II_syntactic.node_types import ASTNodeType


class Interpreter:
    def __init__(self):
        self.fun_map = {
            ASTNodeType.PROGRAM: self.interpret_program,
            ASTNodeType.EXP_STMT: self.interpret_expression_statement,
            ASTNodeType.ASS_STMT: self.interpret_assignment_statement,
            ASTNodeType.DCL_STMT: self.interpret_declaration_statement,
            ASTNodeType.ADD_EXP: self.evaluate_additive_expression,
            ASTNodeType.MUL_EXP: self.evaluate_multiplicative_expression,
            ASTNodeType.PRI_EXP: self.evaluate_primary_expression,
            ASTNodeType.INT_LIT: self.evaluate_integer_literal,
            ASTNodeType.ID: self.evaluate_identifier,
        }
        self.variables = {}

    def interpret_program(self, root):
        for child in root.get_children():
            self.interpret_statement(child)

    def interpret_statement(self, node):
        """
        :param node: ASTNode
        :return:
        """
        result = self.fun_map[node.get_type()](node)
        # if statement does not ended with a semicolon, the result is printed
        if not node.get_stmt():
            print(f"\n{result[0]} =\n\n     {result[1]}\n")

    def interpret_expression_statement(self, node):
        pass

    def interpret_assignment_statement(self, node):
        var_name = node.get_text()
        child = node.get_children()[0]
        if var_name not in self.variables:
            # to adapt the dynamic type feature in interpreted language,
            # assignment could have the same form as declaration
            # because the type specifiers like 'int'/'double' are omitted.
            # which means that assigning to an nonexistent variable is allowed since it is declaration
            pass
        self.variables[var_name] = self.fun_map[child.get_type()](child)[1]

        return var_name, self.variables[var_name]

    def interpret_declaration_statement(self, node):
        var_name = node.get_text()
        child = node.get_children()[0]
        if var_name in self.variables:
            # todo: throw repeating declaration exception
            pass
        self.variables[var_name] = self.fun_map[child.get_type()](child)[1]
        return var_name, self.variables[var_name]

    def evaluate_additive_expression(self, node):
        children = node.get_children()
        child0 = children[0]
        child1 = children[1]
        if node.get_text() == "+":
            value = self.fun_map[child0.get_type()](child0)[1] + self.fun_map[child1.get_type()](child1)[1]
        else:
            value = self.fun_map[child0.get_type()](child0)[1] - self.fun_map[child1.get_type()](child1)[1]
        return "ans", value

    def evaluate_multiplicative_expression(self, node):
        children = node.get_children()
        child0 = children[0]
        child1 = children[1]
        if node.get_text() == "*":
            value = self.fun_map[child0.get_type()](child0)[1] * self.fun_map[child1.get_type()](child1)[1]
        else:
            value = self.fun_map[child0.get_type()](child0)[1] / self.fun_map[child1.get_type()](child1)[1]
        return "ans", value

    def evaluate_primary_expression(self, node):
        # will not be used since in AST it is optimised to skip single-child node
        pass

    def evaluate_identifier(self, node):
        var_name = node.get_text()
        if var_name in self.variables:
            return var_name, self.variables[var_name]
        else:
            # todo: raise unknown exception variable exception
            pass

    @staticmethod
    def evaluate_integer_literal(node):
        return "ans", int(node.get_text())

    def get_variables(self):
        return self.variables
