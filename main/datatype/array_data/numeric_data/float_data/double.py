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
            return "  1x0 empty double row vector"
        if all((int(n) == n) for n in self):
            max_len = max(self.excluding_sign_integer_length(n) for n in self)
            if max_len <= 3:
                return self.pile(self.format_setter(width=6, precision=0))
            elif max_len <= 8:
                return self.pile(self.format_setter(width=12, precision=0))
        return self.pile(self.format_setter())
        # todo: scientific notation for too big or too small

    @staticmethod
    def excluding_sign_integer_length(number):
        string = str(int(number)).lstrip('-')
        return len(string)

    @staticmethod
    def format_setter(width=10, precision=4):
        if precision == 0:
            def fun(item):
                return f"{int(item):>{width}d}"
            return fun
        else:
            def fun(item):
                return f"{item:>{width}.{precision}f}"
            return fun

    @staticmethod
    def convert(obj):
        if isinstance(obj, bool):
            return 1.0 if obj else 0.0
        return float(obj)


if __name__ == "__main__":
    print(Double([]).get_class())
    print(Double([]).get_super())
    print(Double.get_super())
    print(Float is not Double)
    print(Float is (not Double))
