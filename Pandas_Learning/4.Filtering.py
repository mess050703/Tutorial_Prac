import pandas as pd

df = pd.read_csv (r'C:\Tutorial Prac\Python_Learning\Pandas_Learning\ImportingPandas.csv', index_col ='Name')

# print (df.to_string ())

tall_pokemon = df[df['Height'] >= 2]
heavy_pokemon = df[df['Weight'] >= 100]
legendary_pokemon = df[df['Legendary'] == True]
water_pokemon = df[(df['Type1'] == 'Water') | (df['Type2'] == 'Water')]
ff_pokemon = df[(df['Type1'] == 'Fire') | (df['Type2'] == 'Fire')]
ffl_pokemon = df[(df['Type1'] == 'Fire') & (df['Type2'] == 'Flying') & (df['Legendary'])]


print (ffl_pokemon)