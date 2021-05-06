from main.III_semantic.utils import compat
from main.data_types.array_data.char import Char
from main.data_types.array_data.string import String
from main.data_types.array_data.logical import Logical
from main.data_types.array_data.numeric_data.decimal_data.double import Double
from main.exceptions.semantic_exceptions import *


# unary
def evaluate_transpose_operation(operand):
    return operand.get_class()(operand.refactored, size=tuple(reversed(operand.size)))


def evaluate_array_sign_operation(operand, operator):
    if isinstance(operand, String):
        # todo: Unary operator '+' is not supported for operand of type 'string'.
        pass
    if operand.get_class() in (Char, Logical, Double):
        fun = {
            '+': lambda x: +x,
            '-': lambda x: -x
        }[operator]
        return Double([fun(i) for i in operand], size=operand.size)


def evaluate_logic_not_operator(operand):
    if isinstance(operand, String):
        # todo: Unary operator '~' is not supported for operand of type 'string'.
        pass
    operand = Logical([i for i in operand], size=operand.size)
    return Logical([not i for i in operand], size=operand.size)


# binary
def evaluate_matrix_multiplication_operation(operand_0, operand_1):
    if operand_0.size == (1, 1) or operand_1.size == (1, 1):
        compat(operand_0, operand_1)
        if isinstance(operand_0, String) or isinstance(operand_1, String):
            # todo: Operator '*' is not supported for operands of type 'string'.
            return None
        return evaluate_array_multiplication_operation(operand_0, operand_1)
    # todo: matrix multiplication


def evaluate_matrix_right_division_operation(operand_0, operand_1):
    if operand_0.size == (1, 1) and operand_1.size == (1, 1):
        if isinstance(operand_0, String) or isinstance(operand_1, String):
            # todo: Error using  /  \nArguments must be numeric, char, or logical.
            return None
        return evaluate_array_right_division_operation(operand_0, operand_1)
    # todo: matrix multiplication


def evaluate_matrix_left_division_operation(operand_0, operand_1):
    if operand_0.size == (1, 1) and operand_1.size == (1, 1):
        if isinstance(operand_0, String) or isinstance(operand_1, String):
            # todo: Error using  \  \nArguments must be numeric, char, or logical.
            return None
        return evaluate_array_left_division_operation(operand_0, operand_1)
    # todo: matrix multiplication


def evaluate_addition_operation(operand_0, operand_1):
    if isinstance(operand_0, String) or isinstance(operand_1, String):
        def fun(a, b):
            return str(a) + str(b)
        return String([fun(*tup) for tup in zip(operand_0, operand_1)], size=operand_0.size)
    else:
        def fun(a, b):
            return a + b
        return Double([fun(*tup) for tup in zip(operand_0, operand_1)], size=operand_0.size)


def evaluate_subtraction_operation(operand_0, operand_1):
    if isinstance(operand_0, String) or isinstance(operand_1, String):
        # todo: Operator '-' is not supported for operands of type 'string'.
        return None
    else:
        def fun(a, b):
            return a - b
        return Double([fun(*tup) for tup in zip(operand_0, operand_1)], size=operand_0.size)


def evaluate_array_multiplication_operation(operand_0, operand_1):
    if isinstance(operand_0, String) or isinstance(operand_1, String):
        # todo: Operator '.*' is not supported for operands of type 'string'.
        return None
    else:
        def fun(a, b):
            return a * b
        return Double([fun(*tup) for tup in zip(operand_0, operand_1)], size=operand_0.size)


def evaluate_array_right_division_operation(operand_0, operand_1):
    if isinstance(operand_0, String) or isinstance(operand_1, String):
        # todo: Operator './' is not supported for operands of type 'string'.
        return None
    else:
        def fun(a, b):
            if b:
                return a / b
            else:
                return float('inf') if a else float('nan')
        return Double([fun(*tup) for tup in zip(operand_0, operand_1)], size=operand_0.size)


def evaluate_array_left_division_operation(operand_0, operand_1):
    if isinstance(operand_0, String) or isinstance(operand_1, String):
        # todo: Operator '.\' is not supported for operands of type 'string'.
        return None
    else:
        def fun(a, b):
            if a:
                return b / a
            else:
                return float('inf') if b else float('nan')
        return Double([fun(*tup) for tup in zip(operand_0, operand_1)], size=operand_0.size)


def evaluate_relational_operations(operand_0, operand_1, operator):
    if isinstance(operand_0, String) != isinstance(operand_1, String):
        # one is String while one is not String
        # todo: f"Comparison between {a.get_class_name().lower()} and {b.get_class_name().lower()} is not supported."
        pass
    fun = RELATIONAL_OPERATORS[operator]
    return Logical([fun(*tup) for tup in zip(operand_0, operand_1)], size=operand_0.size)


MATRIX_OPERATORS = {
    '*': evaluate_matrix_multiplication_operation,
    '/': evaluate_matrix_right_division_operation,
    '\\': evaluate_matrix_left_division_operation,
}

ARITHMETIC_OPERATORS = {
    '+': evaluate_addition_operation,
    '-': evaluate_subtraction_operation,
    '.*': evaluate_array_multiplication_operation,
    './': evaluate_array_right_division_operation,
    '.\\': evaluate_array_left_division_operation
}

RELATIONAL_OPERATORS = {
    '==': lambda x, y: x == y,
    '>=': lambda x, y: x >= y,
    '>': lambda x, y: x > y,
    '<=': lambda x, y: x <= y,
    '<': lambda x, y: x < y,
    '~=': lambda x, y: x != y
}
