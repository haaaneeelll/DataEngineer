
-- 테이블 변경
create table my_dept
as
select * from dept;


-- 컬럼 추가
alter table my_dept
add ( tel varchar(20));

-- 타입 변경 () 사용불가
alter table my_dept
modify  tel INT ;

-- 컬럼 삭제 () 사용불가
alter table my_dept
drop  tel ;

-- 제약조건 추가
alter table my_dept
add constraint  PRIMARY KEY(deptno);

-- 제약조건 삭제
alter table my_dept
drop primary KEY;

SELECT * 
FROM information_schema.table_constraints
WHERE TABLE_NAME = 'DEPT';


-- 테이블 삭제
-- DROP TABLE [IF EXISTS]  table명, … 
DROP TABLE IF EXISTS my_dept;

