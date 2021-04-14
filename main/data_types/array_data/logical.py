from main.data_types.array import Array
from main.data_types.array_data.numeric_data.decimal_data.double import Double


class Logical(Array):
    """
    The logical data type represents true or false states using the numbers 1 and 0, respectively.
    Certain MATLAB® functions and operators return logical values to indicate fulfillment of a condition.
    You can use those logical values to index into an array or execute conditional code.

    (https://ww2.mathworks.cn/help/matlab/logical-operations.html)
    """
    parent = Double

    def __init__(self, data, size=None):
        super().__init__(data, size)

    def __str__(self):
        if len(self) == 1:
            prefix = "  logical\n\n"
        else:
            prefix = f"  {self.m}x{self.n} logical array\n\n"
        return prefix + self.pile(self.format_setter)

    @staticmethod
    def format_setter(value):
        return "   1" if value else "   0"

    @staticmethod
    def convert(obj):
        return bool(obj)
