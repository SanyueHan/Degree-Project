from main.datatype.array import Array
from main.datatype.array_data.numeric_data.float_data.double import Double


class Logical(Array):
    parent = Double

    def __init__(self, data, size=None):
        super().__init__(data, size)

    def __str__(self):
        if len(self) == 1:
            prefix = "  logical\n\n"
        else:
            prefix = f"  {self.m}×{self.n} logical array\n\n"
        return prefix + self.pile(self.format_setter)

    @staticmethod
    def format_setter(value):
        return "    1" if value else "    0"

    @staticmethod
    def convert(obj):
        return bool(obj)
