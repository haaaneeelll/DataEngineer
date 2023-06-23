# 대입 연산자 심화
a = b = c = 1
print(a, b, c)
name, age, address = "홍길동",20,"서울"  # 중요함, 갯수가 반드시 일치해야 된다.
print(name,age,address)

# 갯수가 달라도 된다. packing

x = [10, 20, 30]
print(x)

x,y,z = [10, 20, 30]
print(x,y,z)

x, *y= [10, 20, 30]
print(x,y) # 10 [20, 30]

x, *y= (10, 20, 30,54,5,6)
print(x,y) # 10 [20, 30, 54, 5, 6]

x, *y= {10, 20, 30}
print(x,y) # 10 [20, 30]


 # dict는 key값이 저장된다.
a, *b = {"x":"홍길동", "y":"이순신","z":"유관순"}
print(a, b) # x ['y', 'z']

*x, y, z= (10, 20, 30,54,5,6) #[10, 20, 30, 54] 5 6
print(x,y,z)