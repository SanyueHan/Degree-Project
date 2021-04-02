from main.datatype.array import Array


class String(Array):
    def __init__(self, data, size=None):
        super().__init__(data, size)
        self.Data = [str(i) for i in self]

    def __str__(self):
        if len(self) < 2:
            prefix = ""
        else:
            prefix = f"  {self.m}×{self.n} string array\n\n"
        return prefix + self.to_string(lambda string: "    "+string)
