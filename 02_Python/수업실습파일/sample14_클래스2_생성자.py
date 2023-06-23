'''
   생성자

   - 클래스내의 메서드(함수)

   - 문법:
         class 클래스명:

            def __init__(self):
                  pass

   - 생성자도 호출해야 된다. ==> 호출방법은 클래스명()

   - 생성자 역할:  객체생성할 때 실제 인스턴스가 필요한 데이터(예>야옹이, 2)를
                 인스턴스 변수 초기화
'''

# 애완동물관리 프로그램 개발구축

class Cat:

    def __init__(self, n, a):
        print("__init__ 생성자", id(self))
        self.username=n
        self.age=a

c = Cat("야옹이", 2) # 하나의 고양이 생성
print(id(c)) # 2596022614384
print(c.username, c.age)

c2 = Cat("나비",1) # 두번째 고양이 생성
print(c2.username, c2.age)


