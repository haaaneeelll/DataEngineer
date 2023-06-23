'''
    python의 변수는 함수 scope 를 따른다.
    ==> 함수안에서 선언된 변수는 함수안에서만 사용 가능하다.
'''

n = 10  # 전역 변수 ( global variable )
def fun():
    n2 = 20  # 지역 변수 ( local variable )
    print("n:" , n)
    print("n2:" , n2)

fun()
print("n:", n)
# print("n2:", n2)
