### 자료형 ###

# 2) 집합 자료형
print("1. 문자열: ", "hello") # 값 변경 불가(immutable)
print("1. 문자열: ", 'hello')
print("1. 문자열: ", """hello""") # triple 가능
print("1. 문자열: ", '''hello''')

print("2. 리스트(list): ", [1, 2, 3, 4, 4, "hello"]) # 순서있음. 중복 가능
print("4. 튜플(tuple): ", (1, 2, 3, 4, 4, "hello")) # 리스트와 동일 특징. 값 변경 불가(immutable)

print("3. 셋(set): ", {1, 2, 3, 4, 4, "hello"})  # 순서없다. 중복 불가, 저장 데이터는 immutable 데이터만 가능하다.
print("5. 딕트(dict): ", {"name": "홍길동", "age": 20})

