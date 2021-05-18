from main.data_types.array_data.string import String
from main.exceptions.semantic_exceptions import *


def concatenate(data_list, direction):
    if direction == "horz":
        if len(set([data.m for data in data_list])) > 1:
            # todo: "Error using vertcat\nDimensions of arrays being concatenated are not consistent."
            line = 0
            filename = 'test'
            error_statement = 'a="str"'
            temp = DimensionNotConsistentError(line, filename, error_statement)
            temp.modify_mess('vertcat')
            raise temp
        data = sum((sum(list(tup), []) for tup in zip(*[data.rows() for data in data_list])), [])
        size = (data_list[0].m, sum(data.n for data in data_list))
        cls = find_nearest_common_ancestor(set(data.get_class() for data in data_list))
        return cls(data, size)
    if direction == "vert":
        if len(set([data.n for data in data_list])) > 1:
            # todo: "Error using horzcat\nDimensions of arrays being concatenated are not consistent."
            line = 0
            filename = 'test'
            error_statement = 'a="str"'
            temp = DimensionNotConsistentError(line, filename, error_statement)
            temp.modify_mess('horzcat')
            raise temp
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
        if class_a is not String:
            class_a = class_a.parent
            if class_a in b_ancestors:
                return class_a
            else:
                a_ancestors.add(class_a)
        if class_b is not String:
            class_b = class_b.parent
            if class_b in a_ancestors:
                return class_b
            else:
                b_ancestors.add(class_b)


def compat(a, b):
    """
    https://ww2.mathworks.cn/help/matlab/matlab_prog/compatible-array-sizes-for-basic-operations.html
    """
    if a.size == b.size:
        return

    if a.size[0] != b.size[0]:
        if a.size[0] == 1:
            a.expand_row(b.size[0])
        elif b.size[0] == 1:
            b.expand_row(a.size[0])
        else:
            # error
            pass
    if a.size[1] != b.size[1]:
        if a.size[1] == 1:
            a.expand_col(b.size[1])
        elif b.size[1] == 1:
            b.expand_col(a.size[1])
        else:
            # error
            pass
    return
