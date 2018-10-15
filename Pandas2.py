import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
s = pd.Series([1,3,5])
print(s.dtypes)

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/voting-records/house-votes-84.data')

#print(df)
#print(df.head(10))


#print(df.tail())
#print(df.tail(100))

#print(df.index)
#print(df.columns)

#print(df.values)
#print(df.describe())

#print(df.describe(include='all'))
#print(df.T)

print(df.describe(exclude=[np.number]))
#print(df.describe(exclude=[np.object]))



#print(df.sort_index(axis=1, ascending=False))
#print(df.sort_values(by='B'))
