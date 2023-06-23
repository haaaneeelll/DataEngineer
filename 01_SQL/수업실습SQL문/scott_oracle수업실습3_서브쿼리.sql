-- ��������
-- 1. ������ ��������
-- 1) where �� ��������
select empno, ename, job, sal
from emp
where sal > ( select sal
              from emp
              where ename ='WARD');
              
-- 2) �׷��Լ� �̿�
select empno, ename, job, sal
from emp
where sal > ( select avg(sal)
              from emp );


-- 2. ������ ��������
-- ������ �ּұ޿��� �޴� ��� ��ȸ
select empno, ename, job, sal
from emp
where sal IN ( select MIN(sal)
               from emp
               Group by job );
               
-- ������ MANAGER�� ����� �ּұ޿����� ���� �޿��� �޴� ��� ��ȸ               
select empno, ename, job, sal
from emp
where sal < ALL ( select sal
                  from emp
                  where job = 'MANAGER');
                  
-- ������ MANAGER�� ����� �ִ�޿����� ���� �޿��� �޴� ��� ��ȸ               
select empno, ename, job, sal
from emp
where sal > ALL ( select sal
                  from emp
                  where job = 'MANAGER');
                  
-- ������ MANAGER�� ����� �ִ�޿����� ���� �޿��� �޴� ��� ��ȸ               
select empno, ename, job, sal
from emp
where sal < ANY ( select sal
                  from emp
                  where job = 'MANAGER'); 
                  
                  
-- ������ MANAGER�� ����� �ּұ޿����� ���� �޿��� �޴� ��� ��ȸ               
select empno, ename, job, sal
from emp
where sal > ANY ( select sal
                  from emp
                  where job = 'MANAGER');
                  
-- exists
-- �������� ������� �����ϴ� ���
select *
from emp
where EXISTS ( select empno
               from emp
               where comm is not null );
               
-- �������� ������� �������� �ʴ� ���
select *
from emp
where EXISTS ( select empno
               from emp
               where ename is null );                  