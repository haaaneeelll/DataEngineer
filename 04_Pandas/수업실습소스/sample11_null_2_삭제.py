
## 2. 널(null) 값 삭제 및 변경
'''
     null 값 삭제 및 변경

     1. 행 삭제
        new_df = df.dropna(axis=0|'index', inplace=False)
        new_df = df.dropna(axis=0|'index', how="any|all" , inplace=False))

     2. 열 삭제
        new_df = df.dropna(axis=1|'column', inplace=False)
        new_df = df.dropna(axis=1|'column', how="any|all" , inplace=False))
'''

import numpy as np
import pandas as pd

df = pd.DataFrame({ "col1" : [1 ,1, 1, 1, np.nan],
                    "col2" : [2, 2, 2, 2, np.nan],
                    "col3" : [3, np.nan, np.nan, np.nan, np.nan],
                    "col4" : [np.nan, np.nan, np.nan, np.nan, np.nan]},
                    index = [1, 2, 3, 4, 5])
'''
 col1  col2  col3  col4
1     1   2.0   3.0   NaN
2     1   2.0   NaN   NaN
3     1   2.0   NaN   NaN
4     1   2.0   NaN   NaN
5    NaN   NaN   NaN   NaN
'''
print(df)

# 1. 행삭제
new_df = df.dropna(axis=0)
print(new_df)

new_df = df.dropna(axis=0, how="all")
print(new_df)

# 2. 열 삭제
new_df = df.dropna(axis=1)
print(new_df)

new_df = df.dropna(axis=1, how="all")
print(new_df)