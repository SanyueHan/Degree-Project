from main.data_types.array_data.numeric_data.decimal import Decimal
from main.data_types.array_data.string import String


class Double(Decimal):
    """
    https://ww2.mathworks.cn/help/matlab/ref/double.html
    """
    parent = String

    def __str__(self):
        if self.size == (0, 0):
            return "     []"
        if self.n == 0:  # 1：0.1
            return "  1x0 empty double row vector"
        if all((int(n) == n) for n in self):
            max_len = max(self.excluding_sign_integer_length(n) for n in self)
            if max_len <= 3:
                return self.pile(self.format_setter(width=6, precision=0))
            elif max_len <= 8:
                return self.pile(self.format_setter(width=12, precision=0))
            else:
                return self.pile(self.format_setter(width=13, sci=True))
        if not self.need_scientific():
            return self.pile(self.format_setter())
        if self.n == 1:
            return self.pile(self.format_setter(width=13, sci=True))
        return self.sci_representation()

    # todo: Finished!!!scientific notation for too big or too small
    def need_scientific(self):
        count = 0
        for n in self:
            if int(n) == n and self.excluding_sign_integer_length(n) < 9:
                continue
            if int(n) == n and self.excluding_sign_integer_length(n) >= 9:
                return True
            if abs(n) > 999.9999:
                return True
            if abs(n) <= 0.001:
                count += 1
        return count == self.__len__()

    def sci_representation(self):
        _min = _max = self[0]
        for n in self:
            _min = min(abs(n), _min)
            _max = max(abs(n), _max)
        if _max >= 1000:
            base = self.get_sci_base(_max, True)
        else:
            base = self.get_sci_base(_max, False)
        result = f'{(10**base):>{10}.{1}e}' + " *\n\n"
        fun = self.format_setter()
        result += ''.join([''.join([fun(v/(10**base)) for v in r]) for r in self.rows()])
        return result

    @staticmethod
    def get_sci_base(num, positive):
        base = 2 if positive else -2
        delta = 1 if positive else -1
        while (10**(base + delta) < num and positive) or (10**(base + delta) > num and not positive):
            base += delta
        return base

    @staticmethod
    def excluding_sign_integer_length(number):
        string = str(int(number)).lstrip('-')  # 删掉-
        return len(string)

    @staticmethod
    def format_setter(width=10, precision=4, sci=False):
        if sci:
            def fun(item):
                return f"{item:>{width}.{precision}e}"
            return fun
        elif precision == 0:
            def fun(item):
                return f"{int(item):>{width}d}"  # format
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
    print(Decimal is not Double)
    print(Decimal is (not Double))
