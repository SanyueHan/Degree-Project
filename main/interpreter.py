from main.II_syntactic.node_types import ASTNodeType
from main.datatype.data.array_data.string import String
from main.datatype.data.array_data.logical import Logical
from main.datatype.data.array_data.numeric_data.float_data.double import Double

BSO_MAP = {
    '|': (Logical, lambda x, y: x or y),
    '&': (Logical, lambda x, y: x and y),
    '==': (Logical, lambda x, y: x == y),
    '~=': (Logical, lambda x, y: x != y),
    '>=': (Logical, lambda x, y: x >= y),
    '>':  (Logical, lambda x, y: x > y),
    '<=': (Logical, lambda x, y: x <= y),
    '<':  (Logical, lambda x, y: x < y),
    '+': (Double, lambda x, y: x + y),
    '-': (Double, lambda x, y: x - y),
    '.*': (Double, lambda x, y: x * y),
    './': (Double, lambda x, y: x / y),
    '.\\': (Double, lambda x, y: y / x),
}

USO_MAP = {
    '+': (Double, lambda x: x),
    '-': (Double, lambda x: -x),
    '~': (Logical, lambda x: not x)
}


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
            ASTNodeType.CLN_EXP: self.evaluate_colon_expression,
            ASTNodeType.BSO_EXP: self.evaluate_binary_scalar_calculation,
            ASTNodeType.MML_EXP: self.evaluate_matrix_multiplication,
            ASTNodeType.MRD_EXP: self.evaluate_matrix_right_division,
            ASTNodeType.MLD_EXP: self.evaluate_matrix_left_division,
            ASTNodeType.USO_EXP: self.evaluate_unary_scalar_calculation,
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
            obj = result[1]
            print(f"\n{var} =\n\n{str(obj)}\n")

    def interpret_assignment_statement(self, node):
        res = self.evaluate_assignment_expression(node.get_child(0))

        return res if node.get_child(1).get_text() != ';' else None

    def interpret_expression_statement(self, node):
        child = node.get_child(0)

        if child.get_type() == ASTNodeType.ID:
            var_name = child.get_text()
        else:
            var_name = "ans"
            self.variables["ans"] = self.evaluate_expression(child)

        return (var_name, self.variables[var_name]) if node.get_child(1).get_text() != ';' else None

    def interpret_clear_statement(self, node):
        variables = [child.get_text() for child in node.get_child(0).get_children()]
        self.del_variables(var_list=variables if variables else None)

    def interpret_selection_statement(self, node):
        for clause in node.get_children():
            if self.interpret_selection_clause(clause):
                break

    def interpret_selection_clause(self, node):
        if node.get_text() == 'else':
            self.interpret_statement_list(node.get_child(0))
        else:
            expression = node.get_child(0)
            if self.evaluate_expression(expression):
                self.interpret_statement_list(node.get_child(1))
                return True
            else:
                return False

    def interpret_iteration_statement(self, node):
        self.interpret_iteration_clause(node.get_child())

    def interpret_iteration_clause(self, node):
        expression = node.get_child(0)
        statement_list = node.get_child(1)
        if node.get_text() == 'while':
            while self.evaluate_expression(expression):
                self.interpret_statement_list(statement_list)
        else:
            var_name = expression.get_child(0).get_text()
            value = self.evaluate_expression(expression.get_child(1))
            for col in value.cols():
                self.variables[var_name] = value.create_same(col, size=(len(col), 1))
                self.interpret_statement_list(statement_list)

    def interpret_jump_statement(self, node):
        pass

    def evaluate_expression(self, node):
        return self.evaluate[node.get_type()](node)

    def evaluate_assignment_expression(self, node):
        var_name = node.get_child(0).get_text()
        value = self.evaluate_expression(node.get_child(1))
        self.variables[var_name] = value
        return var_name, value

    def evaluate_colon_expression(self, node):
        if node.num_children() == 3:
            start = self.evaluate_expression(node.get_child(0))[0]
            step = self.evaluate_expression(node.get_child(1))[0]
            end = self.evaluate_expression(node.get_child(2))[0]
        else:
            start = self.evaluate_expression(node.get_child(0))[0]
            step = 1
            end = self.evaluate_expression(node.get_child(1))[0]

        if step == 0 or start < end and step < 0 or start > end and step > 0:
            return Double([])

        values = []
        while start <= end:
            values.append(start)
            start += step
        return Double(values)

    def evaluate_binary_scalar_calculation(self, node):
        data0 = self.evaluate_expression(node.get_child(0))
        data1 = self.evaluate_expression(node.get_child(1))
        cls, fun = BSO_MAP[node.get_text()]
        if data0.Size == data1.Size:
            return cls([fun(*tup) for tup in zip(data0, data1)], size=data0.Size)
        # todo: auto expand feature and size not fix error.

    def evaluate_unary_scalar_calculation(self, node):
        data = self.evaluate_expression(node.get_child())
        cls, fun = USO_MAP[node.get_text()]
        return cls([fun(v) for v in data], size=data.Size)

    def evaluate_matrix_multiplication(self, node):
        data0 = self.evaluate_expression(node.get_child(0))
        data1 = self.evaluate_expression(node.get_child(1))
        if data0.Size == (1, 1) and data1.Size == (1, 1):
            return Double([data0[0] * data1[0]])
        # todo: matrix multiplication

    def evaluate_matrix_right_division(self, node):
        data0 = self.evaluate_expression(node.get_child(0))
        data1 = self.evaluate_expression(node.get_child(1))
        if data0.Size == (1, 1) and data1.Size == (1, 1):
            return Double([data0[0] / data1[0]])
        # todo: matrix multiplication

    def evaluate_matrix_left_division(self, node):
        data0 = self.evaluate_expression(node.get_child(0))
        data1 = self.evaluate_expression(node.get_child(1))
        if data0.Size == (1, 1) and data1.Size == (1, 1):
            return Double([data1[0] / data0[0]])
        # todo: matrix multiplication

    def evaluate_primary_expression(self, node):
        # will not be used since in AST it is optimised to skip single-child node
        pass

    @staticmethod
    def evaluate_number_literal(node):
        """
        By default, MATLAB® stores all numeric variables as double-precision floating-point values.
        """
        return Double([node.get_text()])

    @staticmethod
    def evaluate_string_literal(node):
        return String([node.get_text()])

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
