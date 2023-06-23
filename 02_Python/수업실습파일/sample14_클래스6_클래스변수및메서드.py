'''
   클래스 변수 및 메서드
'''

class Person:
    
    address ="서울" # 클래스 변수, 단 한번 생성 , 클래스명.변수 로 접근==> 목적: 여러 인스턴스가 공유 가능
    
    def __init__(self,n,a):
        # 인스턴스 변수, 객체생성시마다 매번 생성
        self.username = n
        self.age = a

    def info(self):
         return self.username, self.age, Person.address

    # 클래스 메서드:  목적: 객체생성없이 사용하기 위해서
    @classmethod
    def get_address(cls):
        return Person.address

Person.address = "제주" # 한번에 address 변경이 가능하다.
print(Person.get_address())

p = Person("홍길동",20)
p2 = Person("이순신",44)

print("p1:", p.info(), Person.get_address())
print("p2:", p2.info(), Person.get_address())