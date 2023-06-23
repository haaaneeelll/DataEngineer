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
'''
  구현하기
'''
print()
## 문제 2. 확진일의 빈도수, 어느 날짜에 가장 많이 확진이 되었는지 확인
# "확진일" 컬럼의 데이터가 날짜 형태가 아니라 문자형태
'''
  구현하기
'''
print()
## 문제 3. 연도가 없기 때문에 2020년을 날짜에 추가하고 "-" 문자로 새로운 '확진일자' 컬럼 추가
# 데이터 타입을 변경해서 날짜형태로 변환 ==> pd.to_date() 함수 사용
'''
  구현하기
'''
print()
## 문제 4. '확진일자' 컬럼을 활용하여 '월' 컬럼 추가
'''
  구현하기
'''
print()
## 문제 5. '확진일자' 컬럼을 활용하여 해당 연도의 몇번째 "주(week)"인지  컬럼 추가
'''
  구현하기
'''
print()
## 문제 6. '확진일자' 컬럼을 활용하여  "월-일" 컬럼 추가
'''
  구현하기
'''
print()

## 문제 7. “월-일” 컬럼을 활용 확진자가 가장 많이 나온 '월-일' 확인
'''
  구현하기
'''
print()
## 문제 8. 확진자가 가장 많았던 날의 확진자들의 이력 정보
'''
  구현하기
'''

##################  시각화   ####################

## 문제 9. 확진일자별 확진자수를 선그래프로 시각화
'''
  구현하기
'''

## 문제 10. 확진일자별 확진자수를 선그래프로 시각화 + 값 설정
'''
  구현하기
'''

## 문제 11. "월"별 확진자수를  막대그래프로 시각화 + text 설정
'''
  구현하기
'''

