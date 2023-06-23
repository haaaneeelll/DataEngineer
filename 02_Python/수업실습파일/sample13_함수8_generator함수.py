'''
    generator 함수
    
    - 함수내의 문장을 단계적으로 실행 가능
    - yield 키워드 이용하여 generator 함수로 생성 가능
    - next() 함수 이용
'''
# 1. 일반 함수
def fun():
    print("1")
    print("2")
    print("3")

f=fun()
print(f, type(f))
print("#"*100)
# 2. generator 함수 ==> yield 키워드 이용
def fun2():
    print("10")
    yield
    print("20")
    yield
    print("30")
    yield

f2=fun2()
print(f2, type(f2))
next(f2)
next(f2)
next(f2)