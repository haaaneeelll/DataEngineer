#### 1. DataFrame 생성 방법
'''
   DataFrame의 컬럼과 인덱스 변경

   1. 컬럼명 변경

    df.columns=[값, 값2,..]

   2. 인덱스(라벨) 변경

     가.  pd.DataFrame(..., index=[값, 값2,..])
     나.  df.index=[값, 값2,..]

'''
# pip install pandas 설치하기
import numpy as np
import pandas as pd

df = pd.DataFrame({"col1" : [4 ,5, 6],
                   "col2" : [7, 8, 9],
                   "col3" : [10, 11, 12]})
# 1. 컬럼명 변경
df.columns=['c1','c2','c3']
print(df)

# 2. 인덱스(라벨) 변경
df = pd.DataFrame({"col1" : [4 ,5, 6],
                   "col2" : [7, 8, 9],
                   "col3" : [10, 11, 12]}, index=['A','B','C'])

df.index=[10,20,30]
print(df)