import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc("font", family="Malgun Gothic")
plt.rc("axes", unicode_minus=False)
# plt.rc('ytick', labelsize=8)
# plt.rc('xtick', labelsize=8)
# plt.rc('legend', fontsize=8)
# plt.rc('figure', titlesize=8)
plt.style.use("fivethirtyeight")

df = pd.read_csv("seoul_covid_10_07_.csv", encoding='utf-8')
## 문제 1. 제공된 파일의 데이터의 행과 열의 크기
print("1. 제공된 파일의 데이터의 행과 열의 크기: \n", df.shape)
print()
## 문제 2. 첫번째 데이터부터 10개 까지만 출력
print("2. 첫번째 데이터부터 10개 까지만 출력: \n", df.head(10))
print()
## 문제 3. 마지막 데이터부터 3개 까지만 출력
print("3. 마지막 데이터부터 3개 까지만 출력: \n", df.tail(3))

