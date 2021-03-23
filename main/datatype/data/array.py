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
        return [[self[i * self.Size[1] + j] for j in range(self.Size[1])] for i in range(self.Size[0])]

    def cols(self):
        return [[self[i * self.Size[1] + j] for i in range(self.Size[0])] for j in range(self.Size[1])]

    def transposed(self):
        return self.__class__(sum(self.cols(), []), (self.Size[1], self.Size[0]))

    def to_string(self, fun, **args_dict):
        return '\n'.join([''.join([fun(v, **args_dict) for v in r]) for r in self.rows()])
