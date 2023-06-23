
import numpy as np

print(np.__version__)

'''
    np.arange + reshape ( 중요 )

'''

print("1. arange(10)")
# arange([start,] stop[, step,], dtype=None, *, like=None
data = np.arange(10).reshape((2,5))
print(data)