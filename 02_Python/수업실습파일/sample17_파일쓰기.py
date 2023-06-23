'''
   c:\sample2.txt 파일 쓰기
   => 파일이 없으면 자동으로 생성해준다.
'''

# 가. 파일 쓰기,  mode: w(덮어쓰기)  a(추가, append)
with open(r"c:\sample2.txt", "a", encoding="utf-8") as f:
    f.write("numpy\n")
print("end. 정상종료")