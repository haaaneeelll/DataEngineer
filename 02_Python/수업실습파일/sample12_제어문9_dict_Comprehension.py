'''

   dict Comprehension
   => dict로부터 가공하여 새로운 dict로 반환하는 기능

   가.  변수 = { k:v for k,v in  dict.items()}
   나.  변수 = { k:v for k,v in  dict.items() if 조건 }
   다.  변수 = { 3항연산자 k:v for k,v in  dict.items() }

'''
# 가.
x = {"대한민국":"서울", "미국":"워싱턴","중국":"베이징"}
x2 = { v:k for k,v in x.items()}
x2 = { k:len(v) for k,v in x.items()}
print(x2)

# 나.  국가명이 2글자인 경우에만 반환
x2 = {k:v for k,v in x.items() if len(k)==2}
print(x2)


# 다.  국가명중에서  대한민국은  korea로 표시
x2 = { "korea" if k=="대한민국" else k for k,v in x.items()}
print(x2)