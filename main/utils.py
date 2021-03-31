from functools import reduce
from main.datatype.array import Array


def concatenate(data_list, direction):
    if direction == "horz":
        if not reduce(lambda a, b: a == b, [data.m for data in data_list]):
            # todo: "Error using vertcat\nDimensions of arrays being concatenated are not consistent."
            return None
        data = sum((sum(list(tup), []) for tup in zip(*[data.rows() for data in data_list])), [])
        size = (data_list[0].m, sum(data.n for data in data_list))
        cls = find_nearest_common_ancestor(set(data.get_class() for data in data_list))
        return cls(data, size)
    if direction == "vert":
        if not reduce(lambda a, b: a == b, [data.n for data in data_list]):
            # todo: "Error using horzcat\nDimensions of arrays being concatenated are not consistent."
            return None
        data = sum(sum((data.rows() for data in data_list), []), [])
        size = (sum(data.m for data in data_list), data_list[0].n)
        cls = find_nearest_common_ancestor(set(data.get_class() for data in data_list))
        return cls(data, size)


def find_nearest_common_ancestor(s):
    while len(s) > 1:
        a = s.pop()
        b = s.pop()
        find_nearest_mutual_ancestor(a, b)
    return s.pop()


def find_nearest_mutual_ancestor(a, b):
    if a is b:
        return a
    a_set = {a}
    b_set = {b}
    while True:
        if a is Array or b is Array:
            return Array
        a_super = a.get_super()
        if a_super in b_set:
            return a_super
        else:
            a_set.add(a_super)
        b_super = b.get_super()
        if b_super in a_set:
            return b_super
        else:
            b_set.add(b_super)
