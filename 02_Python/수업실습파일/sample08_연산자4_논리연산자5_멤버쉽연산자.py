# 6) 멤버쉽 연산자 ( in 연산자 )

n = [10,9,8]
result = 10 in n
print("10포함 여부: ", result)

n = (10,9,8)
result = 10 in n
print("10포함 여부: ", result)

n = {10,9,8}
result = 10 in n
print("10포함 여부: ", result)

# dict는 key 존재여부 확인
n = {"name":"홍길동","age":20}
result = "name" in n
print("name 키포함 여부: ", result)