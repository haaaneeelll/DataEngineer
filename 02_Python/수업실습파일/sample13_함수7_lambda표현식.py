'''
    lambda 표현식 ( 익명함수 )
    - def 함수명() 문법을 이용한 함수 작성의 또 다른 표현식이다.
    - 반드시 단일 문장인 경우에만 lambda 표현식이 가능하다.
    - 익명함수이기 때문에 변수에 저장해서 호출해서 사용한다. (일급객체이기 때문에 가능)
'''
# 1. 파라미터 없고 리턴값 없음

def fun():
    print("fun")

# lambda 표현식
fun=lambda :print("lambda fun")
fun()

# 2. 파라미터 있고 리턴값 없음
def fun2(n=10,n2=20, *n3, **n4):
    print("fun2",n, n2)

# lambda 표현식
fun2=lambda n=10,n2=20, *n3, **n4:print("lambda fun2",n, n2, n3, n4)
fun2(10,20)
fun2()
fun2(10,23,4,4,5,6,5, age=20, addr="서울")

# 3. 파라미터 없고 리턴값 있음
def fun3():
    return 100

# lambda 표현식
fun3=lambda :100
result=fun3()
print("lambda fun3", result)

# 4. 파라미터 있고 리턴값 있음
def fun4(n,n2):
    return n+n2

# lambda 표현식
fun4=lambda n,n2: n+n2
result=fun4(10,20)
print("lambda fun4", result)