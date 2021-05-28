from main.III_semantic.data_types.array import Array
from main.III_semantic.data_types.array_data.numeric_data.decimal_data.double import Double
import math


class Logical(Array):
    """
    https://ww2.mathworks.cn/help/matlab/ref/logical.html
    """
    parent = Double

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
        if isinstance(obj, str):
            # todo: "Conversion to logical from string is not possible."
            return None
        if math.isnan(obj):
            # todo: "NaN values cannot be converted to logicals."
            return None
        return bool(obj)
