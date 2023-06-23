
## 3. Series의 기본 함수
'''
   1. 값 변경                                  ==>  df[컬럼].replace()
   2. 컬럼명 및 인덱스명 변경                     ==> df[컬럼].rename()
   3. 모든(특정) 컬럼(행)값의 참/거짓 여부          ==>  df[컬럼].any() , df[컬럼].all()
   4. 중복조회 및 제거                           ==>  df[컬럼].duplicated(),  df[컬럼].drop_duplicates()

   5. 임의의 함수 적용 ==> df[컬럼].apply(함수, axis=0|1)
      임의의 함수를 한번에 DataFrame의 행과 열에 적용.

   7. 값이 있으면 True, 아니면 False ==> df[컬럼].isin(집합형)
      ==> SQL의 in 연산자 동일
      
    8. unique한 값(종류)의 갯수 ==> df[컬럼].nunique(dropna=True)
                            dropna=False 면 nan 포함해서 갯수 반환
        
       df.nunique  ==> 갯수 반환
       series.unique ==> 값 반환

    9.  df['col1'].unique() ==>  유닉크 값 반환, sereis만 사용 가능

    10. df['col1'].value_counts() ==> 값의 빈도수 반환 . 중요

    11. df['col1'].between(start, end) ==> 범위에 있으면 True, 없으면 False
'''

import pandas as pd
import numpy as np
import seaborn as sns

df = pd.DataFrame({ "a" : [0 ,10, 100],
                    "b" : [2, 20, 200],
                    "c" : [3, 20, 300]},
                    index = list('ABC'))
'''
     a    b    c
A    0    2    3
B   10   20   20
C  100  200  300
'''
# 1. 값 변경
new_df = df['a'].replace({0:-1, 10:-2})
print(new_df)
# 2. 컬럼명 변경
x = df['a'].rename("col1")
print(x)
# 3. 참/거짓 여부
x = df['a'].all()
x = df['a'].any()
print(x)

# 샘플: a컬럼값이 모두 10보다 크냐?
x = (df['a']>10).all()
print(x)

df = pd.DataFrame({"k1":['one']*3 + ['two']*4,
                  "k2":[1,1,2,3,3,4,4] })
print(df)
'''
   k1  k2
0  one   1
1  one   1
2  one   2
3  two   3
4  two   3
5  two   4
6  two   4
'''
# 4. 중복여부
x = df['k1'].duplicated()
print(x)
# 5. 중복 제거후 반환
x= df['k1'].drop_duplicates(ignore_index=True)
print(x)

df = pd.DataFrame({"국어":[50,60,70,80,90],"수학":[100,60,100,100,80]})
print(df)
'''
  국어   수학
0  50  100
1  60  60
2  70  100
3  80  100
4  90  80
'''
x=df['국어'].apply(np.sum) # np.sum 연산은 했으나 결과값은 동일. 그룹함수 적용 가능
x=df['국어'].apply(lambda n: n+1) # lambda 적용가능
print(x)

# 8. df['국어'].isin(집합형) - 중요, SQL의 in연산자와 비슷
new_df = df['국어'].isin([60,80])
print(new_df)

df = pd.DataFrame({ "col1" : [1 ,2, 2, None, 1],
                    "col2" : [2, 3, 2, 2, np.nan],
                    "col3" : [ np.nan, 3, 2, 3, 3],
                    "col4" : [ np.nan, np.nan, np.nan, np.nan, np.nan]},
                    index = [1, 2, 3, 4, 5])
print(df)
'''
 col1  col2  col3  col4
1   1.0   2.0   NaN   NaN
2   2.0   3.0   3.0   NaN
3   2.0   2.0   2.0   NaN
4   NaN   2.0   3.0   NaN
5   1.0   NaN   3.0   NaN
'''
# 9. df['col1'].nunique() ==> 유닉크한 값 종류 갯수
x = df['col1'].nunique()
x = df['col1'].nunique(dropna=False)
print(x)

# 10. df['col1'].unique() ==>  유닉크 값 반환, sereis만 사용 가능
x = df['col1'].unique()
print(x)

# 11. df['col1'].value_counts() ==> 값의 빈도수 반환
x = df['col2'].value_counts()
x = df['col2'].value_counts(ascending=True)
x = df['col2'].value_counts(ascending=True, dropna=False)
print(x)

df = pd.DataFrame({"국어":[50,60,70,80,90],"수학":[100,60,100,100,80]})
print(df)
'''
  국어   수학
0  50  100
1  60  60
2  70  100
3  80  100
4  90  80
'''
# 12. df['col1'].between(start, end) ==> 범위에 있으면 True, 없으면 False
x = df['국어'].between(70,100)
print(x)