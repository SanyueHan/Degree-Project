from main.III_semantic.data_types.array_data.char import Char
from main.III_semantic.data_types.array_data.string import String
from main.III_semantic.data_types.array_data.numeric_data.decimal_data.double import Double


def evaluate_number_literal_expression(node):
    """
    By default, MATLAB® stores all numeric variables as double-precision floating-point values.
    """
    return Double([node.get_text()])


def evaluate_string_literal_expression(node):
    return String([node.get_text().replace('""', '"')])


def evaluate_vector_literal_expression(node):
    return Char([ord(c) for c in node.get_text().replace("''", "'")])
