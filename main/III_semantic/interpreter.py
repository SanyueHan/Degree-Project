from main.II_syntactic.node_types import ASTNodeType
from main.data_types.array_data.char import Char
from main.data_types.array_data.string import String
from main.data_types.array_data.logical import Logical
from main.data_types.array_data.numeric_data.decimal_data.double import Double
from main.III_semantic.utils import concatenate


BSO_MAP = {
    '|': (Logical, lambda x, y: x or y),
    '||': (Logical, lambda x, y: x or y),
    '&': (Logical, lambda x, y: x and y),
    '&&': (Logical, lambda x, y: x and y),
    '==': (Logical, lambda x, y: x == y),
    '~=': (Logical, lambda x, y: x != y),
    '>=': (Logical, lambda x, y: x >= y),
    '>':  (Logical, lambda x, y: x > y),
    '<=': (Logical, lambda x, y: x <= y),
    '<':  (Logical, lambda x, y: x < y),
    '+': (Double, lambda x, y: x + y),
    '-': (Double, lambda x, y: x - y),
    '*': (Double, lambda x, y: x * y),
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
            ASTNodeType.BSO_EXP: self.evaluate_binary_scalar_operator_expression,
            ASTNodeType.MML_EXP: self.evaluate_matrix_multiplication_expression,
            ASTNodeType.MRD_EXP: self.evaluate_matrix_right_division_expression,
            ASTNodeType.MLD_EXP: self.evaluate_matrix_left_division_expression,
            ASTNodeType.PRE_EXP: self.evaluate_prefix_expression,
            ASTNodeType.PST_EXP: self.evaluate_postfix_expression,
            ASTNodeType.PRI_EXP: self.evaluate_primary_expression,
            ASTNodeType.ARR_EXP: self.evaluate_array_expression,
            ASTNodeType.IDENTIFIER: self.evaluate_identifier_expression,
            ASTNodeType.NUMBER_LIT: self.evaluate_number_literal,
            ASTNodeType.STRING_LIT: self.evaluate_string_literal,
            ASTNodeType.VECTOR_LIT: self.evaluate_vector_literal,
            ASTNodeType.ARRAY_LIST: self.evaluate_array_list,
            ASTNodeType.INDEX_LIST: self.evaluate_index_list
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
            ass_str = " = " if obj.get_class() == String else " ="
            print(f"\n{var}{ass_str}\n\n{str(obj)}\n")

    def interpret_assignment_statement(self, node):
        res = self.evaluate_assignment_expression(node.get_child(0))

        return res if node.get_child(1).get_text() != ';' else None

    def interpret_expression_statement(self, node):
        child = node.get_child(0)

        if child.get_type() == ASTNodeType.IDENTIFIER:
            name = child.get_text()
        else:
            name = "ans"
            self.variables["ans"] = self.evaluate_expression(child)

        return (name, self.variables[name]) if node.get_child(1).get_text() != ';' else None

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
            name = expression.get_child(0).get_text()
            data = self.evaluate_expression(expression.get_child(1))
            for col in data.cols():
                self.variables[name] = data.get_class()(col, size=(len(col), 1))
                self.interpret_statement_list(statement_list)

    def interpret_jump_statement(self, node):
        pass

    def evaluate_expression(self, node):
        return self.evaluate[node.get_type()](node)

    def evaluate_assignment_expression(self, node):
        name = node.get_child(0).get_text()
        data = self.evaluate_expression(node.get_child(1))
        self.variables[name] = data
        return name, data

    def evaluate_colon_expression(self, node):
        if node.num_children() == 0:
            return ":"

        if node.num_children() == 2:
            start = self.evaluate_expression(node.get_child(0))[0]
            step = 1
            end = self.evaluate_expression(node.get_child(1))[0]
        else:
            start = self.evaluate_expression(node.get_child(0))[0]
            step = self.evaluate_expression(node.get_child(1))[0]
            end = self.evaluate_expression(node.get_child(2))[0]

        if step == 0 or start < end and step < 0 or start > end and step > 0:
            return Double([])

        values = []
        while start <= end:
            values.append(start)
            start += step
        return Double(values)

    def evaluate_binary_scalar_operator_expression(self, node):
        data0 = self.evaluate_expression(node.get_child(0))
        data1 = self.evaluate_expression(node.get_child(1))
        cls, fun = BSO_MAP[node.get_text()]
        if data0.Size == data1.Size:
            return cls([fun(*tup) for tup in zip(data0, data1)], size=data0.Size)
        if data0.Size == (1, 1):
            number = data0[0]
            return cls([fun(i, number) for i in data1], size=data1.Size)
        if data1.Size == (1, 1):
            number = data1[0]
            return cls([fun(i, number) for i in data0], size=data0.Size)
        # todo: Arrays have incompatible sizes for this operation.

    def evaluate_matrix_multiplication_expression(self, node):
        data0 = self.evaluate_expression(node.get_child(0))
        data1 = self.evaluate_expression(node.get_child(1))
        if data0.Size == (1, 1) or data1.Size == (1, 1):
            return self.evaluate_binary_scalar_operator_expression(node)
        # todo: matrix multiplication

    def evaluate_matrix_right_division_expression(self, node):
        data0 = self.evaluate_expression(node.get_child(0))
        data1 = self.evaluate_expression(node.get_child(1))
        if data0.Size == (1, 1) and data1.Size == (1, 1):
            return Double([data0[0] / data1[0]])
        # todo: matrix multiplication

    def evaluate_matrix_left_division_expression(self, node):
        data0 = self.evaluate_expression(node.get_child(0))
        data1 = self.evaluate_expression(node.get_child(1))
        if data0.Size == (1, 1) and data1.Size == (1, 1):
            return Double([data1[0] / data0[0]])
        # todo: matrix multiplication

    def evaluate_prefix_expression(self, node):
        data = self.evaluate_expression(node.get_child())
        cls, fun = USO_MAP[node.get_text()]
        return cls([fun(v) for v in data], size=data.Size)

    def evaluate_postfix_expression(self, node):
        data = self.evaluate_expression(node.get_child())
        return data.get_class()(data.refactored, size=tuple(reversed(data.Size)))

    def evaluate_primary_expression(self, node):
        # will not be used since in AST it is optimised to skip single-child node
        pass

    def evaluate_identifier_expression(self, node):
        var_name = node.get_text()
        if var_name in self.variables:
            return self.variables[var_name]
        else:
            # todo: raise unknown variable exception
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

    @staticmethod
    def evaluate_vector_literal(node):
        return Char([c for c in node.get_text()])

    def evaluate_array_list(self, node):
        array_list = []
        array = []
        for child in node.get_children():
            if child.get_type() == ASTNodeType.EO_STMT:
                if child.get_text() == ';' or child.get_text() == '\n':
                    if array:
                        array_list.append(array)
                        array = []
            else:
                data = self.evaluate_expression(child)
                if data.Data:
                    array.append(data)
        if array:
            array_list.append(array)

        if array_list:
            return concatenate([concatenate(array, "horz") for array in array_list], "vert")
        else:
            return Double([], size=(0, 0))

    def evaluate_array_expression(self, node):
        name = node.get_child(0).get_text()
        if name not in self.variables:
            # todo:
            return None
        data = self.variables[name]
        return data.visit(self.evaluate_index_list(node.get_child(1)))

    def evaluate_index_list(self, node):
        return [self.evaluate_expression(child) for child in node.get_children()]

    def get_variables(self):
        return self.variables

    def del_variables(self, var_list=None):
        if var_list:
            for var in var_list:
                # todo: check exist and raise error
                del self.variables[var]
        else:
            self.variables = {}
