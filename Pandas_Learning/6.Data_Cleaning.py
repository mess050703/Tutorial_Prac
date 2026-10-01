import pandas as pd

df = pd.read_csv (r'C:\Tutorial Prac\Python_Learning\Pandas_Learning\ImportingPandas.csv') #, index_col = 'Name')

# print (df.to_string())

# 1. Drop irrelevant coloumn 

relevant_col = df.drop (columns = ['Legendary', 'No'])

# print (relevant_col)
# print (relevant_col.to_string())

# 2. Handle missing data 

missing_data_cleared = df.dropna (subset = 'Type2')

#print (missing_data_cleared)
#print(missing_data_cleared.to_string())

fill_missing_data = df.fillna ({'Type2' : 'None'})

# print (fill_missing_data)
# print (fill_missing_data.to_string())

# 3. Fix Inconsistent Values

consistent_value = df['Type1'].replace({'Grass' : 'GRASS',
                                        'Water' : 'WATER',
                                         'Fire' : 'FIRE'})

# print (consistent_value)
#print (consistent_value.to_string ())

# 4. Standardize Text

capitalized_text = df['Name'].str.upper ()

#print (capitalized_text)
#print (capitalized_text.to_string())

# 5. Fix Data Type

number_to_boolean = df['Legendary'].astype (bool)

#print (number_to_boolean)
#print (number_to_boolean.to_string())

# 6. Remove Duplicates 

no_duplicates = df.drop_duplicates ()

#print (no_duplicates)
#print (no_duplicates.to_string())