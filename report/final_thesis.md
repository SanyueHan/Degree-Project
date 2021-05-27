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
using manually designed test cases as well as auto-generated scripts, 
in order to demonstrate the correctness of the results produced by our product, or review bugs to repair. 


## 1 Introduction
Programming languages are notations for describing a flow of computational actions to people and to machines. 
However, according to their corresponding instructions sets, the CPUs only know how to execute machine code that is only consisted of 0s and 1s, 
not those higher level programming languages that we are familiar with, such as C, Java, or Python. 
Therefore, before a high level program can be run, it must be translated into a form in which it can be executed by a computer. 

There are two different ways to realize this. The first one is to use a compiler, 
that can read a program in one language and then translate it into an equivalent program in another language. 
If the target program is an executable machine-code program, it can then be called by the user to process inputs and produce outputs. 
Figure 1 shows how compilers work. 

![compiler](images/introduction_1.png)

The other kind of language processor is called interpreter. 
Instead of producing an executable target program as a translation, 
an interpreter directly execute the operations specified by the source program. 
Figure 2 shows the principle of an interpreter. 

![interpreter](images/introduction_2.png)

The advantage of a target program produced by a compiler over an interpreter at mapping inputs into outputs is its speed, 
while an interpreter can usually give better error diagnostics than a compiler, because it executes the program statement by statement.

To design an interpreter or a compiler, 
you can not only provide another version of software implementation for an existing programming language, 
but also create a new programming language whose syntax is defined by yourself. 
The reason why we choose to develop a MATLAB implementation and mimic all of its functionalities and features is that 
for an existing programming languages you can find its [grammar rules file](https://github.com/antlr/grammars-v4/blob/master/matlab/matlab.g4) written in normal form, 
which could be very helpful for novices like us who has no experience in developing interpreters or compilers. 
This will be explained in detail by Han Sanyue. 
Moreover, for an existing programming language, it is convenient for us to carry out tests, 
since we could execute the test scripts using the existing interpreter or compiler, and compare the results produced by it with that of ours, 
which involves with Hao Tingting's job. 
Additionally, MATLAB is an interpreted languages that is easy to realize comparing to those compiled languages such as C/C++, 
the reason will be explained in Zou Yang's individual part. 

In this thesis, we will firstly review the development history of interpreters and compilers, 
and also introduce the interpreter or compilers of some famous modern programming languages like C/C++, Java, Python in Section 2. 
Then we will explain the structure of our project and the work division between group members in sections 3. 
After that in section 4, there are our individual works. 
Section 5 contains overall discussion and conclusion, in which we will compare our product with the official MATLAB software, 
and discuss the advantages and disadvantages. 
Last but not least, we have summary some possible work direction on our project that is not yet finished due to the limitation of time. 


## 2 Literature Review
### 2.1 The development of compilers
Complex and ubiquitous software architectures underpin the global economy [13]. Compilers and high-level languages are the cornerstones of such software. In addition, powerful and elegant compilation technology also has an extremely important value in hardware synthesis and other fields. Compilers and high-level languages are central to the information age as semiconductor technology [24].

By far, the most striking achievement in the compiler field is the widespread use of high-level languages [16]. From banking and enterprise management software to high-performance computing and various World Wide Web (Web) applications, the vast majority of today's software is written in high-level languages and compiled statically or dynamically [17].

The first practical computer compiler, written for the A-0 system in 1952 by American female computer scientist Grace Murray Hopper on UNIVAC I, compiled programs into machine code [38]. However, its function was much closer to what we now know as a linker or loader. The compiler loads punched cards that carry programs written in human languages into the computer. The computer spits out another set of cards containing machine code. The second set of cards is loaded into the computer, and the computer can execute the new program. In response to the shortcomings of assembly language, Fortran, led in 1957 by John Warner Backus, an American computer scientist working for IBM, was the first fully functional high-level language compiler implemented [33].

In the 1950s, the field of the compiler was beginning, and scientists' research focus was limited to the conversion from high-level languages to machine code and the time and space requirements of optimizing programs [51]. Since then, much new knowledge has emerged in program analysis and transformation, code automation, and runtime services. At the same time, compilation algorithms are also used to facilitate software and hardware development, improve application performance, detect or avoid software defects and malware. At the same time, the field of compilation is increasingly intersecting with other areas such as computer architecture.

Object-oriented and data abstraction languages were first introduced in the late 1960s and early 1970s, and it was realized that these concepts could greatly improve programmer productivity. Computer architects and compiler writers first began to consider the static and dynamic optimizations invented in the field of parallelism compilers, seeing parallelism as a promising solution to the problem of computers not being fast enough. Instruct level parallelism was introduced in Seymour Cray's CDC 6600 and CDC 7600 and IBM System/360 Model 91. The compiler front end greatly benefited from developing systematic theories based on the automata theory of lexical, syntactic analysis techniques [60].

In the 1970s, CRAY-1 became the world's first commercially successful supercomputer [39], and the success of the CRAY machine was largely due to the introduction of the vector register. Like scalar registers, vector registers allow programs to perform many small data vectors [69]. Cray Research has also developed a very aggressive vectorization compiler. It is similar in many ways to the earlier TI compilers, but the Cray compiler has some features that make it very interesting. One of the most important features is that the ability to provide compiler feedback to the programmer. Many projects have focused on the automatic generation of other parts of the compiler, including code generation. In short, the Cray programmers finally achieved the three goals of performance, productivity, and portability.

In the early stage of developing a high-level language compiler, the technology is not mature enough, and the generated target code is large, the execution efficiency is low. These problems affect the promotion and application of high-level language. Cocke(1976) made an in-depth study of compiler code generation technology and put forward a series of optimization methods[40]. For example, the program integration, loop conversion, the elimination of common subexpressions, code movement, register positioning, storage unit reuse, so that the quality of the compiler has been greatly improved. The development of compilation technology reached a new stage [62].

In the 1990s, the messaging library was replaced by the Messaging Interface (MPI), and all those vendor-specific parallelization instructions were replaced by OpenMP. More scalable parallel systems emerged, such as Thinking Machines CM-5 and others with thousands of commercial microprocessors. SIMD instruction sets for single-chip microprocessors are on the market, and there is growing interest in redirectable compilers with SIMD support [13], such as SSE and SSE2 from Intel. 

Shortly after 2000, multi-core microprocessors began to be widely offered by many vendors. Compilers include applications for more complex algorithms that are used to infer or simplify information in programs. Compilers are increasingly a part of window-based interactive development environments. They include editors, linkers, debuggers, and project managers.

Compared to earlier compiler implementations, today's compilation algorithms are significantly more complex. While early compilers used simple and intuitive techniques for lexing programs, today's lexing techniques are based on formal languages and automata theory, making the compiler front end more systematic [19]. Similarly, the reconfigurable compiler work that used simple and intuitive techniques for dependency analysis and loop transformation today uses powerful algorithms based on integer linear programming.

Despite all the advances in compiler technology, some people still see compilers as more of a problem than a solution. They want the predictability that comes from the compiler, rather than the advanced analysis and code transcoding that optimizes the compiler in the background.

### 2.2 The development of Interpreters
A compiled language means that after we write a program, we translate the code into a binary file and execute the program by executing the binary file. Interpreted languages, on the other hand, do not convert binaries but compile them when needed. The interpreter includes a compilation process, but this compilation process does not generate object code. A Python interpreter consists of a compiler that converts source code into bytecode, which is then executed line by line through the Python virtual machine and a virtual organization. When we write Python code, we get a text file with an a.py extension that contains Python code. To run the code, a Python interpreter is required to implement Python files. In 1989, Guido began writing a compiler for the Python language; In 1991, the first Python compiler was created. It is implemented in C and can call C library files. Python already had classes, functions, exception handling, core data types including tables and dictionaries, and a module-based extension system. Since then, Python has been updated, with the current version being Python 3.8 (Figure 1). In summary, Python 2.x is legacy; Python 3.x is the present and future of the language.

![Python Interpreter Development](images/literature_review_1.png)

### 2.3 Interpreters & compilers for popular modern programming language
Here are principle of how modern programming language processors are realized. 
Some of them belongs to interpreter, like Python, 
Some of them belongs to compiler, like C/C++, 
while there is also some kinds of language whose execution go through both a stage of compile and a stage of interpret, like Java. 

#### 2.3.1 Python interpreters
There are some popular python interpreters: CPython, Jython, IronPython, and Pypy. 
1. CPython is a reference implementation written in C and is the most widely used Python interpreter. 
2. IPython is an interactive interpreter based on CPython. In other words, IPython is only enhanced in terms of interaction, but executing Python code is the same as that of CPython. 
3. Jython and IronPython are alternative implementations of Python interpreters targeting the Java virtual machine and The.net frameworks, but they typically do not improve performance [16].
4. Pypy is another Python interpreter, and Pypy is the most outstanding effort to develop an alternative interpreter to improve Python's execution speed. Its goal is the speed of execution. Pypy uses JIT technology to dynamically compile Python code (note that it is not interpreted), so it can significantly improve the execution speed of Python code [10].

#### 2.3.2 C/C++ compilers
Visual C++ is the most popular compiler on the Windows platform which integrates well with VS and has good compilation efficiency and compiled code efficiency. GCC/G+ is the preferred option on Linux/ UNIX platforms and supports N component platforms.

#### 2.3.3 Java Virtual Machine
For Java, the compiler compiles the Java source files (.java files) into bytecode files (.class files), which are binary. This bytecode is the "machine language" of the JVM (a virtual machine capable of running Java bytecode). Javac.exe can be thought of simply as a Java compiler. The Java interpreter is part of the JVM. The Java interpreter is used to interpret programs that have been compiled by executing the Java compiler. Java.exe can be thought of simply as a Java interpreter. The JVM interprets the execution of a bytecode file as the JVM manipulates the Java interpreter to interpret the execution of a bytecode file. The JVM masks information specific to a specific operating system, allowing Java programs to run unchanged on multiple platforms by generating only the object code (bytecode) that runs on the Java Virtual Machine.

## 3 Work Division
### 3.1 The Structure of Interpreter/Compiler
If we look into the working process of interpreters or compilers in detail, 
we could find that they operate as a sequence of stages, 
each of which transform one representation of the original program into another. 
A typical decomposition is shown in Figure 3. 

![stages of compiler](images/work_division_1.png)

In this flow chart here are seven steps in total. 
The three steps above, namely lexical analysis, syntax analysis, and semantic analysis, 
are usually regarded as the front end, which is responsible for analyse the source program by breaking it up into constituent pieces, 
create an **abstract syntax tree** to represent it, and report the problem properly when bugs are detected. 
To develop an interpreter we only need to implement these three parts. 
The four steps below, namely intermediate code generation, intermediate code generation, machine code generation, and machine code optimization, 
are usually regarded as the back end, which is responsible for synthesis the target program, using the information provided by the front end. 
To develop a compiler, the back end is also necessary. 

### 3.2 Work Division
Since there are three members in our group, we firstly divided the work as following: 
Han Sanyue is responsible for the three stages in the front end, so that an interpreter could work properly. 
Zou Yang is responsible for the four stages in the back, combining the achievements of front end to form a compiler. 
Hao Tingting undertakes the work of testing, including both testing on individual modules and testing the total product,
to ensure that the interpreter or compiler will not only produce right results for correct code, but also report proper error for buggy codes. 

However, with the progression of the project, we reached an agreement that the back end is more difficult than the front end. 
One reason is that the person responsible for the back end need to understand the results provided by the front end, 
before starting his own part, and if the front end go through a refactor that change something, 
such as the structure of the abstract syntax tree, the back end also need to be adjusted accordingly. 
Another reason is that using interpreter the script code could run on any platform 
as long as the language in which the interpreter is written could run on that platform, 
for example python has different release versions on Windows, macOS, and Linux, 
but for compiler the target program is directly executed by the CPU, 
so the back end involves dealing with different instruction set on different platform. 
Since it's seem to be difficult for Zou Yang to finish the back end perfectly, 
our group decided to reassign the job involving with reporting error in the interpreter part to Zou Yang. 

### 3.3 Structure of the project
The structure of our final project is shown in Figure 4, in which the responsibility of different members are labeled accordingly. 

![structure of project](images/work_division_2.png)

## 4 Individual Job Description
### 4.1 Han Sanyue's Individual Part
#### 4.1.1 Introduction
As mentioned earlier, my main work involves with realize the three phrases in front end, 
namely lexical analysis, syntax analysis, and semantic analysis, in other words the modules an interpreter needed. 
when a source program is passed into the interpreter, it w
#### 4.1.2 Lexical Analysis
#### 4.1.3 Syntax Analysis
#### 4.1.4 Semantic Analysis
#### 4.1.5 Conclusion
### 4.2 Zou Yang's Individual Part
### 4.3 Hao Tingting's Individual Part

## 5 Overall Discussion and Conclusions. 
Comparing to official matlab software
- limitation on functionalities
  - only have four most basic data types
  - only a few built-in functions
  - only support two-dimensional array, not higher
- limitation on error handling
  - not robust enough
- limitation on performance
  - use figure to demonstrate
    
Since MATLAB is a business software which is developed by professional engineers for years,
it is impossible to produce a comparable product in a Degree Project. 
However, ...
Therefore, ...

## 6 Suggestions for possible future work.
- unsolved bugs
  - signed zero problem
- planed upgrade features
  - complex number
  - function definition syntax
  - object-oriented programming
  - other syntax and command
- optimization direction
  - speed
  - robustness
- research areas
  - compiler, machine code part

## References
