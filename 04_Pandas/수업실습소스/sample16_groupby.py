'''
   groupby
   https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html

   # 1. 기본
     df.groupby('그룹으로묶을컬럼명')[선택컬럼].그룹함수
     예> emp.groupby(by="deptno")["sal"].sum()

   # 2. apply 또는 agg 또는 aggregate 함수
     df.groupby('그룹으로묶을컬럼명')[선택컬럼].agg(함수명)
     df.groupby('그룹으로묶을컬럼명')[선택컬럼].agg([함수명,함수명1,..])

  # 3.  여러 컬럼에 다양한 함수 적용
     df.groupby('그룹으로묶을컬럼명').agg({
         컬럼명1:[그룹함수,그룹함수],
         컬럼명2:[그룹함수,그룹함수]
      })
'''
import pandas as pd
import numpy as np

department = {"deptno":[10,20,30,40],'dname':['개발','인사','영업','관리'],'loc':['서울','부산','제주','광주']}
employee = {"empno":['A1','A2','A3','A4','A5'],"ename":['홍길동','유관순','안중근','강감찬','이순신'],
            "sal":[1000,1500,2300,3400,4500],"hireday":['2019/01/02','2018/01/02','2017/01/02','2016/01/02','2015/01/02'],
            "deptno":[10,20,10,30,10]}
dept = pd.DataFrame(department)
emp = pd.DataFrame(employee)

print(dept)
print(emp)
'''
  empno ename   sal     hireday  deptno
0    A1   홍길동  1000  2019/01/02      10
1    A2   유관순  1500  2018/01/02      20
2    A3   안중근  2300  2017/01/02      10
3    A4   강감찬  3400  2016/01/02      30
4    A5   이순신  4500  2015/01/02      10
'''
# 1. 부서별  sal 합,평균, 최대, 최소, 갯수?
xxx = emp.groupby(by="deptno")["sal"].sum()
xxx = emp.groupby(by="deptno")["sal"].mean()
xxx = emp.groupby(by="deptno")["sal"].max()
xxx = emp.groupby(by="deptno")["sal"].min()
xxx = emp.groupby(by="deptno")["sal"].count()
print(xxx)
print(pd.DataFrame(xxx))
'''
       sal
deptno     
10        3
20        1
30        1
'''

# 2. apply 또는 agg 함수 적용
def my_mean(v):
    print(">>", v) # deptno별 sal 값 전달됨
    n = len(v)
    sum=0
    for k in v:
        sum+=k
    return sum/n

xxx = emp.groupby(by="deptno")["sal"].agg(my_mean) #사용자 정의함수
print(xxx)
xxx = emp.groupby(by="deptno")["sal"].agg(np.mean) # numpy의 그룹함수
print(xxx)
xxx = emp.groupby(by="deptno")["sal"].agg("mean")  # python의 그룹함수
print(xxx)

# 3. apply 또는 agg 함수 적용 - 멀티함수 적용
xxx = emp.groupby(by="deptno")["sal"].agg([np.sum, np.mean, np.max, np.size]) # numpy의 그룹함수
xxx = emp.groupby(by="deptno")["sal"].agg(["sum","mean","max","count"]) # python의 그룹함수
xxx = emp.groupby(by="deptno")["sal"].agg([sum,max]) # python의 그룹함수

# 3.여러 컬럼에 다양한 함수 적용
xxx = emp.groupby(by="deptno").agg({
    "sal":["sum","max","min"],
    "deptno":["count"]
})
print(xxx)

# emp와 dept 병합후에 groupby 적용 해보기