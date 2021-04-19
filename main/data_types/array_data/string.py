from main.data_types.array import Array


class String(Array):
    """
    https://ww2.mathworks.cn/help/matlab/ref/string.html
    """

    def __str__(self):
        if len(self) < 2:
            prefix = ""
        else:
            prefix = f"  {self.m}x{self.n} string array\n\n"
        return prefix + self.pile(lambda string: "    " + '\"' + string + '\"')

    @staticmethod
    def convert(obj):
        if isinstance(obj, float):
            if obj == int(obj):
                return str(int(obj))
            else:
                return str(obj)
        if isinstance(obj, bool):
            if obj:
                return "true"
            else:
                return "false"
        return str(obj)
