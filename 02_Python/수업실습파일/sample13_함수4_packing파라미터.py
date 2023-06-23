'''
    packing 파라미터

    def  함수명(n, *n2):
        pass

    - 나머지값은 전부 tuple로 저장해서 전달된다.
'''

# 변수 선언
n, *n2 = 1,2,3,4,5
print(n, n2)


def fun(n, *n2):
    print(n, n2)

fun(10,20)
fun(10,20,30,40)

def fun2(n,x, *n2):
    print(n,x, n2)

fun2(10,20,4,5,6)

# default + packing 혼합 가능
def fun3(n=10,x=20, *n2):
    print(n,x, n2)

fun3()
fun3(1,2,3,3,4,5)