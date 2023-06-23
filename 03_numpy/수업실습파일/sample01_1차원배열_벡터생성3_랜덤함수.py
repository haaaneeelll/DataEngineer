
import numpy as np

print(np.__version__)

'''
      2. 랜덤함수 이용
     가. np.random.seed(1234) # 랜덤값 고정   
     나. np.random.random([갯수]) : 0.0 <= 값 < 1.0 사이의 임의의 float 값 반환, 갯수 생략하면 1 개 반환
     다. np.random.rand([갯수]) :  0 ~ 1의 균등분포에서 표본 추출, 갯수 생략하면 1 개 반환, 동일한 확률로 랜덤값 추출
     라. np.random.randn([갯수]) :  표준편차가 1이고 평균값이 0인 정규분포에서 표본 추출. 갯수 생략하면  1개반환
                              * 편차: 값 - 평균값, 편차의 합은 0
     마. np.random.randint(최소범위, 최대범위, n개) : 주어진 최소(inclusive) ~ 최대(exclusive) 범위안에서 임의의 정수 n개 반환
        np.random.randint(최대범위, size=n개) :   0 ~ 최대(exclusive) 범위안에서 임의의 정수 n개 반환
'''
# 1) 랜덤값 고정
np.random.seed(1234)

# 2) np.random.random([갯수])
# 0.0 <= 값 < 1.0 사이의 임의의 float 5개 랜덤값 반환. 갯수 생략하면  1개반환
print("1. random(5)")
arr = np.random.random()
arr = np.random.random(5)
print(arr, type(arr), arr.dtype) #<class 'numpy.ndarray'> float64

# 3) np.random.rand([갯수])
# 0 ~ 1의 균등분포에서 표본 추출. 갯수 생략하면  1개반환
print("2. rand(5)")
arr = np.random.rand()
arr = np.random.rand(5)
print(arr, type(arr), arr.dtype) # <class 'numpy.ndarray'> float64

# 3) np.random.randn([갯수])
# 표준편차가 1이고 평균값이 0인 정규분포에서 표본 추출. 갯수 생략하면  1개반환
print("3. randn(5)")
arr = np.random.randn()
arr = np.random.randn(5)
print(arr)

# 4) np.random.randint(low, high, n)
# 주어진 최소/최대 범위 안에서 임의의 난수 n개 추출
print("4. randint(1,10,3)")
arr = np.random.randint(1,10,3) # 1~9
print(arr)

# 4) np.random.randint(high, size=n)
# 0 ~ 최대(exclusive) 범위안에서 임의의 정수 n개 반환, 복원추출(뽑고나서 다시 집어넣음)
print("4. randint(5, size=4): ")
arr = np.random.randint(5, size=4) #0~4
print(arr)
help(np.random.randint)
# 5) np.random.choice(리스트)
# 주어진 리스트에서 임의의 값 1개 반환
print("5. np.random.choice(['foo','bar','baz']")
choice_value = np.random.choice(['foo','bar','baz'])
print(choice_value)

# 6) np.random.shuffle(리스트)
# 주어진 리스트를 shuffle 함.  in-place(True)로 동작됨.
print("6. np.random.shuffle(1,3,56,7,98])")
shuffle_value = [1,3,56,7,98]
np.random.shuffle(shuffle_value)
print(shuffle_value)