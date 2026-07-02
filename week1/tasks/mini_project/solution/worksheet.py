import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
trace=False

def tprint(*args, **kwargs):
    if trace:
        print(*args, **kwargs)


df = pd.read_csv('penguins.csv')


tprint(f'Number of rows: {len(df)}')
tprint(f'First 10 rows:\n{df.head()}')
tprint(f'Dictionary:\n{df.describe()}')
tprint(f'Info:\n{df.info()}')
tprint(f'Shape: {df.shape}')
tprint(f'nulls:\n{df.isnull().sum()}')
tprint(f'duplicates:\n{df.duplicated().sum()}')
tprint(f'descriptions:\n{df.describe()}')

print('*'*30,end='')
print('PART 1: Basic Data Analysis',end='')
print('Last 5 rows of the dataset')
print('*'*30)
#use df.tail()
print(df[-5:])
nrows,ncols=df.shape
column_names=[col for col in df.columns]
print(f'Number of rows: {nrows}, Number of columns: {ncols}')
print(f'Column names: {column_names}')

print(f'Info:\n{df.info()}')
print(f'nulls:\n{df.isnull().sum()}')
