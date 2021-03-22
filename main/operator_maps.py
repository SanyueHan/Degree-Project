from main.datatype.data.array_data.logical import Logical
from main.datatype.data.array_data.numeric_data.float_data.double import Double

BSO_MAP = {
    '|': (Logical, lambda x, y: x or y),
    '&': (Logical, lambda x, y: x and y),
    '==': (Logical, lambda x, y: x == y),
    '~=': (Logical, lambda x, y: x != y),
    '>=': (Logical, lambda x, y: x >= y),
    '>':  (Logical, lambda x, y: x > y),
    '<=': (Logical, lambda x, y: x <= y),
    '<':  (Logical, lambda x, y: x < y),
    '+': (Double, lambda x, y: x + y),
    '-': (Double, lambda x, y: x - y),
    '.*': (Double, lambda x, y: x * y),
    './': (Double, lambda x, y: x / y),
    '.\\': (Double, lambda x, y: y / x),
}

USO_MAP = {
    '+': (Double, lambda x: x),
    '-': (Double, lambda x: -x),
    '~': (Logical, lambda x: not x)
}
