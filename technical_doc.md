# Technical Documentation

## 0 Abstract
This project provides an open-source implementation of a subset of the MATLAB programming language who's officially defined by the [MathWorks Corporation](https://www.mathworks.com/). 
Since MATLAB is a business software whose source code is not open to the public, it is impossible to know all the details of the technical realization of the official software. 
Therefore, the aim of this project is to provide an implementation 
that is as similar as possible as the official software, specially MATLAB_R2021a, 
in terms of text outputs, from a normal user perspective. 

There are two main approaches used when developing this project. 
The first one is to read the explanation in the [official documentation](https://ww2.mathworks.cn/help/matlab/), 
and the second one is to run some experimental code on the official MATLAB and then watch the results. 
In other words, like reverse engineering, this project implements similar features by inferring the internal realization of the official software, 
or finding some equivalent ways, within a limit range defined in the [user's manual](user_manual.md). 
If the input code exceeds the designed working range of this project, the behavior of the program is undefined, 
which means that any result could be possible: the interpreter may react correctly, or produce a wrong result, or stuck in infinite loop, or even crash. 
Therefore, to test the software, it is necessary to know exactly the designed working range illustrated in the manual. 

## 1 Project Structure Overview
### 1.1 Interpreter
#### 1.1.0 [Program Entrance](MiniMATLAB.py)
#### 1.1.1 [Lexical Analysis](main/I_lexical)
#### 1.1.2 [Syntactic Analysis](main/II_syntactic)
#### 1.1.3 [Semantic Analysis](main/III_semantic)
##### 1.1.3.1 Type System
###### 1.1.3.1.1 Type Inference
- Synthesized Attribute  
The attribute inferred from descendant nodes, 
such as arithmetic operation.
- Inherited Attribute  
The attribute decided by ancestor nodes or itself, 
such as variable declaration, logical operations
###### 1.1.3.1.2 Type Checking
- Assignment Statement  
Check whether the type on the right is same as the type on the left
- Initialization in Variable Declaration  
Check whether the type of the initial value is same as the specified type
- Transfer Arguments in Function Call  
Check whether the type of the arguments is same as the function's requirement
- Function Return  
Check whether the value returned has the same type as the function specified
###### 1.1.3.1.3 Type Conversion
##### 1.1.3.2 Scope and Lifetime
#### 1.1.4 [Data Types](main/data_types)
#### 1.1.5 [Exceptions](main/exceptions)
### 1.2 Testing
