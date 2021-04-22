## User's Manual - Testing Guidelines

### 0 Get Started with MATLAB

### 1 Language Fundamentals
#### 1.1 Entering Commands
#### 1.2 Matrices and Arrays
#### 1.2 Data Types
#### 1.4 Operators and Elementary Operations
##### 1.4.1 Arithmetic Operations
[arithmetic operation example](test_interpreter/test_cases/language_fundamentals/iv_operators_and_elementary_operations/test_1_arithmetic_operations.m)
###### 1.4.1.1 Basic Arithmetic
- Addition
  - "+"
- Subtraction
  - "-"
- Multiplication
  - ".*"
  - "*"
- Division
  - "./"
  - ".\\"
  - "/"
  - "\\"
- Powers
- Transpose
  - ".'"
  - "'"
- Array Sign
  - "-"
  - "+"
###### 1.4.1.2 Modulo Division and Rounding
###### 1.4.1.3 Custom Binary Functions
##### 1.4.2 Relational Operations
[relational operation example](test_interpreter/test_cases/language_fundamentals/iv_operators_and_elementary_operations/test_2_relational_operations.m)
- "=="
- ">="
- ">"
- "<="
- "<"
- "~="
##### 1.4.3 Logical Operations
[logical operation example](test_interpreter/test_cases/language_fundamentals/iv_operators_and_elementary_operations/test_3_logical_operations.m)
- "&&"
- "||"
- "~"
##### 1.4.4 Set Operations
##### 1.4.5 Bit-Wise Operations
#### 1.5 Loops and Conditional Statements
- if, elseif, else  
  [if example](test_interpreter/test_cases/language_fundamentals/v_loops_and_conditional_statements/test_if_else.m)
- switch, case, otherwise  
  [switch example](test_interpreter/test_cases/language_fundamentals/v_loops_and_conditional_statements/test_switch_case.m)
- for  
  [for example](test_interpreter/test_cases/language_fundamentals/v_loops_and_conditional_statements/test_for.m)
- while  
  [while example](test_interpreter/test_cases/language_fundamentals/v_loops_and_conditional_statements/test_while.m)

### 2 Error Handling
#### 2.1 Lexical Error
- InvalidCharacterError
- StringTerminationError(InterpretException)
- CharacterVectorTerminationError(InterpretException)
#### 2.2 Syntax Error

#### 2.3 Semantic Error