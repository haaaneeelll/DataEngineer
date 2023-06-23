################################################################
################################################################

# 집합 자료형 변환
'''
  str(값) : str로 변경
  list(값) : list로 변경
  tuple(값) : tuple로 변경
  set(값) : set로 변경
  dict(값) : dict로 변경
'''
# list -> tuple,set
a = [10,20,30,30]
a2 = tuple(a)
a3 = set(a)
print(a) # [10, 20, 30, 30]
print(a2) # (10, 20, 30, 30)
print(a3) # {10, 20, 30} # 셋의 주요한 용도: 중복제거

# set -> list, tuple
a = {10,20,30,30}
a2 = list(a)
a3 = tuple(a)
print(a) # {10, 20, 30}
print(a2) # [10, 20, 30]
print(a3) # (10, 20, 30)

# tuple -> list, set
a = (10,20,30,30)
a2 = list(a)
a3 = set(a)
print(a) # (10, 20, 30, 30)
print(a2) # [10, 20, 30, 30]
print(a3) # {10, 20, 30} # 셋의 주요한 용도: 중복제거

# dict -> list,set,tuple (키만 추출)
a = {"name":"홍길동","age":100}
a2 = list(a)
a3 = set(a)
a4 = tuple(a)
print(a)
print(a2) # ['name', 'age']
print(a3) # {'name', 'age'}
print(a4) # ('name', 'age')

# str --> list , tuple
print( list("홍길동길")) # ['홍', '길', '동', '길']
print( tuple("홍길동길")) # ('홍', '길', '동', '길')
print( set("홍길동길")) # {'길', '홍', '동'}