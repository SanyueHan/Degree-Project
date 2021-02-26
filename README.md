# A Python implemented MATLAB code interpreter

## Description
This is a Python implemented interpreter, 
supporting a subset of the functionalities of MATLAB, 
including: 
- Four basic arithmetic calculations
- Variable assignment

## Run
### Environment
Only Python 3.8, no third-party package needed up to now

### REPL Execute
#### Commands
###### Mac OS
```shell
python3 repl_execuate.py
```
###### Windows
```shell
python repl_execuate.py
```
#### Example
```shell
>> a = 1+2

a =

     3

>> b = 3-4

b =

     -1

>> c = 5*6

c =

     30

>> d = 7/8

d =

     0.8750

>> (a+b)*(c+d)

ans =

     61.7500

>> ans - 60

ans =

     1.7500

>> 
```

### Script Execute
#### Commands
###### Mac OS
```shell
python3 script_execute.py <test_script_dir>
```
###### Windows
```shell
python script_execute.py <test_script_dir>
```
The <test_script_dir> argument is optional, 
if not specified, 
the default script would be "test_cases/test_exp_ass.m" at present. 
