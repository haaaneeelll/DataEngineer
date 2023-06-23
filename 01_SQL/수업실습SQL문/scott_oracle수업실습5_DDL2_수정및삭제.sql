
-- 테이블 변경
create table my_dept
as
select * from dept;


-- 컬럼 추가
alter table my_dept
add ( tel varchar(20));

-- 타입 변경
alter table my_dept
modify ( tel number(10));

-- 컬럼 삭제
alter table my_dept
drop ( tel );

-- 제약조건 추가
alter table my_dept
add constraint my_dept_deptno_pk PRIMARY KEY(deptno);

-- 제약조건 삭제
alter table my_dept
drop primary key;


-- 테이블 삭제
-- DROP TABLE  table명 
DROP TABLE  my_dept;
