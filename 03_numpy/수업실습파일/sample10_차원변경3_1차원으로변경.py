
import numpy as np

print(np.__version__)

'''
   다차원 --> 1차원
   
   1.  arrND.flatten()- 많이 사용
      ==> 복사본 반환
      ==> 원본은 영향 없음
      
   2.  arrND.ravel()
      ==> view 반환 (링크걸림) 
      ==> 원본이 영향 받음 
'''

arr2D = np.arange(16).reshape(4,4)
print(arr2D)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
'''
print(arr2D.flatten()) #[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
print(arr2D.ravel()) #[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
######################################################################
xxx = arr2D.flatten() # 복사본 반환
yyy = arr2D.ravel()   # 원본과 링크로 연결된 상태
#원본 변경
arr2D[0,0]= 100
print(arr2D)
'''
[[100   1   2   3]
 [  4   5   6   7]
 [  8   9  10  11]
 [ 12  13  14  15]]
'''
print("flatten:", xxx) # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
print("ravel:", yyy)   # [100   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15]