import numpy as np
a = np.arange(15).reshape(3, 5)
print(a)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
print(type(a))



url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'
df = pd.read_csv(url)
print(df.types)
path = ''
df.to_csv(path)
