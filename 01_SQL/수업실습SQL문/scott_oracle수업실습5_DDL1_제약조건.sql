-- DDL

--1) 테이블 생성
create table dept_2
( deptno number(2),
  dname varchar2(10),
  loc varchar2(10));

-- 2) default  
create table dept_3
( deptno number(2),
  dname varchar2(10),
  loc varchar2(10) default '서울');  

insert into dept_3(deptno,dname) 
values ( 1, '개발');
select * from dept_3;
  
-- 3) 제약조건
-- 가. primary key ( 컬럼 레벨 )
create table table1
( no number(2) constraint table1_no_pk PRIMARY KEY,
  email varchar2(20));

--  primary key ( 테이블 레벨 )
create table table2
( no number(2),
  email varchar2(20),
  constraint table2_no_pk PRIMARY KEY(no)
  );
  
-- 나. unique ( 컬럼 레벨 )
create table table3
( no number(2) constraint table3_no_uk UNIQUE,
  email varchar2(20));

--  unique ( 테이블 레벨 )
create table table4
( no number(2),
  email varchar2(20),
  constraint table4_no_uk UNIQUE(no)
  );
  
-- 다. check ( 컬럼 레벨 )
create table table5
( no number(2) constraint table5_no_ck CHECK(no in (10,20)),
  email varchar2(20));

--  check ( 테이블 레벨 )
create table table6
( no number(2),
  email varchar2(20),
  constraint table6_no_ck CHECK(no in (10,20))
  );
  
-- 라. not null ( 컬럼 레벨 )
create table table7
( no number(2) constraint table7_no_nn NOT NULL,
  email varchar2(20));

--  not null ( 테이블 레벨 ) 지원 안됨

-- 마. forgign key ( 컬럼 레벨 )
-- master 테이블 작성
create table master1
( num  number(2) constraint master1_num_pk PRIMARY KEY,
  email varchar2(10));
  
insert into master1 ( num, email ) values ( 1, 'aa1');
insert into master1 ( num, email ) values ( 2, 'aa2');
insert into master1 ( num, email ) values ( 3, 'aa3');
commit;

-- slave 테이블 작성
select * from slave1;
create table slave1
( no NUMBER(2) constraint slave1_no_pk  PRIMARY KEY,
  name varchar2(10),
  num number(2) constraint slave1_num_fk  REFERENCES master1(num)
);
insert into slave1 ( no, name, num ) values (10, 'xxx1', 1 );
insert into slave1 ( no, name, num ) values (20, 'xxx2', 2 );
insert into slave1 ( no, name, num ) values (30, 'xxx3', 3 );
--insert into slave1 ( no, name, num ) values (40, 'xxx4', 4 ); -- 에러 발생
insert into slave1 ( no, name, num ) values (50, 'xxx5', null );
commit;
--  forgign key ( 테이블 레벨 )
-- slave12 테이블 작성

create table slave2
( no NUMBER(2) constraint slave2_no_pk  PRIMARY KEY,
  name varchar2(10),
  num number(2),
  constraint slave2_num_fk FOREIGN KEY(num) REFERENCES master1(num)
);
insert into slave2 ( no, name, num ) values (10, 'xxx1', 1 );
insert into slave2 ( no, name, num ) values (20, 'xxx2', 2 );
insert into slave2 ( no, name, num ) values (30, 'xxx3', 3 );
--insert into slave2 ( no, name, num ) values (40, 'xxx4', 4 ); -- 에러 발생
insert into slave2 ( no, name, num ) values (50, 'xxx5', null );
commit;
