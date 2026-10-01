import matplotlib.pyplot as plt
import numpy as np

catagories = np.array(['Grains', 'Fruits', 'Vegetables', 'Protein', 'Dairy', 'Sweets'])
values = np.array([4, 3, 2, 5, 3, 1])

plt.bar (catagories,values, color = 'Skyblue')
# plt.barh (catagories,values, color = 'Skyblue')

plt.title ('Daily Consumption')
plt.xlabel ('Food')
plt.ylabel ('Quantity')

plt.show ()