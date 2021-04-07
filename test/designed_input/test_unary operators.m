%test unary operators( logical operators, sign operators, transpose operators)

a=1
b=2
c=10
d=7
e=0
%Try logical operator(right association)
A=~a
B=~(a&b)
%Try sign operators(right-association)
M=+(a-c)
N=-a
%Try transpose operators
%B=A.' 是转置
%B=A'  是共轭转置
x=[1,2,3;4,5,6]
X=x.'
Y=x'
