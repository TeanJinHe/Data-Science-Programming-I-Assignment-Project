# from sympy import *
#
# x = symbols('x')
# expr = (4*(x**3)+16*x+7)/((x**2)+4)**2
# pprint(apart(expr))

# from sympy import *
#
# x,y,z=symbols('x,y,z')
# f = cos(x)*sin(y)*sin(z)
# pprint(integrate(f,(z,pi,2*pi),(y,-pi/2,0),(x,pi,pi**2)))

from sympy import *

x,y=symbols("x,y")
f=symbols('f',cls=Function)
eq=Eq(x*f(x).diff(x)+f(x)-(f(x)*f(x)),0)
pprint(eq)
pprint(dsolve(eq))

# from sympy import *
#
# x,y=symbols('x,y')
#
# pprint(nonlinsolve([x-y+1,y+x**2-3],[x,y]))



