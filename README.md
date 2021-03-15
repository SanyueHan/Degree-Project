# A Python implemented MATLAB code interpreter

## Description
This is a Python implemented interpreter, 
supporting a subset of the functionalities of MATLAB:
1. Operators supported including:
  - arithmetic operators: (left-associative)
    - '+'
    - '-'
    - '*'
    - '/'
  - relational operators: (left-associative)
    - '>+' 
    - '>'
    - '<='
    - '<'
    - '=='
    - '!='
  - logical operators: (left-associative)
    - '&' (logical and)
    - '|' (logical or)
  - unary operators: (right-associative)
    - '+' (positive)
    - '-' (negative)
    - '~' (logical not)
    
2. Statements supported including:
  - assignment statement
  - expression statement
  - clear statement

## Run
### Environment
Python (with the version no lower than 3.7), 
no third-party package needed up to now

### REPL Execute
#### Commands
###### Mac OS
```shell
python3 MATLAB.py
```
###### Windows
```shell
python MATLAB.py
```
#### Example
```
% python3 MATLAB.py
>> 1 & 0 | 1 == 2 < 5 + 5

ans =

     1

>> --++--+-123*45+ans

ans =

     -5534

>> a = 1+2; b = 3+4;
>> c = a*b, d = a/b

c =

     21


d =

     0.4286

>> 
```

### Script Execute
#### Commands
###### Mac OS
```shell
python3 MATLAB.py <script_dir>
```
###### Windows
```shell
python MATLAB.py <script_dir>
```
#### Example
```
% python3 MATLAB.py test_cases/test_exp_ass.m

ans =

     12.3400


ans =

     56


ans =

     0.7800


ans =

     2


ans =

     1


ans =

     20


ans =

     2


a =

     2


b =

     6

```