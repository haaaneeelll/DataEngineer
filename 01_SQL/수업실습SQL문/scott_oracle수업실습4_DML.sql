-- Oracle DML

--  1. insert ��
-- 1) ���� ����
insert into dept(deptno, dname, loc )
values ( 50, '����', '����');

insert into dept(deptno, dname )
values ( 60, '����');

-- 2) ��Ƽ ����
create table copy_dept
as
select * from dept;

create table copy_dept2
as
select * from dept
where 1=2;


--  2. update ��
update dept
set dname ='�λ�', loc='����'
where deptno = 50;

-- 3. delete ��
delete from dept
where deptno = 50;
