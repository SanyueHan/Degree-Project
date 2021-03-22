from main.datatype.classes import DataClass
from main.datatype.data.array_data.numeric_data.float import Float


class Double(Float):
    Class = DataClass.DOUBLE

    def __init__(self, value, size=(1, 1)):
        super().__init__(value, size)
        self.Value = [float(i) for i in self]
