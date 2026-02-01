import numpy as np
a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

#get a specific element-[r,c]
print(a[0,5])
print(a[0,-2])

#get a specific row
print(a[0,:])  #slice syntax-:

#get a specific column
print(a[:,3])

# [start-index:end-index:step-size]
print(a[0,1:6:2])
print(a[0,1:-1:2])

#changing index
a[1,5]=20
print(a)

#changing the whole column
a[:,2]=5
print(a)
a[:,2]=[1,2]
print(a)

#3d example
b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

#to get specific element--work outside in
print(b[0,1,1])
print(b[1,:,1])

#to replace
b[1,1,:]=[9,0]
print(b)











