### 자료형 ###

# 1) 일반 자료형(scalar타입) : 값 변경 불가(immutable)
print("1.정수: ", 0)
print("1.정수(음수): ", -10)
print("1.정수(10진수): ", 10)
print("1.정수(2진수): ", 0b10)   # 2
print("1.정수(8진수): ", 0o10)  # 8
print("1.정수(16진수): ", 0x10) # 16

print("2.실수: ", 3.14)
print("2.실수(지수표기법): ", 3e+5) # 300000.0

print("3.논리: ", True)
print("3.논리: ", False)

print("4.None: ", None) # null 의미

# 함수
def fun():
    print("5. 함수: fun")
fun()