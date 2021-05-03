from main.data_types.array_data.char import Char
from main.data_types.array_data.string import String
from main.data_types.array_data.numeric_data.decimal_data.double import Double


def evaluate_number_literal_expression(node):
    """
    By default, MATLAB® stores all numeric variables as double-precision floating-point values.
    """
    text = node.get_text()
    if text in ('Inf', 'inf'):
        return Double([float('inf')])
    if text in ('NaN', 'nan'):
        return Double([float('nan')])
    return Double([text])


def evaluate_string_literal_expression(node):
    return String([node.get_text().replace('""', '"')])


def evaluate_vector_literal_expression(node):
    return Char([ord(c) for c in node.get_text().replace("''", "'")])
