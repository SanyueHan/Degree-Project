from main.datatype.array import Array
from main.datatype.array_data.numeric_data.float_data.double import Double


class Logical(Array):
    parent = Double

    def __init__(self, data, size=None):
        super().__init__(data, size)
        self.Data = [(1 if i else 0) for i in self]

    def __str__(self):
        if len(self) == 1:
            prefix = "  logical\n\n"
        else:
            prefix = f"  {self.m}×{self.n} logical array\n\n"
        return prefix + self.to_string(lambda logic_value: "   "+str(logic_value))
