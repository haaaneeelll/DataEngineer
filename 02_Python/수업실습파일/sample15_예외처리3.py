'''
  예외처리
'''

print("1")
print("2")

try:
    n = 0
    result = 10/n
    print("결과값:", result)
except Exception as e:  # 적합한 예외클래스를 지정해야 된다. 단, 부모 예외클래스 지정 가능(부모는 자식을 포함하는 큰 개념 ),다형성
                        # 다형성을 이용해서 모든 예외를 Exception으로 사용할 수 있으나 권장안함. 디테일하게 처리함을 권장
    print("0 으로 나누어 예외발생됨")

print("3")
print("end. 정상종료")