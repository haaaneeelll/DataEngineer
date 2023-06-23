'''
   단일 if문
   - 조건에 따라서 실행되거나 실행되지 않는 문장을 작성할 수 있다.

'''
# 1. 단일 if문
print("1")
if 3==3:
    print("2")
    print("3")
    print("4")
print("5")
print()

# 1. 단일 if 문2
if 3 == 3: print("True")
print("-------------------------")

# 문제1:  키보드로 숫자를 입력 받아서 짝수인 경우에만 출력하는 프로그램을 작성하시오.

num = int(input("숫자입력:"))

if num%2==0 and num > 10:
    print("hello")


# 문제 2: xxx 리스트안에 값이 있는지 없는지 확인해서 있을 경우에만 출력하는 프로그램을 작성하시오.
xxx = []

if len(xxx)!=0:
    print("list에 값 있음")

if xxx: # True/False가 아닌 값도 사용 가능.
    print("list에 값 있음")
