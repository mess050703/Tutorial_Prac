import pandas as pd

df = pd.read_csv (r'C:\Tutorial Prac\Python_Learning\Pandas_Learning\ImportingPandas.csv', index_col = 'Name' )

#print (df.to_string())

#Aggregation 

#Whole DataFrame 
print (df.mean (numeric_only= True))
print (df.sum (numeric_only = True))
print (df.min (numeric_only = True))
print (df.max (numeric_only = True))
print (df.count ())

#Single column 
print (df['Height'].mean())
print (df['Height'].sum())
print (df['Height'].min())
print (df['Height'].max())
print (df['Height'].count())

#Group By

group = df.groupby('Type1')

print (group['Height'].mean())
print (group['Height'].sum())
print (group['Height'].min())
print (group['Height'].max())
print (group['Height'].count())