# An alternative to MATLAB - implement MATLAB in Python


## 0 Abstract
[MATLAB](https://en.wikipedia.org/wiki/MATLAB) as an abbreviation of "matrix laboratory", 
stands for the programming languages as well as its software implementation
who is officially defined and released by the [MathWorks Corporation](https://www.mathworks.com/). 
The purpose of this project is to implement a subset of the MATLAB programming language using python, 
that is as similar as possible with the official software, specially MATLAB_R2021a, 
in terms of text outputs, from a normal user perspective. 
The aim of this project is to learn the technologies and tools in compiling, 
in order to understand the principles of interpreters and compilers from a language designer's view, 
and gain a deeper insight in the nature of programming languages. 
There are two main approaches used when developing this project. 
The first one is to read the explanation in the [official documentation](https://ww2.mathworks.cn/help/matlab/) in order to understand the designed behavior of different syntax, 
and the second one is to run some experimental code on the MATLAB software and then watch their results. 
In other words, like reverse engineering, some detailed features are simulated by inferring the internal design of the official software, 
and then finding some equivalent ways in python, when the documentation is not elaborate enough. 
The achievements of this project including the realization of most operators, a number of statements, different data types, 
as well as some matrix operations and built-in functions which are considered as an important advantage for MATLAB. 
As an important functionality for interpreters/compilers, 
our interpreter also implemented error handling to report different kinds of errors detected, when the input code have bugs. 
Additionally, we have an elaborate designed test module that is capable of testing all the features mentioned above, 
using manually designed test cases as well as auto-generated scripts. 




## 1 Introduction
### (what is an interpreter and what is a compiler)
- （从原理和工作方式上介绍一下解释器与编译器的的异同）
- （解释器与编译器的优势与缺点）
The machine-language target program produced by a compiler is usually much faster than an interpreter at mapping inputs into outputs. 
An interpreter, however, can usually give better error diagnostics than a compiler, because it executes the program statement by statement. [Compiler P2]

### why choose matlab as the language
- interpreted language, easy to implement
- convenient to do auto random input test

### the structure of this project

### the structure of this thesis


## 2 Literature Review
- How modern interpreter/Compiler are designed

## 3 Work Division between Group Members
- HSY：词法分析，语法分析，解释执行
- ZY：编译执行，错误处理，内置函数
- HTT：单元测试，数据类型，矩阵运算

## 4 Individual Job Description
### HSY
### ZY
### HTT

## 5 Overall Discussion and Conclusions. 
和官方matlab软件相比：
- 功能实现的局限性
  - 只有四种基本数据类型
  - 只有一点内置函数
  - 没有高维数组
- 错误处理的局限性
  - 鲁棒性有限
- 软件性能的局限性
  - 性能比较图来两张
总结：最然如此但总体来说已经相当不错了，毕竟matlab是商业软件这是一个毕设项目  
    
Since MATLAB is a business software whose source code is not open to the public, 
it is impossible to 
know all the details of the technical realization of the official software/

Therefore, 

## 6 Suggestions for possible future work.
- unsolved bugs
  - 0 有符号问题
- planed upgrade features
  - 复数
  - 自定义函数
  - 面向对象及其他语法
  - 其他语法和命令
- optimization direction
  - speed
  - robustness
- research areas
  - compiler, machine code part

## References
