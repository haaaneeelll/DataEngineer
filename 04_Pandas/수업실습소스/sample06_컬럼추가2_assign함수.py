####################################################
#### 4. 컬럼 추가 및 삽입
'''
   DataFrame에 컬럼 추가
   ==> 기존 컬럼 값을 가지고 추가 정보를 얻을 때

  1. df['컬럼명'] = 리스트
    df['컬럼명'] = Series

  2.  new_df = df.assign(컬럼명=리스트)
  3.  new_df = df.assign(컬럼명=함수, 컬럼명=함수)

  4.  new_df = pd.concat([df,df2], axis=1)

  DataFrame에 컬럼 삽입

   1. df.insert(idx, 컬럼명, 값 )

'''


import numpy as np
import pandas as pd

df = pd.DataFrame({"이름":['홍길동','이순신','유관순','강감찬'],
                   "국어":[30, 26, 11, 10],
                   "수학":[20, 12, 20, 12]
                 }, index=[1,2,3,4])

# 2.  new_df = df.assign(컬럼명=리스트)
df = df.assign(영어=[10,20,30,40])

# 3.  new_df = df.assign(컬럼명=함수, 컬럼명=함수)
# def total(x):
#     return x["국어"]+x["수학"]+x["영어"]
# total = lambda x: x["국어"]+x["수학"]+x["영어"]
# df = df.assign(총합=total)
df = df.assign(총합=lambda x: x["국어"]+x["수학"]+x["영어"],
               총합2=lambda x: x["국어"]+x["수학"]+x["영어"])

# 평균 컬럼 추가하기
df = df.assign(평균=lambda x: np.round(x['총합']/3,1))
print(df)
