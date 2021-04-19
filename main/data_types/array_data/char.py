from main.data_types.array import Array


class Char(Array):
    """
    https://ww2.mathworks.cn/help/matlab/ref/char.html
    """
    def __str__(self):
        if self.n == 0:
            return "  0x0 empty char array"

        if self.m == 1:
            prefix = ""
        else:
            prefix = f"  {self.m}x{self.n} char array\n\n"

        return prefix + '\n'.join('    ' + '\'' + ''.join(c for c in row) + '\'' for row in self.rows())

