from main.datatype.classes import DataClass
from main.datatype.data.array import Array


class Logical(Array):
    Class = DataClass.LOGICAL

    def __init__(self, value, size=(1, 1)):
        super().__init__(value, size)
        self.Value = [(1 if i else 0) for i in self]

    def __str__(self):
        if len(self) == 1:
            prefix = "  logical\n\n"
        else:
            prefix = f"  {self.Size[0]}×{self.Size[1]} logical array\n\n"
        return prefix + self.to_string(lambda logic_value: "   "+str(logic_value))
