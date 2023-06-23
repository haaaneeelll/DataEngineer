
-- 오라클 함수
-- 1) 단일행 함수 - 문자열

-- 첫글자대문자로 변경
select initcap('ORACLE SERVER') from dual;
select deptno, initcap(dname), initcap(loc) from dept;

-- 소문자 및 대문자로 변경
select lower('MANAGER'), upper('manager') from dual;

select empno, ename, deptno
from emp
where lower(ename) ='smith';

-- 문자열 연결
select concat('ORACLE','SERVER') from dual;
select empno, ename, job, concat(ename, job)
from emp;

-- 왼쪽 및 오른쪽 문자열 끼우기
select lpad('MILLER', 10), rpad('MILLER',10) from dual;
select lpad('MILLER', 10, '*'), rpad('MILLER',10, '*') from dual;
select ename, lpad(ename, 15, '*') from emp;

-- 부분열 반환
select substr('000101-3234232', 8, 1 ) from dual;

-- 문자열 길이
select length('000101-3234232') from dual;

-- 문자열 치환
select replace('JACK and JUE', 'J', 'BL') from dual;

-- 특정 문자의 위치 반환
select instr('MILLER' , 'L', 1 ) from dual;
select instr('MILLER' , 'L', 1, 2 ) from dual;
select instr('MILLER' , 'L', 5 ) from dual;

-- 왼쪽 및 오른쪽, 양쪽 공백(문자) 제거
select LTRIM('MILLERM', 'M') from dual;
select RTRIM('MILLERM', 'M') from dual;

select LTRIM('     MILLERM      ') from dual;
select RTRIM('     MILLERM      ') from dual;

select TRIM(leading 1 from 111234561111 ) from dual;
select TRIM(trailing 1 from 111234561111 ) from dual;
select TRIM(both 1 from 111234561111 ) from dual;


-- 2) 단일행 함수 - 수치

-- 올림값 ( 주어진 숫자보다 크거나 같은 최소 정수 )
select ceil(10.1 ) from dual;

-- 내림값 ( 주어진 숫자보다 작거나 같은 최대 정수 )
select floor(10.1 ) from dual;

-- 나머지
select mod(10,3) from dual;

-- 반올림
select round(456.789) from dual;
select round(456.789, 2) from dual;
select round(456.789, -1) from dual;
select round(456.789, -2) from dual;

-- 절삭
select trunc(456.789) from dual;
select trunc(456.789, 2) from dual;
select trunc(456.789, -1) from dual;
select trunc(456.789, -2) from dual;

-- 3) 단일행 함수 - 날짜
select sysdate, systimestamp from dual;

select sysdate, sysdate + 1, sysdate - 1 from dual;

-- 두 날짜 사이의 월수 계산
select months_between(sysdate+100, sysdate) from dual;

-- 월을 날짜에 더하거나 빼기
select add_months(sysdate, 1), add_months(sysdate, -1) from dual;

-- 명시된 날짜로부터 다음 요일에 대한 날짜를 반환
select next_day(sysdate, '화') from dual;

-- 월의 마지막 날 반환
select last_day(sysdate) from dual;

-- 날짜 반올림
select round(sysdate, 'YEAR'), round(sysdate, 'MONTH') from dual;

-- 날짜 절삭
select trunc(sysdate, 'YEAR'), trunc(sysdate, 'MONTH') from dual;

-- 4) 단일행 함수 - 변환함수

-- 문자를 숫자로 변환
select to_number('100')+100 from dual;

--select to_number('1,000')+100 from dual;
--select to_number('1,000','999,999')+100 from dual;


-- 숫자를 문자로 변환
select to_char(1000) from dual;
select to_char(1000, 'L999,999') from dual;
select to_char(1000, '$999,999') from dual;
select to_char(100000000, '$999,999,999') from dual;

-- 문자를 날짜로 변환
select to_date('2023/05/23')from dual;

select to_date('20230523')from dual;
select to_date('2023,05,23','YYYY,MM,dd')from dual;

--select to_date('20230523124554')from dual;
--alter session set NLS_DATE_FORMAT='YYYY/MM/dd HH:MI:SS';
select to_date('20230523124554','YYYYMMddHHMISS')from dual;


--select to_date('2023년05월23')from dual;
select to_date('2023년05월23일', 'YYYY"년"MM"월"dd"일"')from dual;

-- 5) 단일행 함수 - case 함수
select empno, ename, sal, job,
      case job when 'ANALYST' then sal*1.1
               when 'CLERK' then sal*1.2
               when 'MANAGER' then sal*1.3
               when 'PRESIDENT' then sal*1.4
               when 'SALESMAN' then sal*1.5
      END "급여"
from emp;

select empno, ename, 
       CASE when sal >=0 and sal <=1000 then 'E' 
            when sal >1000 and sal <=2000 then 'D'
            when sal >2000 and sal <=3000 then 'C'
            when sal >3000 and sal <=4000 then 'B'
            when sal >5000 and sal <=5000 then 'A'
      END "등급"
from emp;


-- 2) 그룹함수
select max(sal), min(sal), sum(sal), avg(sal), count(*)
from emp;

-- group by 절
select deptno, sum(sal)
from emp
group by deptno;

-- having 절
select deptno, sum(sal)
from emp
group by deptno
having sum(sal) > 8000;

