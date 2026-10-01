import pandas as pd

# Series

data = [100, 102, 104]

series = pd.Series (data)

print (series)

print ('')

data = ['A', 'B', 'C']

series = pd.Series (data)

print (series)

print ('')

data = [True, False, True]

series = pd.Series (data)

print (series)

print ('')

data = [100.1, 102.5, 104.8]

series = pd.Series (data)

print (series)

print ('')

# Indexes 

data = [100, 102, 104]

series = pd.Series (data, index = ['Apartment #1', 'Apartment #2', 'Apartment #3'])

print (series)

print ('')

data = [100, 102, 104]

series = pd.Series (data, index = ['a','b','c'])

print (series.loc['a'])
print (series.loc['c'])

print ('')

# Changing Index's Values 

data = [100, 102, 104]

series = pd.Series (data, index = ['a','b', 'c'])

series.loc['c'] = 200

print (series.loc['c'])

print ('')

# Filtering index values 

data = [100, 102, 104, 200, 202]

series = pd.Series (data, index = ['a','b','c','d','e'])

print (series[series < 200])

print ('')

# Influencing index values

calories = {'Day 1' : 1750, 'Day 2' : 2100, 'Day 3': 1700}

series = pd.Series (calories)

series.loc['Day 3'] += 500

print (series)

print ('')

# When calories were less tha 2000

calories = {'Day 1' : 1750, 'Day 2' : 2100, 'Day 3': 1700}

series = pd.Series (calories)

print (series[series < 2000])