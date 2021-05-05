from main.data_types.data import Data


class Array(Data):
    def __init__(self, data, size=None):
        if size:
            if size[0] * size[1] != len(data):
                # todo raise error
                return
        else:
            size = (1, len(data))
        self.data = [self.convert(element) for element in data]
        self.size = size

    def __bool__(self):
        return all(self.data)

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, i):
        return self.data[i]

    def __len__(self):
        return len(self.data)

    def __eq__(self, other):
        return self.data == other.data and self.size == other.size

    def rows(self):
        return [[self[i * self.n + j] for j in range(self.n)] for i in range(self.m)]

    def cols(self):
        return [[self[i * self.n + j] for i in range(self.m)] for j in range(self.n)]

    def expand_row(self, num):
        self.data = self.data * num
        self.size = (self.size[0] * num, self.size[1])

    def expand_col(self, num):
        self.data = sum(([i for _ in range(num)] for i in self), [])
        self.size = (self.size[0], self.size[1] * num)

    @property
    def refactored(self):
        return sum(self.cols(), [])

    def pile(self, fun):
        return '\n'.join([''.join([fun(v) for v in r]) for r in self.rows()])

    def get_class(self):
        return self.__class__

    @classmethod
    def get_super(cls):
        return cls.__base__

    def get_class_name(self):
        return self.__class__.__qualname__

    @staticmethod
    def convert(obj):
        return obj

    def visit(self, index_list):
        if len(index_list) == 1:
            index = index_list[0]
            if index == ':':
                return self.__class__(self.refactored, size=(len(self), 1))
            data = self.refactored
            return self.__class__([data[to_int(element)-1] for element in index], size=index.size)
        elif len(index_list) == 2:
            index_m = index_list[0]
            if index_m == ":":
                index_m = [i for i in range(0, self.m)]
            else:
                index_m = [to_int(i) - 1 for i in index_m.refactored]

            index_n = index_list[1]
            if index_n == ":":
                index_n = [i for i in range(0, self.n)]
            else:
                index_n = [to_int(i) - 1 for i in index_n.refactored]

            return self.__class__([self[i * self.n + j] for i in index_m for j in index_n],
                                  size=(len(index_m), len(index_n)))
        else:
            pass

    @property
    def m(self):
        return self.size[0]

    @property
    def n(self):
        return self.size[1]


def to_int(number):
    if int(number) == number:
        return int(number)
    else:
        # todo: Array indices must be positive integers or logical values.
        return None
