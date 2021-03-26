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
    - '>=' 
    - '>'
    - '<='
    - '<'
    - '=='
    - '~='
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
  - selection statement
    - if
    - elseif
    - else
  - iteration statement
    - while

## Run
#### Environment
Python (with the version no lower than 3.7), 
no third-party package needed up to now
#### Command
###### Mac OS
```shell
python3 MATLAB.py [-h] [-t T] [-a A] [-v V] [file]
```
###### Windows
```shell
python MATLAB.py [-h] [-t T] [-a A] [-v V] [file]
```

## Examples
#### Show Help Information
```shell
 % python3 MATLAB.py -h
usage: MATLAB.py [-h] [-t T] [-a A] [-v V] [file]

positional arguments:
  file         program read from script file

optional arguments:
  -h, --help   show this help message and exit
  -t T, --t T  print tokens
  -a A, --a A  print abstract syntax tree
  -v V, --v V  print variables
```
#### REPL Execute (Interactive Execute)
```
% python3 MATLAB.py
>> 1 & 0 | 1 == 2 < 5 + 5

ans =

  logical

   1

>> --++--+-123*45++--++-+-ans

ans =

       -5534

>> a = 1+2; b = 3+4;
>> c = a*b, d = a/b

c =

     21


d =

     0.4286

>> if a < 10 a, end

a =

     3

>> while b < 10 b = b + 1, end

b =

     8


b =

     9


b =

     10

>> 1:5

ans =

     1     2     3     4     5

>> for a = 1:2:10 a, end

a =

     1


a =

     3


a =

     5


a =

     7


a =

     9

>> 
```

#### Script Execute (Show Abstract Syntax Tree)
```
% python3 MATLAB.py test_cases/test_while.m -a=True

STMT_LIST: None
  ├── ASS_STMT: None
  │     ├── ASS_EXP: '='
  │     │     ├── ID: 'a'
  │     │     └── NUM_LIT: '0'
  │     └── EO_STMT: ';'
  └── ITR_STMT: None
        ├── ITR_CLS: 'while'
        │     ├── BSO_EXP: '<'
        │     │     ├── ID: 'a'
        │     │     └── NUM_LIT: '10'
        │     └── STMT_LIST: None
        │           ├── EXP_STMT: None
        │           │     ├── ID: 'a'
        │           │     └── EO_STMT: '\n'
        │           └── ASS_STMT: None
        │                 ├── ASS_EXP: '='
        │                 │     ├── ID: 'a'
        │                 │     └── BSO_EXP: '+'
        │                 │           ├── ID: 'a'
        │                 │           └── NUM_LIT: '1'
        │                 └── EO_STMT: ';'
        └── EO_STMT: '\n'


a =

     0


a =

     1


a =

     2


a =

     3


a =

     4


a =

     5


a =

     6


a =

     7


a =

     8


a =

     9

```