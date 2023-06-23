
## 1. 정렬
'''
   DataFrame 정렬

   1. 정렬
      df.sort_values(by=컬럼명, ascending=True, inplace=False, ignore_index=False, kind="quicksort", na_position="last")
      df.sort_values(by=[컬럼명,컬럼명2], ascending=True, inplace=False, ignore_index=False, kind="quicksort", na_position="last")

   2. 행 라벨 및 컬럼 라벨 정렬
      new_df = df.sort_index(axis=0|1)

'''

import pandas as pd
import numpy as np
import seaborn as sns

df = sns.load_dataset("mpg")
df = df.head(10)
df.index=list('HDAFCBEGIJ')
# null 변경
df[df['name']=='ford torino']=np.nan
# df = df.tail(8)
print(df, df.shape) #(398, 9)


# 1.  mpg 컬럼 오름차순 정렬
new_df = df.sort_values(by="mpg", ascending=False, inplace=False, na_position="first")
print(new_df)

# 2.  다중정렬, mpg, displacement  컬럼 오름차순 정렬
new_df = df.sort_values(by=["mpg","displacement"], ascending=False, inplace=False, na_position="first")
print(new_df)