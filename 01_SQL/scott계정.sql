show user;

-- 주석문, 실행안되는 문장(비실행문)

-- 1. 테이블 보기
select * from tab;
select *
from tab;

select * from user_tables;


-- 3.  모든 컬럼 보기
select *
from dept;

select *
from emp;

--  4.  컬럼명 명시
select deptno, loc
from dept;

select loc, deptno
from dept;

-- 5.  컬럼명 별칭 ==> 컬럼명 as 별칭 , as 생략가능 , " "  사용하여 구분된 문자열을 묶을 수 있다.
--  SQL문에서 "" 사용하는 경우는 별칭이 유일하다. 문자(문자열) 표현은 '' 사용한다.
select deptno as 부서번호, loc 위치
from dept;

select deptno as "부서 번호", loc 위치
from dept;

-- 6. 연산 가능
select empno, sal, sal + 100  as  보너스
from emp;

-- 7. 연결 가능, 값 || 값 (파이프연산자) , 예? 컬럼 || 컬럼,   값 || 값 , 컬럼 || 값
-- 값?  수치: 10 ,  3.15  문자(문자열):   'A' , '홍', 'ABC', '홍길동'
select ename || sal as 이름과월급
from emp;

select deptno || ename || sal 
from emp;

select ename ||  ' 사원'
from emp;

-- 8. 중복값 제거: distinct
-- emp 에 어떤 job ?
select job
from emp;

select distinct job
from emp;

-- select distinct 컬럼명,컬럼명 as 별칭, 컬럼 || 컬럼(값),  컬럼 + 100,
-- oracle 에서는 from 절 필수
-- select ~ from 절은 항상 모든 레코드 출력된다. ==> 항상 12개가 나옴
-- projection (컬럼 선택)


-- 9. null값 연산
select empno, sal, comm, (sal*12) + comm
from emp;

select empno, ename,sal, comm, (sal*12) + nvl(comm,0)
from emp;

-- 연산자
-- 가. 비교연산자
select empno, ename, sal
from emp
where sal = 800;

-- 문제:  이름이 ford 찾기?
select empno, ename, sal
from emp
where ename = 'ford';

-- SQL문은 식별자를 대소문자를 구별하지 않는다.  값은 구별한다. (  mariadb는 값도 구별안한다.)
SELECT empno, ename, sal
from EMP
where ename = 'FORD';

-- 문제: 입사일이 80/12/17 사원 검색?
SELECT empno, ename, sal, hiredate
from EMP
where hiredate = '80/12/17';

-- 나. 범위  between A and B :  A 와 B 는 포함됨.   수치 및 날짜(내부적으로 수치처리) 사용 가능
SELECT empno, ename, sal, hiredate
from EMP
where sal BETWEEN 800 AND 2000;

SELECT empno, ename, sal, hiredate
from EMP
where hiredate BETWEEN '80/01/10' AND '80/12/31';

-- 다. 한꺼번에 여러개 지정  ==> 내부적으로 또는 으로 연산됨.
SELECT empno, ename, sal, hiredate
from EMP
where sal IN (800, 1500, 2000); -- 수치형은 '' 없이 사용

SELECT empno, ename, sal, hiredate
from EMP
where ename IN ('SMITH','FORD');

SELECT empno, ename, sal, hiredate
from EMP
where hiredate IN ('80/12/17','80/12/01');

-- 라. null 값 찾기. is null
SELECT empno, ename, sal, hiredate
from EMP
where comm is null;

SELECT empno, ename, sal, hiredate
from EMP
where comm is not null; -- null 부정

-- 마. 비슷한 값 찾기   like +   % 또는 _
SELECT empno, ename, sal, hiredate
from EMP
where ename LIKE 'A%'; -- A로 시작하는 사원 조회

SELECT empno, ename, sal, hiredate
from EMP
where ename LIKE '%T%'; -- T가 포함하는 사원 조회

SELECT empno, ename, sal, hiredate
from EMP
where ename LIKE '%S'; -- S로  끝나는 사원 조회

SELECT empno, ename, sal, hiredate
from EMP
where ename LIKE '_L%';  -- 두번째 L 인 사원 조회

-- 문제: 이름이 5글자이고 마지막은 N으로 끝나는 사원  조회?
SELECT empno, ename, sal, hiredate
from EMP
where ename LIKE '____N'; -- _ 4 개 지정

-- 바. 논리 연산자:   and (그리고): 모두 만족해야 반환됨. , or(또는): 하나라도 만족하면 반환됨 ,  not(부정)
SELECT empno, ename, sal, hiredate
from EMP
where job = 'SALESMAN' and sal >= 1500;

SELECT empno, ename, sal, hiredate
from EMP
where job = 'SALESMAN' or sal >= 1500;

SELECT empno, ename, sal
from EMP
where NOT ename = 'FORD';

SELECT empno, ename, sal, hiredate
from EMP
where NOT ename IN ('SMITH','FORD');

-- 정렬
-- 1. order by 컬럼명
SELECT empno, ename, sal, hiredate
from EMP
order by sal; -- 기본은 오름차순

SELECT empno, ename, sal, hiredate
from EMP
order by sal asc; --  명시적으로 asc 지정. 오름차순, ascending

SELECT empno, ename, sal, hiredate
from EMP
order by sal desc;  -- descending  내림차순

-- 2. order by 별칭
SELECT empno, ename, sal as salary, hiredate
from EMP
order by salary;

-- 3. order by 컬럼순서
SELECT sal as salary, empno, ename,  hiredate
from EMP
order by 1;


-- 4. 다중 정렬 : order by 컬럼명1, 컬럼명2 ==> 컬럼명1으로 정렬하고 같은 행은 컬럼명2로 재정렬
SELECT empno, ename, sal as salary, hiredate
from EMP
order by salary,hiredate ;

SELECT empno, ename, sal as salary, hiredate
from EMP
order by salary, hiredate desc ;

SELECT empno, ename, sal as salary, hiredate
from EMP
order by 3, 4 desc ;
