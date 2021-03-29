from main.datatype.classes import DataClass


class Array:
    Class = DataClass.ARRAY

    def __init__(self, value, size=None):
        if size:
            if size[0] * size[1] != len(value):
                # todo raise error
                return
        else:
            size = (1, len(value))
        self.Value = value
        self.Size = size

    def __bool__(self):
        return all(self.Value)

    def __iter__(self):
        return iter(self.Value)

    def __getitem__(self, i):
        return self.Value[i]

    def __len__(self):
        return len(self.Value)

    def rows(self):
        return [[self[i * self.n + j] for j in range(self.n)] for i in range(self.m)]

    def cols(self):
        return [[self[i * self.n + j] for i in range(self.m)] for j in range(self.n)]

    def transposed(self):
        return self.__class__(sum(self.cols(), []), (self.n, self.m))

    def to_string(self, fun, **args_dict):
        return '\n'.join([''.join([fun(v, **args_dict) for v in r]) for r in self.rows()])

    def create_same(self, *args, **kwargs):
        return self.__class__(*args, **kwargs)

    @property
    def m(self):
        return self.Size[0]

    @property
    def n(self):
        return self.Size[1]
