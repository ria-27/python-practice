import numpy as np
a=np.arange(1,31).reshape(6,5)
print(a)

#1
matrix=a[2:4,0:2]
print(matrix)

#2
matrix=a[[0,1,2,3],[1,2,3,4]] #list out rows, then columns
print(matrix)

#3
matrix=a[[0,4,5],3:]
print(matrix)
