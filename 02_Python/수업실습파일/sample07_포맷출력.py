# 2) 포맷지정 출력

# 1. 문자열 데이터 표현
mesg = "이름:{}".format('홍길동')
print(mesg)

mesg = '이름:{0}'.format('홍길동')
print(mesg)

mesg = '이름:{0}, 나이:{1}'.format('홍길동',20)
mesg = '이름:{1}, 나이:{0}'.format('홍길동',20)
mesg = '이름:{1}, 나이:{1}'.format('홍길동',20)
mesg = '이름:{0:5s}, 나이:{1}'.format('홍길동',20)
print(mesg)

# 2. 수치 데이터 표현
mesg = '{0}'.format(123456789)
print(mesg)

mesg = '{0:f}'.format(123456789) # 123456789.000000
print(mesg)

mesg = '{0:.3f},{0:.9f}'.format(123.4567) # 123.457,123.456700000
print(mesg)

mesg = '{0:,}'.format(123456789) # 123,456,789
print(mesg)

# 3. key 사용 ( 중요하다 )
mesg = '이름: {username}, 나이: {age}'.format(username='홍길동', age=20)
print(mesg)


# 4. unpacking - 문자열/리스트
mesg = '{0}:{1}:{2}'.format(*'홍길동')
print(mesg)  # 홍:길:동

mesg = '{0}:{1}:{2}'.format(*['홍길동', '이순신', '강감찬'])
print(mesg) # 홍길동:이순신:강감찬

# 4. unpacking - dict
person = {'username': '홍길동', 'age': 20} # ==> username=홍길동, age=20
mesg = '이름: {username}, 나이: {age}'.format(**person)
print(mesg)

# 정렬, 채우기,.....
help('FORMATTING')


# 5. % 지정 방식 ( 고전방식 )
print("이름: %s 나이: %d 신장: %.2f 결혼여부:%s 성별:%c" % ("홍길동", 200, 178.5987, True, '남'))

# 6. format string 방식
name = "KyIN"
age = 20

print("이름:{name} 나이:{age}")
print(f"이름:{name} 나이:{age}")
print(f"이름:{name} 나이:{age+1}") # 산술 연산 가능
print(f"이름:{name} 나이:{age > 30}") # 비교 연산 가능
print(f"이름:{name.lower()} 나이:{age > 30}") # 함수 적용도 가능

