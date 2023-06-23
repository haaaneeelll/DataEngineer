'''

   List Comprehension 
   => list로부터 가공하여 새로운 리스트로 반환하는 기능

   가.  변수 = [표현식  for 변수 in  집합형]
   나.  변수 = [표현식  for 변수 in  집합형  if 조건식]
   다.  변수 = [ 3항연산자 표현식  for 변수 in  집합형]
        변수 = [ 참 if 조건식 else 거짓 표현식  for 변수 in  집합형]
'''
# 가)
x = [n+1 for n in [1,2,3]]
x = [n > 2 for n in [1,2,3]]
x = [n.upper() for n in ["A","b","C"]]
print(x)
'''
m = ["A","b","C"]
k = []
for m2 in m:
    m3 = m2.upper()
    k.append(m3)
print(k)
'''

# 나) 짝수만 출력
x = [n for n in range(1,11) if n%2==0]
print(x)

# 다) 짝수면 0으로 홀수면 1 로 반환
x = [ 0 if n%2==0 else 1  for n in range(1,11)]
print(x)