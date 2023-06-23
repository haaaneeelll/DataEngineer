-- Oracle DML
-- transaction
-- autocommit 설정값 확인
show variables like 'autocommit%';
SET autocommit=FALSE;


--  1. insert 문
-- 1) 단일 생성
insert into dept(deptno, dname, loc )
values ( 50, '개발', '서울');

insert into dept(deptno, dname )
values ( 60, '개발');

-- 2) 멀티 생성
create table copy_dept
as
select * from dept;
SELECT * FROM copy_dept;

create table copy_dept2
as
select * from dept
where 1=2;
SELECT * FROM copy_dept2;

--  2. update 문
update dept
set dname ='인사', loc='제주'
where deptno = 50;

-- 3. delete 문
delete from dept
where deptno = 50;
