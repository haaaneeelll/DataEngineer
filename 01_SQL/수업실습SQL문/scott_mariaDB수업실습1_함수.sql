
-- MariaDB 함수
-- 1) 단일행 함수 - 문자열

-- 첫글자대문자로 변경 - 지원안함

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

-- 특정 문자의 위치 반환 ( 시작위치 지정 불가 )
select instr('MILLER' , 'L' ) from dual;


-- 왼쪽 및 오른쪽, 양쪽 공백 제거
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
select round(456.789, -1) from DUAL;
select round(456.789, -2) from dual;

-- 절삭 ( 오라클의 trunc 대신에 truncate 함수 )
select truncate(456.789, 0) from DUAL;  -- 명시적으로 0 지정
select truncate(456.789, 2) from dual;
select truncate(456.789, -1) from dual;
select truncate(456.789, -2) from dual;

-- 3) 단일행 함수 - 날짜 및 시간

select SYSDATE(), NOW() from DUAL;
SELECT CURDATE(),  CURRENT_DATE(),  CURRENT_DATE FROM DUAL;
SELECT CURTIME(),  CURRENT_TIME(),  CURRENT_TIME FROM DUAL;


-- 두 날짜 사이의 일수 계산
select DATEDIFF('2023-01-04', '2022-01-04') from dual;

-- 날짜에 날짜 더하기 
SELECT DATE_ADD('2008-01-02', INTERVAL 1 DAY) as A1,
       DATE_ADD('2008-01-02', INTERVAL 1 MONTH) as A2,
       DATE_ADD('2008-01-02', INTERVAL 1 YEAR) as A3,
       NOW() as A4,
       DATE_ADD(NOW(), INTERVAL 10 MINUTE) as A5,
       DATE_ADD(NOW(), INTERVAL 2 HOUR) as A6
FROM DUAL;

-- 날짜에 날짜 빼기 
SELECT DATE_SUB('2008-01-02', INTERVAL 1 DAY) as B1,
       DATE_SUB('2008-01-02', INTERVAL 1 MONTH) as B2,
       DATE_SUB('2008-01-02', INTERVAL 1 YEAR) as B3,
       NOW() as B4,
       DATE_SUB(NOW(), INTERVAL 10 MINUTE) as B5,
       DATE_SUB(NOW(), INTERVAL 2 HOUR) as B6
 FROM DUAL;      
 
-- 명시된 날짜로부터 다음 요일에 대한 날짜를 반환 ( 지원 안됨 )

-- 월의 마지막 날 반환
select last_day(SYSDATE()) from dual;

-- 날짜에서 특정 정보만 얻기
SELECT NOW(),
       EXTRACT(SECOND FROM NOW()),
       EXTRACT(MINUTE FROM NOW()),
		 EXTRACT(HOUR FROM NOW()),
		 EXTRACT(DAY FROM NOW()),
		 EXTRACT(MONTH FROM NOW()),
		 EXTRACT(YEAR FROM NOW()),
		 EXTRACT(YEAR_MONTH FROM NOW())
from dual;

-- 4) 단일행 함수 - 변환함수

-- 문자를 숫자로 변환
select CAST('100' AS INT )+100 from dual;

-- 숫자를 문자로 변환
select CAST(1000 AS CHAR ) from dual;


-- 문자를 날짜로 변환
SELECT STR_TO_DATE('2020-03-04','%Y-%m-%d'),
       STR_TO_DATE('01,5,2013','%d,%m,%Y'),
       STR_TO_DATE('2020년03월05일','%Y년%m월%d일')
from dual;

-- 날짜를 문자로 변환
SELECT NOW(),
       DATE_FORMAT(NOW(),'%Y%m%d'),
       DATE_FORMAT(NOW(),'%Y/%m/%d'),
       DATE_FORMAT(NOW(),'%Y년%m월 %d일'),
       DATE_FORMAT(NOW(),'%H:%i:%S'),
		 DATE_FORMAT(NOW(),'%Y')
from dual;


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
select max(sal), min(sal), sum(sal), avg(sal), COUNT(*)
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