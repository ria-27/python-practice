import numpy as np
a = np.array([1, 2, 3],dtype='int32') # or np.int32
print(a)

b=np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)

#get dimension
print(a.ndim)
print(b.ndim)

#get shape
print(a.shape) 
print(b.shape) #rows and cols

#get type
print(a.dtype)

#get size
print(a.itemsize)   # 4 bytes here

#get total size
print(a.size*a.itemsize)
#--another way--
print(a.nbytes)



