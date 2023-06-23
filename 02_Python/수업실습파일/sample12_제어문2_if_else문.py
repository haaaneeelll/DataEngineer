'''
   if~else문

   조건에 따라서 실행되는 문장이 다른 경우에 사용된다.

'''

# 2. if ~ else 문
n = int(input("정수입력"))
if n%2==0:
    print("짝수1")
    print("짝수2")
else:
    print("홀수")
print("end")

# in 리스트 활용
pocket = ['paper','card','tel']
if 'tel' in pocket:
    print("tel")
else:
    print("None")
print("-------------------------")