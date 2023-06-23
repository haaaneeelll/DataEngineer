import numpy as np
import pandas as pd

'''
    인덱스 관리
    0. 인덱스 변경
       df.index=[값, ..]
       
    1. df.set_index(기존컬럼, inplace=True|False)
       df.reset_index( drop=True|False, inplace=True|False)
       
    2. df.reindex(index=값)
      ==> 기존 인덱스 재배치       

    3. ignore_index=True 
      ==> df와 df2 연결시 인덱스도 연결이 되서 중복된다.
          이때 인덱스는 빼고 연결하는 방법이다.
          ( 자동으로 인덱스가 생성됨 )
      
'''
# 4) df병합시 기존 index값이 중복발생 ==> ignore_index=True 로 index값을 재설정
df1 = pd.DataFrame({'a':[12,2]},
                   index=[1,2])
df2 = pd.DataFrame({'a':[120,20]},
                   index=[1,2])

new_df = pd.concat([df1, df2], ignore_index=True)
print(new_df)