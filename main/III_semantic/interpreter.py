from main.II_syntactic.node_types import ASTNodeType
from main.III_semantic.utils import concatenate
from main.III_semantic.builtins import *
from main.III_semantic.literals import *
from main.III_semantic.operations import *


class Interpreter:
    def __init__(self):
        self.interpret = {
            ASTNodeType.STMT_LIST: self.interpret_statement_list,
            ASTNodeType.EXP_STMT: self.interpret_expression_statement,
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
            ASTNodeType.ARRAY_LIST_EXP: self.evaluate_array_list_expression,
            ASTNodeType.INDEX_LIST_EXP: self.evaluate_index_list_expression,
            ASTNodeType.IDENTIFIER_EXP: self.evaluate_identifier_expression,
        }
        self.variables = {}
        self.builtins = BUILT_IN_FUNCTIONS

    def get_variables(self):
        return self.variables

    def retrieve(self, identifier):
        if identifier in self.variables:
            return self.variables[identifier]
        if identifier in self.builtins:
            return self.builtins[identifier]
        # todo: Unrecognized function or variable {identifier}.

    def del_variables(self, var_list=None):
        if var_list:
            for var in var_list:
                # todo: check exist and raise error
                del self.variables[var]
        else:
            self.variables = {}

    def interpret_statement_list(self, lst):
        for child in lst.get_children():
            self.interpret_statement(child)

    def interpret_statement(self, stmt):
        result = self.interpret[stmt.get_type()](stmt)
        # if statement does not ended with a semicolon, the result is printed
        if result:
            var = result[0]
            obj = result[1]
            ass_str = " = " if obj.get_class() == String else " ="
            print(f"\n{var}{ass_str}\n\n{str(obj)}\n")

    def interpret_expression_statement(self, stmt):
        expression = stmt.get_child(0)
        if expression.get_type() == ASTNodeType.ASS_EXP:
            var = expression.get_child(0).get_text()
            val = self.evaluate_expression(expression.get_child(1))
            self.variables[var] = val
        else:
            if expression.get_type() == ASTNodeType.IDENTIFIER_EXP and expression.get_children() == [] \
                    and expression.get_text() not in self.builtins:
                # calling builtin function always result in 'ans', although sometime it looks like retrieval a variable
                var = expression.get_text()
            else:
                var = "ans"
            val = self.evaluate_expression(expression)
            self.variables[var] = val
        return (var, val) if stmt.get_child(1).get_text() != ';' else None

    def interpret_clear_statement(self, stmt):
        variables = [child.get_text() for child in stmt.get_child(0).get_children()]
        self.del_variables(var_list=variables if variables else None)

    def interpret_selection_statement(self, stmt):
        if stmt.get_text() == 'if':
            for clause in stmt.get_children()[:-1]:
                if self.interpret_selection_clause(clause):
                    break
        else:
            switch_clause = stmt.get_child(0)
            switch_exp = self.evaluate_expression(switch_clause.get_child(0))
            for clause in stmt.get_children()[1:-1]:
                if self.interpret_selection_clause(clause, switch_exp=switch_exp):
                    break

    def interpret_selection_clause(self, clause, switch_exp=None):
        if clause.get_text() in ('else', 'otherwise'):
            self.interpret_statement_list(clause.get_child(0))
        else:
            exp = self.evaluate_expression(clause.get_child(0))
            if clause.get_text() in ('if', 'elseif') and exp or clause.get_text() == 'case' and exp == switch_exp:
                self.interpret_statement_list(clause.get_child(1))
                return True
            else:
                return False

    def interpret_iteration_statement(self, stmt):
        self.interpret_iteration_clause(stmt.get_child())

    def interpret_iteration_clause(self, clause):
        expression = clause.get_child(0)
        statement_list = clause.get_child(1)
        if clause.get_text() == 'while':
            while self.evaluate_expression(expression):
                self.interpret_statement_list(statement_list)
        else:
            name = expression.get_child(0).get_text()
            data = self.evaluate_expression(expression.get_child(1))
            for col in data.cols():
                self.variables[name] = data.get_class()(col, size=(len(col), 1))
                self.interpret_statement_list(statement_list)

    def interpret_jump_statement(self, stmt):
        pass

    def evaluate_expression(self, exp):
        return self.evaluate[exp.get_type()](exp)

    def evaluate_unary_operation_expression(self, exp):
        operator = exp.get_text()
        operand = self.evaluate_expression(exp.get_child(0))
        if operator in ('.\'', '\''):
            return evaluate_transpose_operation(operand)
        if operator in ('+', '-'):
            return evaluate_array_sign_operation(operand, operator)
        if operator == '~':
            return evaluate_logic_not_operator(operand)

    def evaluate_binary_operation_expression(self, exp):
        operator = exp.get_text()
        child_0 = exp.get_child(0)
        child_1 = exp.get_child(1)
        if operator in ('&&', '||'):
            return self.evaluate_logical_operations(child_0, child_1, operator)

        operand_0 = self.evaluate_expression(child_0)
        operand_1 = self.evaluate_expression(child_1)

        if operator in MATRIX_OPERATORS:
            return MATRIX_OPERATORS[operator](operand_0, operand_1)

        # binary scalar operators left
        compat(operand_0, operand_1)

        if operator in ARITHMETIC_OPERATORS:
            return ARITHMETIC_OPERATORS[operator](operand_0, operand_1)
        return evaluate_relational_operations(operand_0, operand_1, operator)

    def evaluate_colon_expression(self, exp):
        if exp.num_children() == 0:
            return ":"

        if exp.num_children() == 2:
            start = self.evaluate_expression(exp.get_child(0))[0]
            step = 1
            end = self.evaluate_expression(exp.get_child(1))[0]
        else:
            start = self.evaluate_expression(exp.get_child(0))[0]
            step = self.evaluate_expression(exp.get_child(1))[0]
            end = self.evaluate_expression(exp.get_child(2))[0]

        if step == 0 or start < end and step < 0 or start > end and step > 0:
            return Double([])

        values = []
        while start <= end:
            values.append(start)
            start += step
        return Double(values)

    def evaluate_array_list_expression(self, exp):
        array_list = []
        array = []
        for child in exp.get_children():
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

    def evaluate_index_list_expression(self, exp):
        return [self.evaluate_expression(child) for child in exp.get_children()]

    @staticmethod
    def evaluate_ident_list_expression(exp):
        return [String([child.get_text()]) for child in exp.get_children()]

    def evaluate_identifier_expression(self, exp):
        ref = exp.get_text()
        obj = self.retrieve(ref)

        arguments = []
        if exp.get_children():
            child = exp.get_child(0)
            if child.get_type() == ASTNodeType.INDEX_LIST_EXP:
                arguments = self.evaluate_index_list_expression(child)
            else:
                arguments = self.evaluate_ident_list_expression(child)

        return obj(arguments)

    def evaluate_logical_operations(self, child_0, child_1, operator):
        """
        https://ww2.mathworks.cn/help/matlab/ref/logicaloperatorsshortcircuit.html#bt_0nai-1
        """
        operand_0 = self.evaluate_expression(child_0)
        if len(operand_0) > 1:
            "Operands to the logical and (&&) and or (||) operators must be convertible to logical scalar\nvalues."
        operand_0 = Logical([operand_0[0]])

        if operator == '||' and operand_0[0]:
            return Logical([True])
        if operator == '&&' and not operand_0[0]:
            return Logical([False])

        operand_1 = self.evaluate_expression(child_1)
        if len(operand_1) > 1:
            "Operands to the logical and (&&) and or (||) operators must be convertible to logical scalar\nvalues."
        operand_1 = Logical([operand_1[0]])
        return Logical([True]) if operand_1[0] else Logical([False])
