#MATHEMATICS
import numpy as np
a=np.array([1,2,3])
print(a)
print(a+2)
print(a-2)
print(a*2)
print(a/2)
print(a**2)

b=np.array([2,4,6])
print(a+b)

#getting sin,cos...
print(np.sin(a))
print(np.cos(a))

#LINEAR ALGEBRA
a=np.ones((2,3))
b=np.full((3,2),2)#3x2 of values 2
#col of 1st matrix=row of 2nd
print(a)
print(b)
print(np.matmul(a,b))

#determinant
c=np.identity(3)
print(np.linalg.det(c))
print(np.trace(c))
print(np.linalg.norm(c))

#STATISTICS
stats=np.array([[1,2,3],[4,5,6]])
print(stats)
print(np.min(stats))
print(np.max(stats))
print(np.min(stats,axis=0))
print(np.max(stats,axis=1))
print(np.sum(stats))
