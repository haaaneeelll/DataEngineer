'''
  예외처리
'''

print("1")
print("2")

try:
    n = 0
    result = 10/n
    print("결과값:", result)
    #...
except ZeroDivisionError as e:
    print("error:", e)
except ValueError as e:
    print("error:", e)
except Exception as e:
    print("error:", e)

print("3")
print("end. 정상종료")