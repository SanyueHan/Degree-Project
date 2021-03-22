from main.datatype.classes import DataClass
from main.datatype.data.array import Array


class String(Array):
    Class = DataClass.STRING

    def __init__(self, value, size=(1, 1)):
        super().__init__(value, size)
        self.Value = [str(i) for i in self]
