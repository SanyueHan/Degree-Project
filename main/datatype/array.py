

class Array:
    def __init__(self, data, size=None):
        if size:
            if size[0] * size[1] != len(data):
                # todo raise error
                return
        else:
            size = (1, len(data))
        self.Data = data
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

    def transposed(self):
        return self.__class__(sum(self.cols(), []), (self.n, self.m))

    def to_string(self, fun):
        return '\n'.join([''.join([fun(v) for v in r]) for r in self.rows()])

    def get_class(self):
        return self.__class__

    @classmethod
    def get_super(cls):
        return cls.__base__

    def get_class_name(self):
        return self.__class__.__qualname__

    def visit(self, index_list):
        if len(index_list) == 1:
            pass
        elif len(index_list) == 2:
            pass
        else:
            pass

    @property
    def m(self):
        return self.Size[0]

    @property
    def n(self):
        return self.Size[1]
