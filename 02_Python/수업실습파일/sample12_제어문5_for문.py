'''
   반복문

   for 변수 in 집합형:
       문장

    집합형: 리스트, 문자열, range(n) ==> 갯수 만큼 반복된다.

'''

# 1) 특정 문장 반복처리하는 기본코드
for _ in range(3):
    print("happy")

# 2) 집합형에 저장된 데이터 얻기
for n in [1,2,3]:
    print(n)

for n in (10,20,30):
    print(n, end=" ")
print()

for n in {100,200,300,300}:
    print(n, end=" ")
print()

for s in "abcde":
    print(s)


# 반복할 때 idx값 얻기
for idx, n in enumerate([10,20,30]):
    print(idx, n)

for idx, n in enumerate("abcde"):
    print(idx, n)

for idx, n in enumerate([10,20,30], 1):
    print(idx, n)


# 4) dict 반복
soft = {'java':'웹용', 'python':'만능언어', 'oracle':'db처리'}
for key, value in soft.items():
    print(key + ':  ' + value)
print()

for key in soft.keys():
    print(key, end=" ")
print()

for value in soft.values():
    print(value, end=" ")
print()