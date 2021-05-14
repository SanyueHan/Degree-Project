from main.builtin_functions.elmat.special_variables_and_constants import *


ELEMENTARY_MATRICES = {
    'zeros': None,
    'ones': None,
    'eye': None,
    'repmat': None,
    'repelem': None,
    'linspace': None,
    'logspace': None,
    'freqspace': None,
    'meshgrid': None,
    'accumarray': None
}


BASIC_ARRAY_INFORMATION = {
    'size': None,
    'length': None,
    'ndims': None,
    'numel': None,
    'disp': None,
    'isempty': None,
    'isequal': None,
    'isequaln': None,
    'height': None,
    'width': None
}


MATRIX_MANIPULATION = {
    'cat': None,
    'reshape': None,
    'diag': None,
    'blkdiag': None,
    'tril': None,
    'triu': None,
    'fliplr': None,
    'flipud': None,
    'flip': None,
    'rot90': None,
    'find': None,
    'end': None,
    'sub2ind': None,
    'ind2sub': None,
    'bsxfun': None
}


MULTI_DIMENSIONAL_ARRAY_FUNCTIONS = {
    'ndgrid': None,
    'permute': None,
    'ipermute': None,
    'shiftdim': None,
    'circshift': None,
    'squeeze': None
}


ARRAY_UTILITY_FUNCTIONS = {
    'isscalar': None,
    'isvector': None,
    'isrow': None,
    'iscolumn': None,
    'ismatrix': None
}


SPECIAL_VARIABLES_AND_CONSTANTS = {
    'eps': None,
    'realmax': None,
    'intmax': None,
    'intmin': None,
    'flintmax': None,
    'pi': pi,
    'i': None,
    'inf': inf,
    'Inf': inf,
    'nan': nan,
    'Nan': nan,
    'isnan': isnan,
    'isinf': isinf,
    'isfinite': isfinite,
    'j': None,
    'true': true,
    'false': false,
}


SPECIALIZED_MATRICES = {
    'compan': None,
    'gallery': None,
    'hadamard': None,
    'hankel': None,
    'hilb': None,
    'invhilb': None,
    'magic': None,
    'pascal': None,
    'rosser': None,
    'toeplitz': None,
    'vander': None,
    'wilkinson': None
}


ELEMENTARY = {
    **ELEMENTARY_MATRICES,
    **BASIC_ARRAY_INFORMATION,
    **MATRIX_MANIPULATION,
    **MULTI_DIMENSIONAL_ARRAY_FUNCTIONS,
    **ARRAY_UTILITY_FUNCTIONS,
    **SPECIAL_VARIABLES_AND_CONSTANTS,
    **SPECIALIZED_MATRICES
}


MATLAB = {
    **ELEMENTARY,
}
