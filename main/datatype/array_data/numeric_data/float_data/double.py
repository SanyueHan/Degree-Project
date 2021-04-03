from main.datatype.array_data.numeric_data.float import Float
from main.datatype.array_data.string import String


class Double(Float):
    parent = String

    def __init__(self, data, size=None):
        super().__init__(data, size)

    def __str__(self):
        if self.Size == (0, 0):
            return "     []"
        if self.n == 0:
            return "  1×0 empty double row vector"
        if all((int(i) == i) for i in self):
            max_len = max(len(str(int(i))) for i in self)
            if max_len <= 3:
                return self.pile(self.format_setter(width=6, precision=0))
            elif max_len <= 8:
                return self.pile(self.format_setter(width=12, precision=0))
        return self.pile(self.format_setter())
        # todo: scientific notation for too big or too small

    @staticmethod
    def format_setter(width=10, precision=4):
        def fun(item):
            return f"{item:>{width}.{precision}f}"
        return fun

    @staticmethod
    def convert(obj):
        if isinstance(obj, bool):
            if obj:
                res = 0
            else:
                res = 0
            return float(res)
        return float(obj)


if __name__ == "__main__":
    print(Double([]).get_class())
    print(Double([]).get_super())
    print(Double.get_super())
    print(Float is not Double)
    print(Float is (not Double))
