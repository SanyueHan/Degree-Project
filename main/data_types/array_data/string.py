from main.data_types.array import Array


class String(Array):
    def __init__(self, data, size=None):
        super().__init__(data, size)

    def __str__(self):
        if len(self) < 2:
            prefix = ""
        else:
            prefix = f"  {self.m}x{self.n} string array\n\n"
        return prefix + self.pile(lambda string: "    " + string)

    @staticmethod
    def convert(obj):
        if isinstance(obj, float):
            if obj == int(obj):
                res = int(obj)
            else:
                res = obj
            return '"' + str(res) + '"'
        if isinstance(obj, bool):
            if obj:
                res = "true"
            else:
                res = "false"
            return '"' + res + '"'
        return str(obj)
