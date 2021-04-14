

class Array:
    def __init__(self, data, size=None):
        if size:
            if size[0] * size[1] != len(data):
                # todo raise error
                return
        else:
            size = (1, len(data))
        self.Data = [self.convert(element) for element in data]
        self.Size = size

    def __bool__(self):
        return all(self.Data)

    def __iter__(self):
        return iter(self.Data)

    def __getitem__(self, i):
        return self.Data[i]

    def __len__(self):
        return len(self.Data)

    def rows(self):
        return [[self[i * self.n + j] for j in range(self.n)] for i in range(self.m)]

    def cols(self):
        return [[self[i * self.n + j] for i in range(self.m)] for j in range(self.n)]

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
            return self.__class__([data[to_int(element)-1] for element in index], size=index.Size)
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
        return self.Size[0]

    @property
    def n(self):
        return self.Size[1]


def to_int(number):
    if int(number) == number:
        return int(number)
    else:
        # todo: Array indices must be positive integers or logical values.
        return None
