'''
    3항 연산자

    변수 = 참값  if 조건식 else 거짓값
'''

# 4. 3항 연산자
jumsu = int(input('점수-->'))

res = '합격' if jumsu >= 60 else '불합격'
print(res)
res = [2,3,4] if jumsu >= 60 else [-1,2]
print(res)

# 5. 중첩 3항 연산자
n = 70
m = "A" if n > 90 else "B" if n > 80 else "C"
print(m)