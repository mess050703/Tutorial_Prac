import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

df = pd.read_csv (r'C:\Tutorial Prac\Pandas_Learning\ImportingPandas.csv')

# print (df.to_string ())

type_count = df['Type1'].value_counts (ascending = True)

plt.barh (type_count.index, type_count.values, color = "#08E8EC",
                                               edgecolor = 'black')

plt.title ('# of the pokemon')
plt.xlabel ('Count')
plt.ylabel ('Type')
plt.tight_layout ()

plt.show ()