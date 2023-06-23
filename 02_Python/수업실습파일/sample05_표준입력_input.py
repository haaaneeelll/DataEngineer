

help(input)

name = input("이름 입력")
age = input("나이 입력") # 키보드로 입력받는 데이터는 모두 문자로 처리한다.
grade = int(input("학년 입력"))
print(name, int(age) + 1, grade+1) # int() 사용하여 숫자로 변경
