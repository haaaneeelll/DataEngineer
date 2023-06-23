### 연산자 ###

# 1) 산술 연산자
a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print("h"*10) # hhhhhhhhhh
print(a/b)    # 3.3333333333333335 , 나누기 할 때 소수점까지 출력됨.
print(a % b)  # 1  ,  Modulus

print(a//b)   # 3  ,  Floor Division   소수점 버림
print(a**b)   # square ( 제곱 )

# 몫과 나머지를 한꺼번에 반환 ( tuple 로 반환 )
result = divmod(10, 3) # (3, 1)
print(result)
# name, age, address = ("홍길동",20,"서울")
x, y = divmod(10, 3) # 일반적임
print(x, y)
