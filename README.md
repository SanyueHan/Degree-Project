# A Python implemented MATLAB code interpreter

## Description
This is a Python implemented interpreter, 
supporting a subset of the functionalities of MATLAB, 
including: 
- Four basic arithmetic calculations
- Integer declaration
- Integer assignment

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
/usr/local/bin/python3.8 /Users/hansanyue/Desktop/Degree-Project/repl_execute.py
>> a = 1+2

a =

     3

>> b = 3*4

b =

     12

>> c = a + b * 2 + 3 * (4 + 5) * 6

c =

     189

>> quit()

Process finished with exit code 0
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
