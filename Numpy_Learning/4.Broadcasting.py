import numpy as np

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1], [2], [3], [4]])

print (array1.shape)
print (array2.shape)

# because they have similar shapes they can be broadcasted together 

print (array1 * array2)
print (array1 + array2)