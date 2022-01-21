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