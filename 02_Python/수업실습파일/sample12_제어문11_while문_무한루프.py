'''
   while 문 이용한 무한루프

   문법:

        while True:
            문장1
            문장2
            if 조건식: break
            
            
'''

while True:
    name = input("이름 입력하시오. 중지하려면 Q 입력")
    print("입력한 이름:", name)
    if name == "Q": break
    
print("종료")











