'''
    sample3.csv 파일 읽기

'''
import csv
# 가.  ,로 구분자
with open(r"c:\sample3.csv", mode="r", encoding="utf-8") as f:
    data = csv.reader(f)
    for line in data:
        print(line, line[0], " ".join(line)) #['홍길동1', '40', '서울1']
print("#" * 100)

# 나.  |로 구분자
with open(r"c:\sample4.csv", mode="r", encoding="utf-8") as f:
    data = csv.reader(f, delimiter="|")
    for line in data:
        print(line, line[0], " ".join(line))
print("#" * 100)

# 다.  ,로 구분자, 헤더값 존재
with open(r"c:\sample5.csv", mode="r", encoding="utf-8") as f:
    next(f) #컬럼헤더 읽기
    data = csv.reader(f)
    for line in data:
        print(line, line[0], " ".join(line)) #['홍길동1', '40', '서울1']
print("#" * 100)