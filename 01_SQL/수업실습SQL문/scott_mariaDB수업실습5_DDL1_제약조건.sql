-- DDL

--1) 테이블 생성
create table IF NOT EXISTS dept_2
( deptno INT,
  dname varchar(10),
  loc varchar(10));

-- 2) default  
create table IF NOT EXISTS dept_3
( deptno int,
  dname varchar(10),
  loc varchar(10) default '서울');  

insert into dept_3(deptno,dname) 
values ( 1, '개발');
select * from dept_3;
  
-- 3) 제약조건

-- 제약조건 확인
SELECT * 
FROM information_schema.table_constraints
WHERE TABLE_NAME = 'DEPT';

-- 가. primary key ( 컬럼 레벨 )
create table IF NOT EXISTS table1
( no int  PRIMARY KEY AUTO_INCREMENT,
  email varchar(20));

--  primary key ( 테이블 레벨 )
create table IF NOT EXISTS table2
( no int,
  email varchar(20),
  constraint PRIMARY KEY(no)
  );
-- 복합컬럼
create table table2_1
( no int,
  email varchar(20),
  address varchar(20),
  constraint  PRIMARY KEY(no, email)
  );  
  
-- 나. unique ( 컬럼 레벨 )
create table IF NOT EXISTS table3
( no int  UNIQUE,
  email varchar(20));

--  unique ( 테이블 레벨 )
create table IF NOT EXISTS table4
( no int,
  email varchar(20),
  constraint  UNIQUE(no)
  );
  
-- 다. check ( 컬럼 레벨 )
create table IF NOT EXISTS table5
( no int  CHECK(no in (10,20)),
  email varchar(20));

--  check ( 테이블 레벨 )
create table IF NOT EXISTS table6
( no int,
  email varchar(20),
  constraint  CHECK(no in (10,20))
  );
  
-- 라. not null ( 컬럼 레벨 )
create table IF NOT EXISTS table7
( no int  NOT NULL,
  email varchar(20));

--  not null ( 테이블 레벨 ) 지원 안됨

-- 마. forgign key ( 컬럼 레벨 )
DROP TABLE slave1;
DROP TABLE SLAVE2;
DROP TABLE master1;

CREATE TABLE MASTER1
( NO INT PRIMARY KEY ,
  NAME VARCHAR(10) NOT NULL );

INSERT INTO MASTER1 ( NO, NAME ) VALUES ( 1, 'aa1');
INSERT INTO MASTER1 ( NO, NAME ) VALUES ( 2, 'aa2');
INSERT INTO MASTER1 ( NO, NAME ) VALUES ( 3, 'aa3');
  
CREATE TABLE SLAVE1
( num INT PRIMARY KEY,
  NO INT REFERENCES master1(NO));
  
INSERT INTO SLAVE1 ( num, NO ) VALUES ( 10, 1);
INSERT INTO SLAVE1 ( num, NO ) VALUES ( 11, 2);
INSERT INTO SLAVE1 ( num, NO ) VALUES ( 12, 3);
INSERT INTO SLAVE1 ( num, NO ) VALUES ( 13, 4); # 예외발생

-- forgign key ( 테이블  레벨 )
CREATE TABLE SLAVE2
( num INT PRIMARY KEY,
  NO INT,
  CONSTRAINT FOREIGN KEY(NO) REFERENCES master1(NO)  ON DELETE CASCADE); # 테이블 레벨만 지원

INSERT INTO SLAVE2 ( num, NO ) VALUES ( 10, 1);
INSERT INTO SLAVE2 ( num, NO ) VALUES ( 11, 2);
INSERT INTO SLAVE2 ( num, NO ) VALUES ( 12, 3);
