

# 이스케이프 문자 (escape 문자) ==> \는 특별한 의미를 갖는다.
print("c:\\temp") # 파일 경로 지정시 주로 사용됨.
print("Hello\nworld") # 엔터 친 효과
print("Hello\tworld") # 탭 친 효과
print("she\'s")
print("\"hello\"")


# raw string : 이스케이프 문자를 무시한다.,
# 정규 표현식(regular expression):패턴매칭, *?+^() 특별한 의미를 가짐.
print(r"c:\\temp") #  c:\\temp
print(r"c:\temp") #  c:\temp
print(r"Hello\nworld") #  Hello\nworld
print(r"Hello\tworld") #  Hello\tworld
print(r"she\'s") # she\'s
print(r"\"hello\"") # \"hello\"