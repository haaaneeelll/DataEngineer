'''

    range 함수

   range(stop)
   range(start, stop[, step])
     ==> start 포함, stop 미포함
     ==> 기본값은 0 부터
'''
# help(range)
print(list(range(10))) # 0 ~ 9
print(list(range(1,5))) # 1 ~ 4
print(list(range(1,10,2))) # 1 3 5 7 9