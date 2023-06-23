'''
  상속전
'''

class Cat:
    def __init__(self,n,a):
        self.username = n
        self.age = a
    # 추가 메서드 지정 가능
    def info(self):
        return self.username, self.age

class Dog:
    def __init__(self,n,a, g):
        self.username = n
        self.age = a
        self.gender = g
    # 추가 메서드 지정 가능
    def info(self):
        return self.username, self.age, self.gender

#######################
c = Cat("야옹이", 2)
d = Dog("망치", 1, "숫컷")

print("고양이:", c.info())
print("강아지:", d.info())

