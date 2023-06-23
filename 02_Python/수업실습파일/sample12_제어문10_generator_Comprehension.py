'''

   generator Comprehension

   1) 문법:
       변수 = (표현식  for 변수 in  집합형 )

  2) 한번에 실행 안되고 단계적으로 동작 됨.
     - next() 함수 이용해서 단계적으로 값을 얻는다.
'''

list_x = [n for n in [1,2,3]]
generator_x = (n for n in [1,2,3])

print("list comprehension:" , list_x) # [1, 2, 3]
print("generator comprehension:" , generator_x) # <generator object <genexpr> at 0x0000021B6B2F8B30>

print(next(generator_x))
print(next(generator_x))
print(next(generator_x))