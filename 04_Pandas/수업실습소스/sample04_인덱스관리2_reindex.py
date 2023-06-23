import numpy as np
import pandas as pd

'''
    인덱스 관리
    
    1. df.set_index(기존컬럼, inplace=True|False)
       df.reset_index( drop=True|False, inplace=True|False)
       
    2. df.reindex(index=값)
      ==> 기존 인덱스 재배치       

'''

df = pd.DataFrame({ "date":['2021','2022','2012','2023','2024'],
                    "City": ["Seoul", "Seoul", "Seoul","Seoul","Seoul"],
                    "Temperature": [32, 34,32, 34,53]
                  },index=list('AECBD'))

# 3. 인덱스 재배치
new_df = df.reindex(index=list('ABCDE')) #  AECBD --> ABCDE 로 재배치
print(new_df)
print(df)