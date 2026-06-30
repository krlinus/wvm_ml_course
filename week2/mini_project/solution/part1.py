import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
trace=True

def tprint(*args, **kwargs):
    if trace:
        print(*args, **kwargs)


df = pd.read_csv('penguins.csv')

tprint(f'Number of rows: {len(df)}')
tprint(f'First 10 rows:\n{df.head()}')
tprint(f'Dictionary:\n{df.describe()}')
tprint(f'Info:\n{df.info()}')
