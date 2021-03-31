from main.datatype.array import Array


class Logical(Array):
    def __init__(self, value, size=None):
        super().__init__(value, size)
        self.Value = [(1 if i else 0) for i in self]

    def __str__(self):
        if len(self) == 1:
            prefix = "  logical\n\n"
        else:
            prefix = f"  {self.m}×{self.n} logical array\n\n"
        return prefix + self.to_string(lambda logic_value: "   "+str(logic_value))
