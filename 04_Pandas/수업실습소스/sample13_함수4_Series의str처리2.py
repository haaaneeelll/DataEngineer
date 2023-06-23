'''
    Series의 문자열 처리

    1. series.str.함수

    * 문자열 관련 함수
    1) python
       - 문자열.함수
        예> "hello".upper()

    2) numpy
        arr = np.array(['aa','Bb','cc'])
        => np.char.함수명

    3) pandas
        series.str.함수
'''
'''
'capitalize', 'casefold', 'cat', 'center', 'contains', 'count', 'decode', 'encode', 
'endswith', 'extract', 'extractall', 'find', 'findall', 'fullmatch', 'get', 'get_dummies', 
'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'islower', 'isnumeric', 'isspace', 
'istitle', 'isupper', 'join', 'len', 'ljust', 'lower', 'lstrip', 'match', 'normalize', 'pad', 
'partition', 'removeprefix', 'removesuffix', 'repeat', 'replace', 'rfind', 'rindex', 'rjust', 
'rpartition', 'rsplit', 'rstrip', 'slice', 'slice_replace', 'split', 'startswith', 'strip', 
'swapcase', 'title', 'translate', 'upper', 'wrap', 'zfill'
'''
import numpy as np
import pandas as pd
info={"name":["Hello","Happy","cat"],
      "age":[18,31, 33],
      "birthday":['1920/09/28','1910/03/26','2020/03/26']}
df = pd.DataFrame(info)
print(df)
'''
    name  age    birthday
0  Hello   18  1920/09/28
1  Happy   31  1910/03/26
2    Cat   33  2020/03/26
'''
# 1. series.str.replace(old, new)
df['name1']=df['name'].str.replace("Hello","hello")
# print(df)

# 2.  인덱싱 및 slice
df['name2']= df['name'].str[:]
# df['name']= df['name'].str[::-1]
# df['name']= df['name'].str[1:]
df['name3']= df['name'].str[0]
# print(df)

# 3.  upper, lower
df['name4']= df['name'].str.upper()
df['name5']= df['name'].str.lower()

# 4.  contains(값|값2) - 중요 , boolean 인덱스
df['name6']= df['name'].str.contains('a')
df['name7']= df['name'].str.contains('a|e')

# 실습: name 컬럼에서 a 포함된 값 출력?
xxx = df['name']
print(xxx, type(xxx))
print(xxx.str.contains('a'))
print(xxx[xxx.str.contains('a')])
print(df['name'][df['name'].str.contains('a')])

# 5.  startswith, endswith ==> boolean 인덱스
df['name8']= df['name'].str.startswith('H')

# 6.  islower ==> boolean 인덱스
df['name9']= df['name'].str.islower()
print(df)

# 7. one-hot 인코딩 변환
pets = pd.Series(['Cat','Dog', 'Bird'])
print(pets.str.get_dummies())