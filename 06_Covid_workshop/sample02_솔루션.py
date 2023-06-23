import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc("font", family="Malgun Gothic")
plt.rc("axes", unicode_minus=False)
# plt.rc('ytick', labelsize=8)
# plt.rc('xtick', labelsize=8)
# plt.rc('legend', fontsize=8)
# plt.rc('figure', titlesize=8)
# plt.style.use("fivethirtyeight")

df = pd.read_csv("seoul_covid_10_07_.csv", encoding='utf-8')

## 문제 1. "연번"을 기준으로  오름차순으로 정렬
df = df.sort_values(by="연번", ascending=True)
print("1. 연번 기준으로 오름차순으로 정렬: \n", df.head())
print()
## 문제 2. 확진일의 빈도수, 어느 날짜에 가장 많이 확진이 되었는지 확인
# "확진일" 컬럼의 데이터가 날짜 형태가 아니라 문자형태
print("2. 확진일의 빈도수 확인: \n",  df["확진일"].value_counts().head())
print()
## 문제 3. 연도가 없기 때문에 2020년을 날짜에 추가하고 "-" 문자로 새로운 '확진일자' 컬럼 추가
# 데이터 타입을 변경해서 날짜형태로 변환 ==> pd.to_date() 함수 사용
df["확진일자"] = pd.to_datetime("2020-"+ df["확진일"].str.replace(".", "-", regex=False))
print(df[["확진일", "확진일자"]].head())
print("3. '확진일자' 컬럼 추가: \n", df.head())
print()
## 문제 4. '확진일자' 컬럼을 활용하여 '월' 컬럼 추가
df["월"] = df["확진일자"].dt.month
print("4. '월' 컬럼 추가: \n", df.head())
print()
## 문제 5. '확진일자' 컬럼을 활용하여 해당 연도의 몇번째 "주(week)"인지  컬럼 추가
df["주"] = df["확진일자"].dt.isocalendar().week
print("5. '주' 컬럼 추가: \n", df.head())
print()
## 문제 6. '확진일자' 컬럼을 활용하여  "월-일" 컬럼 추가
df["월-일"] = df["확진일자"].astype(str).map(lambda x : x[-5:])
print("6. '월일' 컬럼 추가: \n", df.head())
print()

## 문제 7. “월-일” 컬럼을 활용 확진자가 가장 많이 나온 '월-일' 확인
# day_count = df["월-일"].value_counts().sort_values(ascending=False)
# print(day_count)
# print(day_count.max())
# print("7. 확진자가 가장 많이 나온날 확인: \n", day_count[day_count == day_count.max()])
print("7. 확진자가 가장 많이 나온 '월-일' 확인: \n",df["월-일"].value_counts().index[0])
print()
## 문제 8. 확진자가 가장 많았던 날의 확진자들의 이력 정보
max_day = df["월-일"].value_counts().index[0]
print("8. 확진자가 가장 많았던 날의 확진자들의 이력 정보: \n", df[df["월-일"] == max_day])

##################  시각화   ####################

## 문제 9. 확진일자별 확진자수를 선그래프로 시각화
#####DataFrame.plot 버전 시작#################
# df['확진일자'].value_counts().sort_index().plot(title = "일자별 확진자수", figsize=(15,4))
# plt.axhline(30, color='r', linestyle="--")
# plt.show()
######DataFrame.plot 버전 끝#############
# plt.figure(figsize=(15,4))
# plt.plot(df['확진일자'].value_counts().sort_index())
# plt.title("일자별 확진자수")
# plt.axhline(100, color='r', linestyle="--")
# plt.show()

## 문제 10. 확진일자별 확진자수를 선그래프로 시각화 + 값 설정
#####DataFrame.plot 버전 시작#################
# day_count = df["월-일"].value_counts().sort_index()
# g = day_count.plot(figsize=(20,4))
# print(g)
# for i in range(len(day_count)):
#     case_count = day_count.iloc[i]
#     if case_count > 50:
#         print(i, case_count)
#         g.text(x=i, y=case_count, s=case_count)
# plt.axhline(50, color='r', linestyle="--")
# plt.show()
######DataFrame.plot 버전 끝#############
# day_count =df['확진일자'].value_counts().sort_index()
# print(day_count)
# plt.figure(figsize=(15,4))
# plt.plot(day_count)
# for i in range(len(day_count)):
#     case_day = day_count.index[i]
#     case_count = day_count.iloc[i]
#     if case_count > 150:
#         print(i, case_count)
#         plt.text(x=case_day, y=case_count, s=f"{case_count}명") # text(x좌표, y좌표, 표시값)
# plt.title("일자별 확진자수")
# plt.axhline(100, color='r', linestyle="--")
# plt.show()

## 문제 11. "월"별 확진자수를  막대그래프로 시각화 + text 설정
# day_count =df['월'].value_counts()
# print(day_count)
# plt.figure(figsize=(15,4))
# plt.bar(day_count.index, day_count)
#
# for i in range(len(day_count)):
#     case_day = day_count.index[i]
#     case_count = day_count.iloc[i]
#     if case_count > 150:
#         print(i, case_count)
#         plt.text(x=case_day, y=case_count, s=f"{case_count}명") # text(x좌표, y좌표, 표시값)
# plt.title("월별 확진자수")
# plt.show()

