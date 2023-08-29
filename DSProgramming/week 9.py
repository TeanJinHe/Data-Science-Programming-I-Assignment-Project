# import numpy as np
# np=myarray1.shape(2.8)
# myarray1.shape(2,8)

# import numpy as np
# Name=['Ayra','Insyirah','Taufik']
# Age=[2,5,25]
# BloodGroup=['O','AB', 'A']
# data=np.zeros(4,dtype={'names':('name','age','bloodgroup'),'formats':('U10','i4','f8')})

# import numpy as np
# def integrate (f,a, b, n):
#     x = np.linspace(a,b,n)
#     fx= f(x)

# import numpy as np
# x = np.linspace(0, 3, num=7)
# fx = np.sqrt(np.sin(x)**3+1)
# print(x)
# print(fx)
# h = 0.5
# sum=(np.sum(fx[1:6]))
# I=(h/2)*(np.array(fx[0])+np.array(fx[6])+2*sum)
# print(I)

import numpy as np
import math


import numpy as np
import math

x=np.linspace(0,3,num=7)
fx=np.round(np.sqrt(np.sin(x)**3+1),6)
print(x)
print(fx)

h=0.5
sum=0

def f(x):
    y= math.sqrt((math.sin(x)**3+1))
    return y

for x in np.arange(0,3.5,0.5):
    if x==0 or x==3.0:
        sum+=(f(x))
    else:
        sum+=2*(f(x))
I=(h/2)*sum
print(np.round(I,6))

