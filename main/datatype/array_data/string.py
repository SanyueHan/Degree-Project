from main.datatype.array import Array


class String(Array):
    def __init__(self, data, size=None):
        super().__init__(data, size)
        self.Data = [self.represent(i) for i in self]

    def __str__(self):
        if len(self) < 2:
            prefix = ""
        else:
            prefix = f"  {self.m}×{self.n} string array\n\n"
        return prefix + self.to_string(lambda string: "    "+string)

    @staticmethod
    def represent(obj):
        if isinstance(obj, float):
            if obj == int(obj):
                return '"' + str((int(obj))) + '"'
        return str(obj)
