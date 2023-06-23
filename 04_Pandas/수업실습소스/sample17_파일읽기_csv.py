'''
   csv 파일 읽기

   df = pd.read_csv(경로)

'''
import pandas as pd

# 1. csv 파일읽기 기본
df = pd.read_csv("./data/scientists.csv")

# 2. 특정 컬럼을 index 로 변경
df = pd.read_csv("./data/scientists.csv", index_col=0)


# 3. 컬럼명 변경
df = pd.read_csv("./data/scientists.csv", header=0,
                 names=['name','born','died','age','occupation'])

# 4. 컬럼 선택 ==> 지정된 순서가 아닌 원본 순서로 출력됨.
df = pd.read_csv("./data/scientists.csv", usecols=['Age','Name'])
print(df)

# 5. 지정된 갯수만 보기
df = pd.read_csv("./data/scientists.csv", nrows=3)

# 6. , 아닌 임의의 구분자
df = pd.read_csv("./data/piped.csv", sep="|", index_col=0)
print(df)

# 7. csv 파일로 저장
df.to_csv("./data/piped_copy.csv")