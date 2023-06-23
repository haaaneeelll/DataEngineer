
import numpy as np

print(np.__version__)

# 1. np.zeros((행,열))
# shape만큼 0으로 채움. 기본 type은 float64
print("1. np.zeros(행,열):")
data = np.zeros((2,3))
# data = np.zeros((2,3), dtype=np.int32) # [0 0 0 0 0] int32
print(data, data.dtype) # [0. 0. 0. 0. 0. ] float64

# 2. np.ones((행,열))
# shape만큼  1.0 으로 채움. 기본 type은 float64
print("2. np.ones((행,열)):")
data = np.ones((2,3))
data = np.ones((2,3), dtype=np.int32)
print(data , data.dtype) # [1. 1. 1. 1. 1.] float64

# 3. np.empty((행,열))
# shape 만큼 임의의 값으로 채워짐 ==> 임의의 값으로 초기화 시킨 것
print("3. np.empty((2,9))")
data = np.empty((2,9))
# data = np.empty((2,9), dtype=np.int32)
print(data , data.dtype ) # [1868832878 1847620453 1965061231] int32

# 4. np.full((행,열), 값)
# shape 만큼 지정된 값으로 채워짐
print("4. full((2,3), 10)")
data = np.full((2,3), 10)
print(data) # [10 10 10 10 10]