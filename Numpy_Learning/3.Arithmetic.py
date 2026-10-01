import numpy as np

# Scalar Arithmetic 

array = np.array ([1,2,3])

print (array - 1)
print (array + 4)
print (array * 3)
print (array / 4)
print (array ** 5) # ^5

print ('')

# Vectorized Math Functions 

array = np.array ([1.01,2.5,3.99])

print (np.sqrt(array)) 
print (np.ceil(array)) 
print (np.round(array))
print (np.pi)

print ('')

# Exercise 

radii = np.array ([1,2,3])
print (np.pi * radii ** 2)

print ('')

# Element-wise Arithmetic 

array1 = np.array ([1,2,3])
array2 = np.array ([4,5,6])

print (array1 + array2)
print (array1 - array2)
print (array1 * array2)
print (array1 / array2)
print (array1 ** array2)

print ('')

# Comparision Operator 

scores = np.array ([91, 55, 100, 73, 82, 64])

print (scores == 100)
print (scores < 60)

scores [scores < 60] = 0
print (scores)