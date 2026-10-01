import pandas as pd 

# Importing 

df = pd.read_csv (r'C:\Tutorial prac\Python_learning\Pandas_Learning\ImportingPandas.csv' , index_col= 'Name')

#print (df.to_string())

# Selection by colomn 

#print (df['Name'].to_string ())
#print (df['Height'].to_string ())
#print (df['Weight'].to_string ())

#print (df['Name', 'Height', 'Weight'].to_string ())

# Selection by rows

print (df.loc ['Pikachu'])
print (df.loc ['Charizard' : 'Blastoise', ['Height', 'Weight']])
print (df.iloc [0:11])

# Selection by every second/third row 

print (df.iloc [0:11:2])
print (df.iloc [0:11:3])


# Selection (Input)

pokemon = input ('Enter Pokemon Name : ')

try : 
    print (df.loc[pokemon])
except  KeyError :
    print (f'{pokemon} Not Found')