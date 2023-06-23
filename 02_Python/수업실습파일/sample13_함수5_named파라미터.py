'''
    named 파라미터 ( 매우 중요하다 )

    def fun(age, username):
        pass

    fun(10, '홍길동')
    #fun('홍길동',10)

    fun(age=10, username='홍길동')
'''
def fun(age, username):
    print(age, username)
fun(10, "홍길동")
fun(age=10, username='홍길동')
fun(username='홍길동', age=10)

# 추가 정리
def fun2(**n):
    print(n)

fun2(age=10)
fun2(age=10, username='홍길동')
fun2(age=10, username='홍길동',address="서울")

# 혼합
def fun3(n=1,n2=2,*n3, **n4): # 순서 중요
    print(n, n2, n3, n4)

fun3(10,20,30, age=10, username='홍길동')
fun3(10,20,30,40,50, age=10, username='홍길동')
fun3()