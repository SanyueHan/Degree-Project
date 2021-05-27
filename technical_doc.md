# Technical Documentation

## 1 Project Structure Overview
### 1.1 Interpreter
#### 1.1.0 [Program Entrance](MiniMATLAB.py)
#### 1.1.1 [Lexical Analysis](main/I_lexical)
#### 1.1.2 [Syntactic Analysis](main/II_syntactic)
Operator Precedence
01. Parentheses ()
02. Transpose (.'), power (.^), complex conjugate transpose ('), matrix power (^)
03. Power with unary minus (.^-), unary plus (.^+), or logical negation (.^~) as well as matrix power with unary minus (^-), unary plus (^+), or logical negation (^~).
04. Unary plus (+), unary minus (-), logical negation (~)
05. Multiplication (.*), right division (./), left division (.\), matrix multiplication (*), matrix right division (/), matrix left division (\)
06. Addition (+), subtraction (-)
07. Colon operator (:)
08. Less than (<), less than or equal to (<=), greater than (>), greater than or equal to (>=), equal to (==), not equal to (~=)
09. **Element-wise AND (&)**
10. **Element-wise OR (|)**
11. Short-circuit AND (&&)
12. Short-circuit OR (||)

```markdown
    stmt_list ::= stmt*

    stmt ::= ass_stmt | exp_stmt | clr_stmt | sel_stmt | itr_stmt | jmp_stmt | eo_stmt

    ass_stmt ::= ass_exp eo_stmt
    exp_stmt ::= cln_exp eo_stmt
    clr_stmt ::= 'clear' id_list eo_stmt
    sel_stmt ::= 'if' cln_exp stmt_list ('elseif' cln_exp stmt_list)* ('else' stmt_list)? 'end' eo_stmt
    itr_stmt ::= 'while' cln_exp stmt_list
    jmp_stmt ::=

    id_list ::= identifier*

    ass_exp ::= id '=' cln_exp
    cln_exp ::= lor_exp (':' lor_exp)*
    lor_exp ::= lan_exp (('||'|'|') lan_exp)*
    lan_exp ::= eql_exp (('&&'|'&') eql_exp)*
    eql_exp ::= rel_exp (('~='|'==') rel_exp)*
    rel_exp ::= add_exp (('<='|'<'|'>='|'>') add_exp)*
    add_exp ::= mul_exp (('+'|'-') mul_exp)*
    mul_exp ::= uny_exp (('*'|'/') uny_exp)*
    uny_exp ::= ('+'|'-'|'~')* pri_exp
    pri_exp ::= identifier | number_lit | string_lit | '('cln_exp')' | '[' array_list ']'

    identifier ::=
    number_lit ::=
    string_lit ::=
    array_list ::= (cln_exp exp_stmt*)*
```

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
