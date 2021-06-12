## Manual - Testing Guidelines

### [0 Get Started with MATLAB](https://ww2.mathworks.cn/help/matlab/getting-started-with-matlab.html?s_tid=CRUX_lftnav)

### [1 Language Fundamentals](https://ww2.mathworks.cn/help/matlab/language-fundamentals.html?s_tid=CRUX_lftnav)
#### [1.1 Entering Commands](https://ww2.mathworks.cn/help/matlab/entering-commands.html?s_tid=CRUX_lftnav)
#### [1.2 Matrices and Arrays](https://ww2.mathworks.cn/help/matlab/matrices-and-arrays.html?s_tid=CRUX_lftnav)
- Functions
  - Create and Combine Arrays
  - Create Grids
  - Determine Size, Shape, and Order
  - Reshape and Rearrange
  - indexing
- Topics
  - Creating, Concatenating, and Expanding Matrices
  - Array Indexing
  - Removing Rows or Columns from a Matrix
  - Reshaping and Rearranging Arrays
  - Multidimensional Arrays
#### [1.3 Data Types](https://ww2.mathworks.cn/help/matlab/data-types.html?s_tid=CRUX_lftnav)
#### [1.4 Operators and Elementary Operations](https://ww2.mathworks.cn/help/matlab/operators-and-elementary-operations.html?s_tid=CRUX_lftnav)
- Operator Basics
  - [Array vs. Matrix Operations](https://ww2.mathworks.cn/help/matlab/matlab_prog/array-vs-matrix-operations.html)
  - [Compatible Array Sizes for Basic Operations](https://ww2.mathworks.cn/help/matlab/matlab_prog/compatible-array-sizes-for-basic-operations.html)
##### [1.4.1 Arithmetic Operations](https://ww2.mathworks.cn/help/matlab/arithmetic-operators.html)
[examples in auto-generated test cases](test_interpreter/test_cases/language_fundamentals/iv_operators_and_elementary_operations/test_1_arithmetic_operations.m)
- Basic Arithmetic
  - Addition
    - +
  - Subtraction
    - -
  - Multiplication
    - .*
    - *
  - Division
    - ./
    - .\\
    - /
    - \\
  - Powers
    - .^
    - ^
  - Transpose
    - .'
    - '
  - Array Sign
    - \-
    - \+
- Modulo Division and Rounding
- Custom Binary Functions
##### [1.4.2 Relational Operations](https://ww2.mathworks.cn/help/matlab/relational-operators.html)
- Functions
  - ==
  - \>=
  - \>
  - <=
  - <
  - ~=
  - [auto-generated test cases](test_interpreter/test_cases/language_fundamentals/iv_operators_and_elementary_operations/test_2_relational_operations.m)
- Topics
##### [1.4.3 Logical Operations](https://ww2.mathworks.cn/help/matlab/logical-operations.html)
- Functions
  - Short-circuit &&, ||
  - &
  - ~
  - |
  - [auto-generated test cases](test_interpreter/test_cases/language_fundamentals/iv_operators_and_elementary_operations/test_3_logical_operations.m)
- Topics
##### 1.4.4 Set Operations
##### 1.4.5 Bit-Wise Operations
#### [1.5 Loops and Conditional Statements](https://ww2.mathworks.cn/help/matlab/control-flow.html?s_tid=CRUX_lftnav)
- if, elseif, else  
  
- switch, case, otherwise  
  
- for  
  
- while  
  

### 2 Error Handling
- [Lexical Error](main/exceptions/i_lexical_exception.py)
  - InvalidCharacterError
    - [Case 1](test_interpreter/test_cases/error_handling/i_lexical_error/invalid_character_error/test_1.m)
    - [Case 2](test_interpreter/test_cases/error_handling/i_lexical_error/invalid_character_error/test_2.m)
    - [Case 3](test_interpreter/test_cases/error_handling/i_lexical_error/invalid_character_error/test_3.m)
  - StringTerminationError
    - [Case 1](test_interpreter/test_cases/error_handling/i_lexical_error/string_termination_error/test_1.m)
  - CharacterVectorTerminationError
    - [Case 1](test_interpreter/test_cases/error_handling/i_lexical_error/character_vector_termination_error/test_1.m)
- [Syntax Error](main/exceptions/ii_syntactic_exceptions.py)

- [Semantic Error](main/exceptions/iii_semantic_exceptions.py)