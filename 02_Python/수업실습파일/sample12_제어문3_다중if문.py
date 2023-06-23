'''
   다중 if 문

   조건이 여러개 인 경우에 사용된다.

    점수         학점
    91 ~ 100     A
    81 ~ 90      B
    71 ~ 80      C
    나머지       F
'''

# 3. 다중 if ~ else 문
n = int(input("점수입력"))
if n>90:
    print("A 학점")
elif n>80:
        print("B 학점")
elif n>70:
        print("C 학점")
else:
    print("F 학점")
print("end")

print("-------------------------")

# 중첩 가능
num = 85
if num >= 90:
    print("우수")
else:
    if num >= 70:
        print("보통")
    else:
        print("저조")

