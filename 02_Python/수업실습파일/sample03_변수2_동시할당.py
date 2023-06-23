### 변수 ###

# 2) 동시할당

# 값 하나를 여러 변수에 저장
n=n1=n2=10
'''
n=10
n1=10
n2=10
'''
print(n, n1, n2)


# 반드시 갯수가 일치해야 된다. ( 중요하다 )
name, age, address = ("홍길동",20,"서울")
name, age, address = ["홍길동",20,"서울"]
print(name,age,address)

# dummy variable ==> _(underscore) 이용
a, b, _ = 10, 20, 30
print(a, b)

 # dict는 key값이 저장된다.
a, b = {"x":"홍길동", "y":"이순신"}
print(a, b)