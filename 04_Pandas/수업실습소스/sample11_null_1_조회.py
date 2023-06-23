## 1. 널(null) 값 조회
'''
     널(null) 값 조회 : None, NaN or NA as null

    1.  Pandas 함수 이용
     1)  bool = pd.isna(스칼라|Series|df)
     2)  bool = pd.isnull(스칼라|Series|df)
     3)  bool = pd.notnull(스칼라|Series|df)

    2.  DataFrame 함수 이용
     1)  bool = df.isnull()
         bool = df[컬럼명].isnull()
         bool = df[[컬럼,컬럼2]].isnull()

'''


import numpy as np
import pandas as pd

df = pd.DataFrame({ "col1" : [1 ,1, 1, None, 1],
                    "col2" : [2, 2, 2, 2, np.nan],
                    "col3" : [ np.nan, 3, 3, 3, 3],
                    "col4" : [ np.nan, np.nan, np.nan, np.nan, np.nan]},
                    index = [1, 2, 3, 4, 5])
'''
col1  col2  col3  col4
1   1.0   2.0   NaN   NaN
2   1.0   2.0   3.0   NaN
3   1.0   2.0   3.0   NaN
4   NaN   2.0   3.0   NaN
5   1.0   NaN   3.0   NaN
'''
print(df)
# Pandas의 함수
# 1. df 대상
print(pd.isna(df))
print(pd.isnull(df))

print(pd.notnull(df))
print(~pd.isnull(df))

# 2. 특정 컬럼(Series) 대상
print(pd.isna(df['col1']))
print(pd.isnull(df['col1']))

# 3. 특정 컬럼들(DataFrame) 대상
print(pd.isna(df[['col1','col2']]))
print(pd.isnull(df[['col1','col2']]))
print("#"*100)

# DataFreame 함수
# 1. df 대상
print(df.isnull())
print(df.isna())

# 2. 특정 컬럼(Series) 대상
print(df['col1'].isnull())

# 3. 특정 컬럼들(DataFrame) 대상
print(df[['col1','col2']].isnull())
