from main.II_syntactic.node_types import ASTNodeType
from main.III_semantic.utils import concatenate
from main.III_semantic.literals import *
from main.III_semantic.operations import *


class Interpreter:
    def __init__(self):
        self.interpret = {
            ASTNodeType.STMT_LIST: self.interpret_statement_list,
            ASTNodeType.EXP_STMT: self.interpret_expression_statement,
            ASTNodeType.CLR_STMT: self.interpret_clear_statement,
            ASTNodeType.SEL_STMT: self.interpret_selection_statement,
            ASTNodeType.ITR_STMT: self.interpret_iteration_statement,
            ASTNodeType.JMP_STMT: self.interpret_jump_statement,
        }
        self.evaluate = {
            ASTNodeType.CLN_EXP: self.evaluate_colon_expression,
            ASTNodeType.UOP_EXP: self.evaluate_unary_operation_expression,
            ASTNodeType.BOP_EXP: self.evaluate_binary_operation_expression,
            ASTNodeType.NUMBER_LIT_EXP: evaluate_number_literal_expression,
            ASTNodeType.STRING_LIT_EXP: evaluate_string_literal_expression,
            ASTNodeType.VECTOR_LIT_EXP: evaluate_vector_literal_expression,
            ASTNodeType.IDENTIFIER_EXP: self.evaluate_identifier_expression,
            ASTNodeType.ARRAY_LIST_EXP: self.evaluate_array_list_expression,
            ASTNodeType.INDEX_LIST_EXP: self.evaluate_index_list_expression,
            ASTNodeType.INDEXING_EXP: self.evaluate_indexing_expression,
        }
        self.variables = {}

    def get_variables(self):
        return self.variables

    def del_variables(self, var_list=None):
        if var_list:
            for var in var_list:
                # todo: check exist and raise error
                del self.variables[var]
        else:
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

    def interpret_expression_statement(self, node):
        expression = node.get_child(0)
        if expression.get_type() == ASTNodeType.ASS_EXP:
            var = expression.get_child(0).get_text()
            val = self.evaluate_expression(expression.get_child(1))
            self.variables[var] = val
        else:  # normal expression
            if expression.get_type() == ASTNodeType.IDENTIFIER_EXP:
                var = expression.get_text()
                val = self.variables[var]
            else:
                var = "ans"
                val = self.evaluate_expression(expression)
                self.variables["ans"] = val
        return (var, val) if node.get_child(1).get_text() != ';' else None

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

    def evaluate_unary_operation_expression(self, node):
        operator = node.get_text()
        operand = self.evaluate_expression(node.get_child(0))
        if operator in ('.\'', '\''):
            return evaluate_transpose_operation(operand)
        if operator in ('+', '-'):
            return evaluate_array_sign_operation(operand, operator)
        if operator == '~':
            return evaluate_logic_not_operator(operand)

    def evaluate_binary_operation_expression(self, node):
        operator = node.get_text()

        a = self.evaluate_expression(node.get_child(0))
        b = self.evaluate_expression(node.get_child(1))

        if operator in MATRIX_OPERATORS:
            return MATRIX_OPERATORS[operator](a, b)

        # binary scalar operators left
        compat(a, b)

        if operator in ARITHMETIC_OPERATORS:
            return ARITHMETIC_OPERATORS[operator](a, b)
        if operator in RELATIONAL_OPERATORS:
            return evaluate_relational_operations(a, b, operator)
        if operator in LOGICAL_OPERATORS:
            return evaluate_logical_operations(a, b, operator)

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

    def evaluate_identifier_expression(self, node):
        var_name = node.get_text()
        if var_name in self.variables:
            return self.variables[var_name]
        else:
            # todo: raise unknown variable exception
            pass

    def evaluate_array_list_expression(self, node):
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
                if data.data:
                    array.append(data)
        if array:
            array_list.append(array)

        if array_list:
            return concatenate([concatenate(array, "horz") for array in array_list], "vert")
        else:
            return Double([], size=(0, 0))

    def evaluate_index_list_expression(self, node):
        return [self.evaluate_expression(child) for child in node.get_children()]

    def evaluate_indexing_expression(self, node):
        name = node.get_child(0).get_text()
        if name not in self.variables:
            # todo:
            return None
        data = self.variables[name]
        return data.visit(self.evaluate_index_list_expression(node.get_child(1)))






