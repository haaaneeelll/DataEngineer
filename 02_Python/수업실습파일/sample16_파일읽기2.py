'''
   c:\sample.txt 파일 읽기

'''

# 예외처리 추가
### 일반적으로 파일을 읽는 코드
try:
    with open(r"c:\sample2.txt", "r", encoding="utf-8") as f:
         while True:
             line = f.readline()
             if not line: break # EOF (End Of File) 의미
             print(line, end="")
except FileNotFoundError as e:
    print("error:", e)
print("end.  정상종료")