import numpy as np

array = np.array ([ 1, 2, 3, 4 ])

array = array * 2 

#print (array)

array = np.array([
                  [['A','B','C'],
                   ['D','E','F'],
                   ['G','H','I']],
                  
                  [['J','K','L'],
                   ['M','N','O'],
                   ['P','Q','R']],
                  
                  [['S','T','U'],
                   ['V','W','X'],
                   ['Y','Z',' ']]
                  ])

print (array.ndim)
print (array.shape)

# Multi - Dimensional Indexing

word = array[1,0,0] + array[0,0,0] + array[1,1,0]

print (word)