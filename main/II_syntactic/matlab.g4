/*
BSD License
Copyright (c) 2013, Tom Everett
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
3. Neither the name of Tom Everett nor the names of its contributors
   may be used to endorse or promote products derived from this software
   without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/
/*
* Grammar based on yacc-keable for matlab by Danny Luk 12/1995
*
* http://www.angelfire.com/ar/CompiladoresUCSE/images/MATLAB.zip
*/

grammar matlab;

primary_expression // finished
   : IDENTIFIER
   | CONSTANT
   | STRING_LITERAL
   | '(' expression ')'
   | '[' ']'
   | '[' array_list ']'
   ;

postfix_expression // finished
   : primary_expression
   | array_expression
   | postfix_expression TRANSPOSE
   | postfix_expression NCTRANSPOSE
   ;

index_expression // finished
   : ':'
   | expression
   ;

index_expression_list // finished
   : index_expression
   | index_expression_list ',' index_expression
   ;

array_expression // finished
   : IDENTIFIER '(' index_expression_list ')'
   ;

unary_expression // finished
   : postfix_expression
   | unary_operator postfix_expression
   ;

unary_operator // finished
   : '+'
   | '-'
   | '~'
   ;

multiplicative_expression // finished
   : unary_expression
   | multiplicative_expression '*' unary_expression
   | multiplicative_expression '/' unary_expression
   | multiplicative_expression '\\' unary_expression
   | multiplicative_expression '^' unary_expression
   | multiplicative_expression ARRAYMUL unary_expression
   | multiplicative_expression ARRAYDIV unary_expression
   | multiplicative_expression ARRAYRDIV unary_expression
   | multiplicative_expression ARRAYPOW unary_expression
   ;

additive_expression // finished
   : multiplicative_expression
   | additive_expression '+' multiplicative_expression
   | additive_expression '-' multiplicative_expression
   ;

relational_expression // finished
   : additive_expression
   | relational_expression '<' additive_expression
   | relational_expression '>' additive_expression
   | relational_expression LE_OP additive_expression
   | relational_expression GE_OP additive_expression
   ;

equality_expression // finished
   : relational_expression
   | equality_expression EQ_OP relational_expression
   | equality_expression NE_OP relational_expression
   ;

and_expression // finished
   : equality_expression
   | and_expression '&' equality_expression
   ;

or_expression // finished
   : and_expression
   | or_expression '|' and_expression
   ;

expression // finished
   : or_expression
   | expression ':' or_expression
   ;

assignment_expression // finished
   : postfix_expression '=' expression
   ;

eostmt // finished
   : ','
   | ';'
   | CR
   ;

statement // finished
   : global_statement
   | clear_statement
   | assignment_statement
   | expression_statement
   | selection_statement
   | iteration_statement
   | jump_statement
   ;

statement_list // finished
   : statement
   | statement_list statement
   ;

identifier_list // finished
   : IDENTIFIER
   | identifier_list IDENTIFIER
   ;

global_statement
   : GLOBAL identifier_list eostmt
   ;

clear_statement // finished
   : CLEAR identifier_list eostmt
   ;

expression_statement // finished
   : eostmt
   | expression eostmt
   ;

assignment_statement // finished
   : assignment_expression eostmt
   ;

array_element // finished
   : expression
   | expression_statement
   ;

array_list // finished
   : array_element
   | array_list array_element
   ;

selection_statement // finished
   : IF expression statement_list END eostmt
   | IF expression statement_list ELSE statement_list END eostmt
   | IF expression statement_list elseif_clause END eostmt
   | IF expression statement_list elseif_clause ELSE statement_list END eostmt
   ;

elseif_clause // finished
   : ELSEIF expression statement_list
   | elseif_clause ELSEIF expression statement_list
   ;

iteration_statement // finished
   : WHILE expression statement_list END eostmt
   | FOR IDENTIFIER '=' expression statement_list END eostmt
   | FOR '(' IDENTIFIER '=' expression ')' statement_list END eostmt
   ;

jump_statement
   : BREAK eostmt
   | RETURN eostmt
   ;

translation_unit
   : statement_list
   | FUNCTION function_declare eostmt statement_list
   ;

func_ident_list
   : IDENTIFIER
   | func_ident_list ',' IDENTIFIER
   ;

func_return_list
   : IDENTIFIER
   | '[' func_ident_list ']'
   ;

function_declare_lhs
   : IDENTIFIER
   | IDENTIFIER '(' ')'
   | IDENTIFIER '(' func_ident_list ')'
   ;

function_declare
   : function_declare_lhs
   | func_return_list '=' function_declare_lhs
   ;


ARRAYMUL // finished
   : '.*'
   ;


ARRAYDIV // finished
   : '.\\'
   ;


ARRAYRDIV // finished
   : './'
   ;


ARRAYPOW
   : '.^'
   ;


BREAK
   : 'break'
   ;


RETURN
   : 'return'
   ;


FUNCTION
   : 'function'
   ;


FOR // finished
   : 'for'
   ;


WHILE // finished
   : 'while'
   ;


END // finished
   : 'end'
   ;


GLOBAL
   : 'global'
   ;


IF // finished
   : 'if'
   ;


CLEAR // finished
   : 'clear'
   ;


ELSE // finished
   : 'else'
   ;


ELSEIF // finished
   : 'elseif'
   ;


LE_OP // finished
   : '<='
   ;


GE_OP // finished
   : '>='
   ;


EQ_OP // finished
   : '=='
   ;


NE_OP // finished
   : '~='
   ;


TRANSPOSE // finished
   : 'transpose'
   ;


NCTRANSPOSE // finished
   : '.\''
   ;


STRING_LITERAL // finished
   : '\'' ( ~ '\'' | '\'\'' ) * '\''
   ;


IDENTIFIER // finished
   : [a-zA-Z] [a-zA-Z0-9_]*
   ;


CONSTANT // finished
   : NUMBER (E SIGN? NUMBER)?
   ;


fragment NUMBER // finished
   : ('0' .. '9') + ('.' ('0' .. '9') +)?
   ;


fragment E
   : 'E' | 'e'
   ;


fragment SIGN // finished
   : ('+' | '-')
   ;


CR
   : [\r\n] +
   ;


WS
   : [ \t] + -> skip
   ;
