'''
   함수

'''

# 1. 파라미터 없고 리턴값도 없음

def fun():
    print("fun")

fun()
print("end")

# 2. 파라미터 있고 리턴값도 없음

def fun2(n, n2):
    print("fun2", n, n2)

fun2(10,"홍길동")
fun2([1,2,3], {"a":20})

# 3. 파라미터 없고 리턴값 있음

def fun3():
    print("fun3")
    return 100

result=fun3()
print(result)

def fun4():
    print("fun4")
    return 100,200

result=fun4()
print(result) # (100, 200)



# 4. 파라미터 있고 리턴값 있음

def fun5(n, n2):
    print("fun5")
    return n+n2

result=fun5(10,20)
print(result)