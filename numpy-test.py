import numpy as np

array=np.array([[1,2,3],[2,3,4]],dtype=np.int)
print(array)
print('number of dimenrion:',array.ndim)
print('shape:',array.shape)
print('size:',array.size)

a=np.array([10,20,30,40])
b=np.arange(4)
print(a,b)
c=a-b
print(c)