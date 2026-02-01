import numpy as np
#INITIALIZATION
#----------------
#All 0s matrix
a=np.zeros((2,2),dtype=np.int32) #need to specify shape
b=np.zeros(5)
c=np.zeros((3,5,1))
print(a)
print(b)
print(c)

#All 1s matrix
print(np.ones((4,2),dtype=np.int32))

#Any other number (full_like)--take a shape that has already been built--copy 
print(np.full_like(a.shape,4))

#Initialize matrix of random numbers
print(np.random.random((4,2)))
print(np.random.randint(4,7,size=(2,2)))
print(np.identity(5))#square matrix

#repeating an array
a=np.array([1,2,3])
r1=np.repeat(a,3) #specifying what and how many times to repeat
print(r1)

b=np.array([4,5,6])
r2=np.repeat(b,3,axis=0)
print(r2)

#recap 
output=np.ones((5,5),dtype=np.int32)
print(output)
z=np.zeros((3,3),dtype=np.int32)
z[1,1]=9
print(z)
output[1:-1,1:-1]=z
print(output)

#copying
a=np.array([1,2,3])
b=a #they point to the same thing--both get same values even when one of them is changed
print(b)
b[0]=100
print(b)
print(a) #--> problem is that a also has same value as b instead of its initial value
c=np.array([1,2,4])
b=c.copy()  #initial value of c stays same
b[0]=100
print(b)
print(c)
