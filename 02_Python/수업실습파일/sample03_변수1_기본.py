### 변수 ###

# 1) 기본
num = 4
name = "홍길동"
address = "서울"
height = 174.2
isMarried = True
email =["aa@daum.net","bb@google.com"]
info ={
    "핸드폰":["010", "011"],
    "애완동물":["강아지","고양이"]
}
print(num, id(num)) # 4 140719199405824 (주소값)
print(name, id(name)) # 홍길동 2190278661200
print(address, id(address)) # 서울 2190278661296
print(height, id(height))  # 174.2 2190278551600
print(isMarried, id(isMarried)) # True 140719199127376
print(email, id(email)) # ['aa@daum.net', 'bb@google.com'] 2190278446720
print(info, id(info)) # {'핸드폰': ['010', '011'], '애완동물': ['강아지', '고양이']} 2190278392640