show user;

-- �ּ���, ����ȵǴ� ����(����๮)

-- 1. ���̺� ����
select * from tab;
select *
from tab;

select * from user_tables;


-- 3.  ��� �÷� ����
select *
from dept;

select *
from emp;

--  4.  �÷��� ���
select deptno, loc
from dept;

select loc, deptno
from dept;

-- 5.  �÷��� ��Ī ==> �÷��� as ��Ī , as �������� , " "  ����Ͽ� ���е� ���ڿ��� ���� �� �ִ�.
--  SQL������ "" ����ϴ� ���� ��Ī�� �����ϴ�. ����(���ڿ�) ǥ���� '' ����Ѵ�.
select deptno as �μ���ȣ, loc ��ġ
from dept;

select deptno as "�μ� ��ȣ", loc ��ġ
from dept;

-- 6. ���� ����
select empno, sal, sal + 100  as  ���ʽ�
from emp;

-- 7. ���� ����, �� || �� (������������) , ��? �÷� || �÷�,   �� || �� , �÷� || ��
-- ��?  ��ġ: 10 ,  3.15  ����(���ڿ�):   'A' , 'ȫ', 'ABC', 'ȫ�浿'
select ename || sal as �̸�������
from emp;

select deptno || ename || sal 
from emp;

select ename ||  ' ���'
from emp;

-- 8. �ߺ��� ����: distinct
-- emp �� � job ?
select job
from emp;

select distinct job
from emp;

-- select distinct �÷���,�÷��� as ��Ī, �÷� || �÷�(��),  �÷� + 100,
-- oracle ������ from �� �ʼ�
-- select ~ from ���� �׻� ��� ���ڵ� ��µȴ�. ==> �׻� 12���� ����
-- projection (�÷� ����)


-- 9. null�� ����
select empno, sal, comm, (sal*12) + comm
from emp;

select empno, ename,sal, comm, (sal*12) + nvl(comm,0)
from emp;

-- ������
-- ��. �񱳿�����
select empno, ename, sal
from emp
where sal = 800;

-- ����:  �̸��� ford ã��?
select empno, ename, sal
from emp
where ename = 'ford';

-- SQL���� �ĺ��ڸ� ��ҹ��ڸ� �������� �ʴ´�.  ���� �����Ѵ�. (  mariadb�� ���� �������Ѵ�.)
SELECT empno, ename, sal
from EMP
where ename = 'FORD';

-- ����: �Ի����� 80/12/17 ��� �˻�?
SELECT empno, ename, sal, hiredate
from EMP
where hiredate = '80/12/17';

-- ��. ����  between A and B :  A �� B �� ���Ե�.   ��ġ �� ��¥(���������� ��ġó��) ��� ����
SELECT empno, ename, sal, hiredate
from EMP
where sal BETWEEN 800 AND 2000;

SELECT empno, ename, sal, hiredate
from EMP
where hiredate BETWEEN '80/01/10' AND '80/12/31';

-- ��. �Ѳ����� ������ ����  ==> ���������� �Ǵ� ���� �����.
SELECT empno, ename, sal, hiredate
from EMP
where sal IN (800, 1500, 2000); -- ��ġ���� '' ���� ���

SELECT empno, ename, sal, hiredate
from EMP
where ename IN ('SMITH','FORD');

SELECT empno, ename, sal, hiredate
from EMP
where hiredate IN ('80/12/17','80/12/01');

-- ��. null �� ã��. is null
SELECT empno, ename, sal, hiredate
from EMP
where comm is null;

SELECT empno, ename, sal, hiredate
from EMP
where comm is not null; -- null ����

-- ��. ����� �� ã��   like +   % �Ǵ� _
SELECT empno, ename, sal, hiredate
from EMP
where ename LIKE 'A%'; -- A�� �����ϴ� ��� ��ȸ

SELECT empno, ename, sal, hiredate
from EMP
where ename LIKE '%T%'; -- T�� �����ϴ� ��� ��ȸ

SELECT empno, ename, sal, hiredate
from EMP
where ename LIKE '%S'; -- S��  ������ ��� ��ȸ

SELECT empno, ename, sal, hiredate
from EMP
where ename LIKE '_L%';  -- �ι�° L �� ��� ��ȸ

-- ����: �̸��� 5�����̰� �������� N���� ������ ���  ��ȸ?
SELECT empno, ename, sal, hiredate
from EMP
where ename LIKE '____N'; -- _ 4 �� ����

-- ��. �� ������:   and (�׸���): ��� �����ؾ� ��ȯ��. , or(�Ǵ�): �ϳ��� �����ϸ� ��ȯ�� ,  not(����)
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

-- ����
-- 1. order by �÷���
SELECT empno, ename, sal, hiredate
from EMP
order by sal; -- �⺻�� ��������

SELECT empno, ename, sal, hiredate
from EMP
order by sal asc; --  ��������� asc ����. ��������, ascending

SELECT empno, ename, sal, hiredate
from EMP
order by sal desc;  -- descending  ��������

-- 2. order by ��Ī
SELECT empno, ename, sal as salary, hiredate
from EMP
order by salary;

-- 3. order by �÷�����
SELECT sal as salary, empno, ename,  hiredate
from EMP
order by 1;


-- 4. ���� ���� : order by �÷���1, �÷���2 ==> �÷���1���� �����ϰ� ���� ���� �÷���2�� ������
SELECT empno, ename, sal as salary, hiredate
from EMP
order by salary,hiredate ;

SELECT empno, ename, sal as salary, hiredate
from EMP
order by salary, hiredate desc ;

SELECT empno, ename, sal as salary, hiredate
from EMP
order by 3, 4 desc ;
