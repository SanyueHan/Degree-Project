from enum import Enum, auto


class DataClass(Enum):
    ARRAY = auto()
    LOGICAL = auto()
    STRING = auto()
    CHAR = auto()
    NUMERIC = auto()
    INTEGER = auto()
    S_INT_8 = auto()
    U_INT_8 = auto()
    S_INT_16 = auto()
    U_INT_16 = auto()
    S_INT_32 = auto()
    U_INT_32 = auto()
    S_INT_64 = auto()
    U_INT_64 = auto()
    FLOAT = auto()
    SINGLE = auto()
    DOUBLE = auto()
    TABLE = auto()
    CELL = auto()
    STRUCT = auto()
    SCALAR = auto()