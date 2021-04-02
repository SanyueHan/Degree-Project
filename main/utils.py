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


def find_nearest_common_ancestor(class_set):
    while len(class_set) > 1:
        class_a = class_set.pop()
        class_b = class_set.pop()
        class_set.add(find_nearest_mutual_ancestor(class_a, class_b))
    return class_set.pop()


def find_nearest_mutual_ancestor(class_a, class_b):
    if class_a is class_b:
        return class_a
    a_ancestors = {class_a}
    b_ancestors = {class_b}
    while True:
        if class_a is not Array:
            class_a = class_a.get_super()
            if class_a in b_ancestors:
                return class_a
            else:
                a_ancestors.add(class_a)
        if class_a is not Array:
            class_b = class_b.get_super()
            if class_b in a_ancestors:
                return class_b
            else:
                b_ancestors.add(class_b)
