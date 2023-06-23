
-- ����Ŭ �Լ�
-- 1) ������ �Լ� - ���ڿ�

-- ù���ڴ빮�ڷ� ����
select initcap('ORACLE SERVER') from dual;
select deptno, initcap(dname), initcap(loc) from dept;

-- �ҹ��� �� �빮�ڷ� ����
select lower('MANAGER'), upper('manager') from dual;

select empno, ename, deptno
from emp
where lower(ename) ='smith';

-- ���ڿ� ����
select concat('ORACLE','SERVER') from dual;
select empno, ename, job, concat(ename, job)
from emp;

-- ���� �� ������ ���ڿ� �����
select lpad('MILLER', 10), rpad('MILLER',10) from dual;
select lpad('MILLER', 10, '*'), rpad('MILLER',10, '*') from dual;
select ename, lpad(ename, 15, '*') from emp;

-- �κп� ��ȯ
select substr('000101-3234232', 8, 1 ) from dual;

-- ���ڿ� ����
select length('000101-3234232') from dual;

-- ���ڿ� ġȯ
select replace('JACK and JUE', 'J', 'BL') from dual;

-- Ư�� ������ ��ġ ��ȯ
select instr('MILLER' , 'L', 1 ) from dual;
select instr('MILLER' , 'L', 1, 2 ) from dual;
select instr('MILLER' , 'L', 5 ) from dual;

-- ���� �� ������, ���� ����(����) ����
select LTRIM('MILLERM', 'M') from dual;
select RTRIM('MILLERM', 'M') from dual;

select LTRIM('     MILLERM      ') from dual;
select RTRIM('     MILLERM      ') from dual;

select TRIM(leading 1 from 111234561111 ) from dual;
select TRIM(trailing 1 from 111234561111 ) from dual;
select TRIM(both 1 from 111234561111 ) from dual;


-- 2) ������ �Լ� - ��ġ

-- �ø��� ( �־��� ���ں��� ũ�ų� ���� �ּ� ���� )
select ceil(10.1 ) from dual;

-- ������ ( �־��� ���ں��� �۰ų� ���� �ִ� ���� )
select floor(10.1 ) from dual;

-- ������
select mod(10,3) from dual;

-- �ݿø�
select round(456.789) from dual;
select round(456.789, 2) from dual;
select round(456.789, -1) from dual;
select round(456.789, -2) from dual;

-- ����
select trunc(456.789) from dual;
select trunc(456.789, 2) from dual;
select trunc(456.789, -1) from dual;
select trunc(456.789, -2) from dual;

-- 3) ������ �Լ� - ��¥
select sysdate, systimestamp from dual;

select sysdate, sysdate + 1, sysdate - 1 from dual;

-- �� ��¥ ������ ���� ���
select months_between(sysdate+100, sysdate) from dual;

-- ���� ��¥�� ���ϰų� ����
select add_months(sysdate, 1), add_months(sysdate, -1) from dual;

-- ��õ� ��¥�κ��� ���� ���Ͽ� ���� ��¥�� ��ȯ
select next_day(sysdate, 'ȭ') from dual;

-- ���� ������ �� ��ȯ
select last_day(sysdate) from dual;

-- ��¥ �ݿø�
select round(sysdate, 'YEAR'), round(sysdate, 'MONTH') from dual;

-- ��¥ ����
select trunc(sysdate, 'YEAR'), trunc(sysdate, 'MONTH') from dual;

-- 4) ������ �Լ� - ��ȯ�Լ�

-- ���ڸ� ���ڷ� ��ȯ
select to_number('100')+100 from dual;

--select to_number('1,000')+100 from dual;
--select to_number('1,000','999,999')+100 from dual;


-- ���ڸ� ���ڷ� ��ȯ
select to_char(1000) from dual;
select to_char(1000, 'L999,999') from dual;
select to_char(1000, '$999,999') from dual;
select to_char(100000000, '$999,999,999') from dual;

-- ���ڸ� ��¥�� ��ȯ
select to_date('2023/05/23')from dual;

select to_date('20230523')from dual;
select to_date('2023,05,23','YYYY,MM,dd')from dual;

--select to_date('20230523124554')from dual;
--alter session set NLS_DATE_FORMAT='YYYY/MM/dd HH:MI:SS';
select to_date('20230523124554','YYYYMMddHHMISS')from dual;


--select to_date('2023��05��23')from dual;
select to_date('2023��05��23��', 'YYYY"��"MM"��"dd"��"')from dual;

-- 5) ������ �Լ� - case �Լ�
select empno, ename, sal, job,
      case job when 'ANALYST' then sal*1.1
               when 'CLERK' then sal*1.2
               when 'MANAGER' then sal*1.3
               when 'PRESIDENT' then sal*1.4
               when 'SALESMAN' then sal*1.5
      END "�޿�"
from emp;

select empno, ename, 
       CASE when sal >=0 and sal <=1000 then 'E' 
            when sal >1000 and sal <=2000 then 'D'
            when sal >2000 and sal <=3000 then 'C'
            when sal >3000 and sal <=4000 then 'B'
            when sal >5000 and sal <=5000 then 'A'
      END "���"
from emp;


-- 2) �׷��Լ�
select max(sal), min(sal), sum(sal), avg(sal), count(*)
from emp;

-- group by ��
select deptno, sum(sal)
from emp
group by deptno;

-- having ��
select deptno, sum(sal)
from emp
group by deptno
having sum(sal) > 8000;

