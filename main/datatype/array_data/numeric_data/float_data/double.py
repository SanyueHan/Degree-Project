from main.datatype.array_data.numeric_data.float import Float


class Double(Float):
    def __init__(self, value, size=None):
        super().__init__(value, size)
        self.Value = [float(i) for i in self]
