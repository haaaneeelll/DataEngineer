'''
   내장 함수(built-in)

   print(dir(__builtins__))

'abs', 'all', 'any', 'ascii', 'bin', 'bool',
'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod',
'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir',
'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format',
'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id',
'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list',
'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open',
'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round',
'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super',
'tuple', 'type', 'vars', 'zip'

'''
# 빌트인 함수
print("1. 합계:", sum([1,2,3,4]))
print("2. 평균:", sum([1,2,3,4])/len([1,2,3,4]))
print("3. 리스트 최대값, 최소값:", max([1,2,3,4]), min([1,2,3,4]))
print("4. 딕셔너리 최대값", max({10:'aaa',4:'bbb',100:'ccc'})) #100
print("5. 딕셔너리 최소값", min({10:'aaa',4:'bbb',100:'ccc'})) #4
print("6. 절대값:", abs(-100))
print("7. 아스키코드값:", chr(65), chr(97)) # A a
print("7. 아스키코드값:", ord('A'), ord('a')) # 65 97

print("8. 몫과 나머지:", divmod(10,3))
print("9. 반올림:",  round(4.67))  # 소수점 0 자리 반올림, 즉 정수 반올림
print("10. 반올림:",  round(4.67, 1)) # 소수점 1자리 반올림

# zip 함수 ( 기억 )
x=['name',"age", "address"]
y=["홍길동", 20, "서울"]
print("12. zip:",list(zip(x,y))) #[('name', '홍길동'), ('age', 20), ('address', '서울')]
print("13. zip:",dict(zip(x,y))) # {'name': '홍길동', 'age': 20, 'address': '서울'}

## 실습
p = {"냉장고":1000, "TV":3000, "컴퓨터":2500}
print("가장비싼 제품", max(zip(p.values(),p.keys())))

# all, any  ==> 전부 또는 일부가 맞으면 True/False
b_list = [True, 1, False]
print(all(b_list))          #iterable data들 중 모두 참이면 참
print(all([1,1,0]))          #iterable data들 중 모두 참이면 참
print(any(b_list))

# 응용
b_list =[1, 3, 2, 5, 7, 6]
print("b_list 값이 모두 10 미만이냐?")
x = [n < 10 for n in b_list]
print(x)
print(all(x), all([n < 10 for n in b_list]))

print("b_list 값 중에서 3미만이 있냐?")
print(any([n < 3 for n in b_list]))

# filter 함수 ==> 내장된 함수에서 반환된 값이 참인 경우만 반환
# filter(함수, 집합형) 호출

b_list =[1, 3, 2, 5, 7, 6]

def fun(n):
    return n%2==0
result = filter(fun, b_list)


fun = lambda n: n%2==0
result = filter(fun, b_list)

result = filter(lambda n: n%2==0, b_list) # 가장 일반적임
print(list(result))

# 실습: 다음 문자열에서 영문자만 뽑아서 리스트로 출력하시오
xxx = "abde1234AbCde24Dgdd22"

def fun(n):
    return n.isalpha()

result= filter(fun, xxx)
result= filter(lambda n:n.isalpha(), xxx)
# print(list(result))
# "abdeAbCdeDgdd" 출력하시오
xxx = list(result)
print(xxx)
print("".join(xxx)) # 기억하기

# map 함수 ==> 내장된 함수에서 다른 함수적용(가공)후 반환
#  map(func, *iterables)
# help(map)


xxx = ["Abc","EbAeEG"]
def fun(n):
    return n.upper()

result = map(fun, xxx)
result = map(lambda n:n.upper(), xxx)
result = map(str.upper, xxx)
result = map(str.lower, xxx)

print(list(result))

# 문제: xxx의 글자 길이를 출력하시오
xxx = ["Abc","EbAeEG"]
def fun(n):
    return len(n)

result = map(fun, xxx)
result = map(len, xxx) # list.sort(key=len)
print(list(result))

# 문제: xxx2의 문자를 정수로 변환하여 출력하시오
xxx2 =['10','234','42']
result = map(int, xxx2)
print(list(result))

