# 3) 비교 연산자
k = 10
k2 = 5
print( k == k2 ) # SQL에서는 = 임.
print( k != k2 )
print( k > k2 )
print( k >= k2 )
print( k < k2 )
print( k <= k2 )

# None 비교
xyz = None
print( xyz is None ) # 권장


# n값이 5보다 크고 20 보다 작냐?
n = 10
result = (n>5) and  (n<20) # 일반적인 프로그램언어에서 사용하는 방식
print(result)

result = 5 < n < 20  # python 만 가능
print(result)
