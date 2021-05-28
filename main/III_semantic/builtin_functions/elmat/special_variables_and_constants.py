from main.III_semantic.builtin_functions.utils import *


def eps(argv):
    """
    %EPS  Spacing of floating point numbers.
    %   D = EPS(X), is the positive distance from ABS(X) to the next larger in
    %   magnitude floating point number of the same precision as X.
    %   X may be either double precision or single precision.
    %   For all X, EPS(X) is equal to EPS(ABS(X)).
    %
    %   EPS, with no arguments, is the distance from 1.0 to the next larger double
    %   precision number, that is EPS with no arguments returns 2^(-52).
    %
    %   EPS('double') is the same as EPS, or EPS(1.0).
    %   EPS('single') is the same as EPS(single(1.0)), or single(2^-23).
    %
    %   Except for numbers whose absolute value is smaller than REALMIN,
    %   if 2^E <= ABS(X) < 2^(E+1), then
    %      EPS(X) returns 2^(E-23) if ISA(X,'single')
    %      EPS(X) returns 2^(E-52) if ISA(X,'double')
    %
    %   For all X of class double such that ABS(X) <= REALMIN, EPS(X)
    %   returns 2^(-1074).   Similarly, for all X of class single such that
    %   ABS(X) <= REALMIN('single'), EPS(X) returns 2^(-149).
    %
    %   Replace expressions of the form
    %      if Y < EPS * ABS(X)
    %   with
    %      if Y < EPS(X)
    %
    %   Example return values from calling EPS with various inputs are
    %   presented in the table below:
    %
    %         Expression                   Return Value
    %        ===========================================
    %         eps(1/2)                     2^(-53)
    %         eps(1)                       2^(-52)
    %         eps(2)                       2^(-51)
    %         eps(realmax)                 2^971
    %         eps(0)                       2^(-1074)
    %         eps(realmin/2)               2^(-1074)
    %         eps(realmin/16)              2^(-1074)
    %         eps(Inf)                     NaN
    %         eps(NaN)                     NaN
    %        -------------------------------------------
    %         eps(single(1/2))             2^(-24)
    %         eps(single(1))               2^(-23)
    %         eps(single(2))               2^(-22)
    %         eps(realmax('single'))       2^104
    %         eps(single(0))               2^(-149)
    %         eps(realmin('single')/2)    2^(-149)
    %         eps(realmin('single')/16)   2^(-149)
    %         eps(single(Inf))             single(NaN)
    %         eps(single(NaN))             single(NaN)
    %
    %   See also REALMAX, REALMIN.
    """


def realmax(argv):
    """
    %REALMAX Largest finite floating point number.
    %   REALMAX returns the largest finite floating point number in IEEE double
    %   precision.
    %
    %   REALMAX('double') is the same as REALMAX.
    %
    %   REALMAX('single') returns the largest finite floating point number in
    %   IEEE single precision.
    %
    %   See also EPS, REALMIN, INTMAX.
    """


def realmin(argv):
    """
    %REALMIN Smallest positive normalized floating point number.
    %   REALMIN returns the smallest positive normalized floating point number
    %   in IEEE double precision.
    %
    %   REALMIN('double') is the same as REALMIN.
    %
    %   REALMIN('single') returns the smallest positive normalized floating
    %   point number in IEEE single precision.
    %
    %   See also EPS, REALMAX, INTMIN.
    """


def intmax(argv):
    """
    %INTMAX Largest positive integer value.
    %   X = INTMAX is the largest positive value representable in an int32.
    %   Any value that is larger than INTMAX will saturate to INTMAX when
    %   cast to int32.
    %
    %   INTMAX('int32') is the same as INTMAX with no arguments.
    %
    %   INTMAX(CLASSNAME) is the largest positive value in the integer class
    %   CLASSNAME. Valid values of CLASSNAME are 'int8', 'uint8', 'int16',
    %   'uint16', 'int32', 'uint32', 'int64' and 'uint64'.
    %
    %   See also INTMIN, REALMAX.
    """


def intmin(argv):
    """
    %INTMIN Smallest integer value.
    %   X = INTMIN is the smallest value representable in an int32.
    %   Any value that is smaller than INTMIN will saturate to INTMIN when
    %   cast to int32.
    %
    %   INTMIN('int32') is the same as INTMIN with no arguments.
    %
    %   INTMIN(CLASSNAME) is the smallest value in the integer class CLASSNAME.
    %   Valid values of CLASSNAME are 'int8', 'uint8', 'int16', 'uint16',
    %   'int32', 'uint32', 'int64' and 'uint64'.
    %
    %   See also INTMAX, REALMIN.
    """


def flintmax(argv):
    """
    %FLINTMAX Largest consecutive integer in floating point format.
    %   FLINTMAX returns the largest consecutive integer in IEEE double
    %   precision, which is 2^53. Above this value, double precision format
    %   does not have integer precision, and not all integers can be represented
    %   exactly.
    %
    %   FLINTMAX('double') is the same as FLINTMAX.
    %
    %   FLINTMAX('single') returns the largest consecutive integer in
    %   IEEE single precision, which is SINGLE(2^24).
    %
    %   See also EPS, REALMAX, INTMAX.
    """


def pi(argv):
    """
    %PI     3.1415926535897....
    %   PI = 4*atan(1) = imag(log(-1)) = 3.1415926535897....
    """
    return Double([3.141592653589793])


def inf(argv):
    """
    %INF Infinity.
    %   INF returns the IEEE arithmetic representation for positive
    %   infinity.  Infinity is also produced by operations like dividing by
    %   zero, eg. 1.0/0.0, or from overflow, eg. exp(1000).
    %
    %   INF('double') is the same as INF with no inputs.
    %
    %   INF('single') is the single precision representation of INF.
    %
    %   INF(N) is an N-by-N matrix of INFs.
    %
    %   INF(M,N) or INF([M,N]) is an M-by-N matrix of INFs.
    %
    %   INF(M,N,P,...) or INF([M,N,P,...]) is an M-by-N-by-P-by-... array of INFs.
    %
    %   INF(..., CLASSNAME) is an array of INFs of class specified by the
    %   string CLASSNAME. CLASSNAME can be either 'single' or 'double'.
    %
    %   INF(..., 'like', Y) is an array of INFs with the same data type, sparsity,
    %   and complexity (real or complex) as the single or double precision numeric
    %   variable Y.
    %
    %   Note: The size inputs M, N, and P... should be nonnegative integers.
    %   Negative integers are treated as 0.
    %
    %   See also NAN, ISINF, ISFINITE, ISFLOAT.
    """
    fun = creator_function_generator(float('inf'))
    return fun(argv)


def nan(argv):
    """
    %NaN    Not-a-Number.
    %   NaN is the IEEE arithmetic representation for Not-a-Number.
    %   A NaN is obtained as a result of mathematically undefined
    %   operations like 0.0/0.0  and inf-inf.
    %
    %   NaN('double') is the same as NaN with no inputs.
    %
    %   NaN('single') is the single precision representation of NaN.
    %
    %   NaN(N) is an N-by-N matrix of NaNs.
    %
    %   NaN(M,N) or NaN([M,N]) is an M-by-N matrix of NaNs.
    %
    %   NaN(M,N,P,...) or NaN([M,N,P,...]) is an M-by-N-by-P-by-... array of NaNs.
    %
    %   NaN(..., CLASSNAME) is an array of NaNs of class specified by the
    %   string CLASSNAME. CLASSNAME can be either 'single' or 'double'.
    %
    %   NaN(..., 'like', Y) is an array of NaNs with the same data type, sparsity,
    %   and complexity (real or complex) as the single or double precision numeric
    %   variable Y.
    %
    %   Note: The size inputs M, N, and P... should be nonnegative integers.
    %   Negative integers are treated as 0.
    %
    %   See also INF, ISNAN, ISFINITE, ISFLOAT.
    """
    fun = creator_function_generator(float('nan'))
    return fun(argv)


def isnan(argv):
    """
    %ISNAN  True for Not-a-Number.
    %   ISNAN(X) returns an array that contains 1's where
    %   the elements of X are NaN's and 0's where they are not.
    %   For example, ISNAN([pi NaN Inf -Inf]) is [0 1 0 0].
    %
    %   See also ISFINITE, ISINF, ISMISSING.
    """


def isinf(argv):
    """
    %ISINF  True for infinite elements.
    %   ISINF(X) returns an array that contains 1's where the
    %   elements of X are +Inf or -Inf and 0's where they are not.
    %   For example, ISINF([pi NaN Inf -Inf]) is [0 0 1 1].
    %
    %   See also ISFINITE, ISNAN.
    """


def isfinite(argv):
    """
    %ISFINITE True for finite elements.
    %   ISFINITE(X) returns an array that contains 1's where
    %   the elements of X are finite and 0's where they are not.
    %   For example, ISFINITE([pi NaN Inf -Inf]) is [1 0 0 0].
    %
    %   For any X, exactly one of ISFINITE(X), ISINF(X), or ISNAN(X)
    %   is 1 for each element.
    %
    %   See also ISNAN, ISINF.
    """


def true(argv):
    """
    %TRUE   True array.
    %   TRUE is short-hand for logical(1).
    %   TRUE(N) is an N-by-N matrix of logical ones.
    %   TRUE(M,N) or TRUE([M,N]) is an M-by-N matrix of logical ones.
    %   TRUE(M,N,P,...) or TRUE([M N P ...]) is an M-by-N-by-P-by-...
    %   array of logical ones.
    %   TRUE(SIZE(A)) is the same size as A and all logical ones.
    %   TRUE(..., 'like', Y) is an array of logical ones with the same data type
    %   and sparsity as the logical array Y.
    %
    %   TRUE(N) is much faster and more memory efficient than LOGICAL(ONES(N)).
    %
    %   Note: The size inputs M, N, and P... should be nonnegative integers.
    %   Negative integers are treated as 0.
    %
    %   See also FALSE, LOGICAL.
    """
    fun = creator_function_generator(Logical([true]))
    return fun(argv)


def false(argv):
    """
    %FALSE  False array.
    %   FALSE is short-hand for logical(0).
    %   FALSE(N) is an N-by-N matrix of logical zeros.
    %   FALSE(M,N) or FALSE([M,N]) is an M-by-N matrix of logical zeros.
    %   FALSE(M,N,P,...) or FALSE([M N P ...]) is an M-by-N-by-P-by-...
    %   array of logical zeros.
    %   FALSE(SIZE(A)) is the same size as A and all logical zeros.
    %   FALSE(..., 'like', Y) is an array of logical zeros with the same data type
    %   and sparsity as the logical array Y.
    %
    %   FALSE(N) is much faster and more memory efficient than LOGICAL(ZEROS(N)).
    %
    %   Note: The size inputs M, N, and P... should be nonnegative integers.
    %   Negative integers are treated as 0.
    %
    %   See also TRUE, LOGICAL.
    """
    fun = creator_function_generator(Logical([false]))
    return fun(argv)
