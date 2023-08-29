# #1a
# from sympy import *
# x= symbols('x')
# expr1 = x**2+1
# expr2 = 1-2*x
# pprint(expand(expr1*expr2))

# #1b
# from sympy import *
# x= symbols('x')
# expr1 = 5*x
# expr2 = (x**2+x+1)*(x-2)
# eqn = expr1/expr2
# pprint(apart(eqn))

# #1c
# from sympy import *
# x= symbols('x')
# expr1 = x-2
# expr2 = 1+x**2
# pprint(diff(expr1/expr2))

from sympy import *

x,y = symbols('x,y')
def f(x,y):
    return x*y+exp(-x*y)
x=0
x_beg = 0
x_end = 2
y = 1
h = 0.5
iteration = 1

while(x<x_end-h):
        y =y+f(x,y)*h
        x = x + h
        pprint(x)
        pprint(round(y,4))