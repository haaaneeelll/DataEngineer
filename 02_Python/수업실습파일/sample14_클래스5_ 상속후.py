'''
  상속후

'''
# 공통적인 속성 및 동작 추출하여 큰 개념의 Pet 작성한다.
class Pet: # 자동으로 (Object)가 지정된다.
    def __init__(self,n,a):
        self.username = n
        self.age = a

class Cat(Pet):  # Cat is a Pet,  상속관계
    def __init__(self,n,a):
        # 부모에서 초기화하도록 코드 수정
        super().__init__(n, a)

    # 추가 메서드 지정 가능
    def info(self):
        return self.username, self.age

class Dog(Pet):
    def __init__(self,n,a, g):
        # 부모에서 초기화하도록 코드 수정
        super().__init__(n, a)
        self.gender = g

    # 추가 메서드 지정 가능
    def info(self):
        return self.username, self.age, self.gender

#######################
c = Cat("야옹이", 2)
d = Dog("망치", 1, "숫컷")

print("고양이:", c.info())
print("강아지:", d.info())

# 상속의 계층 구조 확인 :   클래스명.mro()
print(Cat.mro())

# 다중상속 지원

