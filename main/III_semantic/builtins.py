from main.data_types.array_data.numeric_data.decimal_data.double import Double
from main.data_types.array_data.logical import Logical


BUILTINS = {
    'pi': Double([3.141592653589793]),
    'inf': Double([float('inf')]),
    'Inf': Double([float('inf')]),
    'nan': Double([float('nan')]),
    'NaN': Double([float('nan')]),
    'eps': Double([2.220446049250313e-16]),
    'true': Logical([True]),
    'false': Logical([False]),
}