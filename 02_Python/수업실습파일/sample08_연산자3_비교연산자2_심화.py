


# 동등 비교
'''
  a == b : a와 b의 실제값을 비교한다.
 a is b  : a와 b의 주소값을 비교한다.
           id(a) == id(b) 동일
'''
a = [1,2,3,4,5]
b = a
print(a, id(a)) # [ 1, 2, 3, 4, 5] 2589885980608
print(b, id(b)) # [1, 2, 3, 4, 5]  2589885980608
print( a==b) # True
print( a is b, id(a) == id(b)) # True True

c = a[:] # a 복사본 생성
print(c, id(c)) # [1, 2, 3, 4, 5] 2180534751936
print(a==c) # True
print(a is c) # False