# import math
# import sympy
#
# print(math.sqrt(8))
# print(sympy.sqrt(8))

# import math
# import sympy
# from sympy import *
#
# print(math.sqrt(8))
# print(sympy.sqrt(8))
# print(prime(5))
# x=symbols('x')
# eqn=x+x+1
# print(eqn)
# pprint(eqn)
#
# x=symbols('x')
# expr1=x*x+3
# expr2=2*x*x-1
# pprint(expr1+expr2)
# pprint(expr1-expr2)
# pprint(expand(expr1*expr2))
# pprint(expand(expr1/expr2))

import math
import sympy
from sympy import *

# theta=symbols('theta')
# pprint(2+2*expand_trig(sin(pi-theta)))
# x=symbols('x')
# pprint(trigsimp((1-sin(x)**2)/(csc(x)**2-1)))

# from sympy import *
# x,y=symbols('x,y')
#
# pprint(linsolve([x+5*y-2,-3*x+6*y-15],(x,y)))
# pprint(nonlinsolve([x**2+y-5,x**2+y**2-7],(x,y)))

# from sympy import *
# x,y=symbols('x,y')
# f= symbols('f',cls=Function)
#
# eqn=Eq(f(x).diff(x,2)-2*f(x).diff(x)+f(x),sin(x))
# pprint(eqn)
# pprint(dsolve(eqn))

# from sympy import *
# x,y,z =symbols('x,y,z')
# pprint(linsolve([15*x+17*y+19*z-3890,0.3*x+0.4*y+0.55*z-95,x+1.2*y+1.5*z-282],(x,y,z)))

from sympy import *
x=symbols('x')
#series expansion
expr=cos(x)
z=expr.series(x,0,5)
pprint(z)
z1=expr.series(x,0,5).removeO()
pprint(z1)
pprint(z1.subs(x,1))