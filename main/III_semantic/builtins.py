from main.III_semantic.built_in.elmat.special_variables_and_constants import *


ELEMENTARY_MATRICES = {

}


BASIC_ARRAY_INFORMATION = {

}


MATRIX_MANIPULATION = {

}


MULTI_DIMENSIONAL_ARRAY_FUNCTIONS = {

}


ARRAY_UTILITY_FUNCTIONS = {

}


SPECIAL_VARIABLES_AND_CONSTANTS = {
    'eps': eps,
    'realmax': realmax,
    'intmax': intmax,
    'intmin': intmin,
    'flintmax': flintmax,
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


BUILT_IN_FUNCTIONS = {
    **ELEMENTARY,
}
