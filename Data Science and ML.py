import numpy as np
import pandas as pd
from numpy.random import randn

# Index Levels
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

# Construct a Multi-index level data frame
df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])

# Setting index names for the G1, and 1,2,3 layers
df.index.names = ['Groups', 'Num']
print(df)

# Grab value at G2, 2, Column B
print(df.loc['G2'].loc[2]['B'])

# Very useful function called 'Cross-Section'
print(df.xs(1, level='Num'))

'-----------------------------------------------------------------------'

# Missing Data
d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
df = pd.DataFrame(d)
print(df)

# Explore the dropna method
df.dropna()
print(df)
# NOTE: dropna with axis 0 drops rows, and axis=1 drops columns with na values
df.dropna(axis=1)
print(df)
# NOTE: Thresh value will drop rows/columns with more than specified non-na values

# Explore the fillna method
print(df['A'].fillna(value=df['A'].mean()))

'-----------------------------------------------------------------------'

# Explore the groupby method to group rows of data together
# NOTE: Groupby allows you to group together rows based off of a column
# and perform an aggregate function on them

data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Midi', 'Sue', 'Cole', 'Jen', 'Schmegan', 'Luxi'],
        'Sales': [200, 120, 340, 124, 243, 350]}
df = pd.DataFrame(data)
print(df)

byComp = df.groupby('Company')
print(byComp.mean())
print(byComp.sum())
print(byComp.std())

# Won't usually create a groupby variable, but will instead do a one-liner
print(df.groupby('Company').sum().loc['GOOG'])

# Using the describe method to give lots of useful information
print(df.groupby('Company').describe())
# If you don't prefer the output format, use .transpose to change it
print(df.groupby('Company').describe().transpose())

'-----------------------------------------------------------------------'

# Learning Merging, Joining, and Concatenating data frames

# Concatenation essentially glues together dataframes. Keep in mind that
# dimensions should match along the axis you are concatenating on.
# You can use pd.concat and pass in a list of DFs to concatenate together
# Example: pd.concat([df1, df2, df3])

# Pandas is capable of using the merge function to do merge logic.
# It's very similar to merging SQL tables together.
# Using the pd.merge function, you can merge DFs together.
# Example: pd.merge(df1, df2, how='inner', on='key')

# Joining is a convenient method for combining the columns of two
# potentially differently-indexed DFs into a single resulting DF.
# You can think of this as the same thing as merge, except the keys you
# want to join on are on your index instead of a column.

'-----------------------------------------------------------------------'

