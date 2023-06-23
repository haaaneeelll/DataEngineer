'''
    1. inner 병합

      가. 공통 컬럼 이용
          new_df = pd.merge(df, df2,  how=“inner”  on=“공통컬럼명”)
          new_df = pd.merge(df, df2,  how=“inner”  on=[“공통컬럼명”,“공통컬럼명2”]) => 복합컬럼

          new_df = pd.merge(df, df2,  how=“inner”  on=“공통컬럼명”, indicator=True)
                  .query("조건식").drop(columns=[컬럼,.])
'''
import numpy as np
import pandas as pd

# 1) 공통컬럼
df1 = pd.DataFrame({"x1":['A','B','C'],
                    "x2":[1, 2, 3]})

df2 = pd.DataFrame({"x1":['A','B','D'],
                    "x3":['T','F','T'],
                    "x4":['T1','F1','T1']})
print(df1)
'''
  x1  x2
0  A   1
1  B   2
2  C   3
'''
print(df2)
'''
  x1 x3  x4
0  A  T  T1
1  B  F  F1
2  D  T  T1
'''
# 1) df1과 df2의 공통컬럼인 x1으로 inner 병합
new_df = pd.merge(df1, df2, on="x1", how="inner")
new_df = pd.merge(df1, df2[['x1','x3']], on="x1", how="inner")
new_df = pd.merge(df1, df2, on=["x1"], how="inner")
new_df = pd.merge(df1, df2, on="x1", how="inner", indicator=True) # _merge 이용해서 병합유형 정보알려줌
print(new_df)

# 2) 복합컬럼
 # on=리스트
df1 = pd.DataFrame(
[
    ['T1', 'G1', 1, 1],
    ['T2', 'G1', 1, 1],
    ['T3', 'G1', 2, 1],
    ['T4', 'G2', 1, 1],
    ['T5', 'G3', 1, 1]
], columns=['TrasactionID', 'GoodsID', 'GoodsIDSeqNo', 'Quantity'])

df2 = pd.DataFrame(
[
    ['G1', 1, 1000],
    ['G1', 2, 1100],
    ['G2', 1, 2000],
    ['G2', 2, 2200]
], columns=['GoodsID', 'GoodsIDSeqNo', 'GoodsPrice'])
print(df1)
'''
    TrasactionID GoodsID  GoodsIDSeqNo  Quantity
0           T1      G1             1         1
1           T2      G1             1         1
2           T3      G1             2         1
3           T4      G2             1         1
4           T5      G3             1         1
'''
print(df2)
'''
    GoodsID  GoodsIDSeqNo  GoodsPrice
0      G1             1        1000
1      G1             2        1100
2      G2             1        2000
3      G2             2        2200
'''
new_df = pd.merge(df1, df2, on=["GoodsID","GoodsIDSeqNo"], how="inner")


# 3) query
df1 = pd.DataFrame({"x1":['A','B','C'],
                    "x2":[1, 2, 3]})

df2 = pd.DataFrame({"x1":['A','B','D'],
                    "x3":['T','F','T'],
                    "x4":['T1','F1','T1']})
new_df = pd.merge(df1, df2, on="x1", how="inner")\
           .query("x1 == 'A'")\
           .drop(columns=['x2','x4']) \
           .rename(columns={'x1':'X1','x3':'X3'})
print(new_df)

# 4)  suffixes 속성
df1 = pd.DataFrame({"x1":['A','B','C'],
                    "x2":[1, 2, 3]})

df2 = pd.DataFrame({"x1":['A','B','D'],
                    "x2":['T','F','T']})

new_df = pd.merge(df1, df2, on="x1", how="inner")
print(new_df)
'''
  x1  x2_x x2_y
0  A     1    T
1  B     2    F
'''
new_df = pd.merge(df1, df2, on="x1", how="inner", suffixes=["_left","_right"])
print(new_df)