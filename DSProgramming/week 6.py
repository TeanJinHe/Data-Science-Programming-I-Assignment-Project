# import numpy as np
# print(np.array([1,2,3]))//more function then list

# import numpy as np
# arr1=np.array([1,2]) #1D array so it’s not a matrix
# arr2=np.array([[1,2]]) #2D array - row matrix
# arr3=np.array([[1],[2]]) #2D array - column matrix
# arr4=np.array([[1,2], #2D array - matrix 2x2
# [3,4]])
# arr5=np.array([[1,2], #2D array - matrix 3x2
# [3,4],
# [5,6]])
# print(arr1)
# print(arr2)
# print(arr3)
# print(arr4)
# print(arr5)

# import numpy as np
# arr = np.array([1.1,3.5,3.9])
# newarr = arr.astype('i')
# print(arr.dtype)
# print(newarr)
# print(newarr.dtype)

# import numpy as np
# arr = np.array([11,31.1,29.9])
# newarr = arr.astype('i')
# print(newarr)
# print(newarr.dtype)

# import numpy as np
# arr= np.arange(4)
# print(arr)
#
# arr= np.arange(1,10,3)
# print(arr)#using arange

# import numpy as np
# arr= np.linspace(0,10, num =5)
# print(arr)
#
# arr= np.linspace(0,9, num=4)
# print(arr)#找平等的位值要几个

# import numpy as np
# x=np.random.randint(10)
# print(x)#未知数值在10里面
# x=np.random.random()
# print(x)#未知数值

# import numpy as np
# x=np.random.randint(100, size=(5))#size显示5个数值
# print(x)
# x=np.random.random(5)#显示5个数值
# print(x)

# import numpy as np
# x= np.random.randint(100, size=(20))
# print(x)
# x1= np.sum(x)
# print(x1)
# x2= max(x)
# x3= min(x)
# print(x3,x2)
# x4=np.average(x)
# print(x4)

# import numpy as np
#
# x= np.random.randint(100, size=(20))
# print(x)
# print(x.sum())
# print(x.min())
# print(x.max())
# print(x.)

# import numpy as np
#
# x = np.random.randint(10, size=(3,2))
# print(x)
# x = np.random.rand(3, 2)
# print(x)

# import numpy as np
#
# x= np.random.random()
# x1= np.random.random(2)
# x2= np.random.rand(2,3)
# print(x)
# print(x1)
# print(x2)

# import numpy as np
# print(np.random.randint(5, size=(2,4)))
# print(np.random.randint(10, size=(19,18)))
# print(np.random.rand(1,5))
# print(np.random.rand(5,1))

import numpy as np
y= np.array([[1,2,3,4],[5,6,7,8]])
print(y[::2,::2])

y=np.array([[1,2,3,4,],[5,6,7,8],[9,10,11,12]])
print(y[0:4,1])