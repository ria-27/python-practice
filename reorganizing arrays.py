#REORGANIZING ARRAYS
import numpy as np
before=np.array([[1,2,3],[4,5,6]])
print(before)

after=before.reshape((6,1))
print(after)

#vertically stacking vectors or matrices
v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])
v=np.vstack([v1,v2])
print(v)
v=np.vstack([v1,v2,v2,v1]) #keep stacking
print(v)

#horizontally stacking
h1=np.ones((2,4))
h2=np.zeros((2,2))
print(np.hstack([h1,h2]))
