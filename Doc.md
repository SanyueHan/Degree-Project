# Technical Documentation - Testing Guidelines

## Language Fundamentals
### Entering Commands
### Matrices and Arrays
### Data Types
### Operators and Elementary Operations
#### Arithmetic Operations
[arithmetic operation example](test_interpreter/test_cases/language_fundamentals/iv_operators_and_elementary_operations/test_1_arithmetic_operations.m)
###### Basic Arithmetic
1. Addition
   - "+"
2. Subtraction
   - "-"
3. Multiplication
   - ".*"
4. Division
   - "./"
   - ".\\"
   - "/"
   - "\\"
5. Powers
6. Transpose
   - ".'"
   - "'" 
7. Array Sign
   - "-"
   - "+" 
###### Modulo Division and Rounding
###### Custom Binary Functions
#### Relational Operations
[relational operation example](test_interpreter/test_cases/language_fundamentals/iv_operators_and_elementary_operations/test_2_relational_operations.m)
- "=="
- ">="
- ">"
- "<="
- "<"
- "~="
#### Logical Operations
[logical operation example](test_interpreter/test_cases/language_fundamentals/iv_operators_and_elementary_operations/test_3_logical_operations.m)
- "&&"
- "||"
- "&"
- "~"
- "|"
#### Set Operations
#### Bit-Wise Operations
### Loops and Conditional Statements
- if, elseif, else  
  [if example](test_interpreter/test_cases/language_fundamentals/v_loops_and_conditional_statements/test_if_else.m)
- switch, case, otherwise  
  [switch example](test_interpreter/test_cases/language_fundamentals/v_loops_and_conditional_statements/test_switch_case.m)
- for  
  [for example](test_interpreter/test_cases/language_fundamentals/v_loops_and_conditional_statements/test_for.m)
- while  
  [while example](test_interpreter/test_cases/language_fundamentals/v_loops_and_conditional_statements/test_while.m)

## Error Handling
#### Lexical Error
- InvalidCharacterError
- StringTerminationError(InterpretException)
- CharacterVectorTerminationError(InterpretException)
#### Syntax Error
#### Semantic Error