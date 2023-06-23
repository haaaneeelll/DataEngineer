--  mariadb 조인(join)
-- 1. inner join
-- 1) natural join
select empno, ename, dname, loc, deptno
from emp natural join dept;

select e.empno, e.ename, d.dname, d.loc, deptno
from emp e natural join dept d;

-- 2) using 절
select empno, ename, dname, loc, deptno
from emp join dept using(deptno);

-- 3) on 절 
select empno, ename, dname, loc, emp.deptno
from emp join dept on emp.deptno = dept.deptno;

select empno, ename, dname, loc, sal, emp.deptno
from emp join dept on emp.deptno = dept.deptno
where sal > 3000;

select empno, ename, sal, losal, hisal, grade
from emp e join salgrade s on sal BETWEEN s.losal and s.hisal;

-- 4) 3개의 테이블 조인
select empno, ename, sal, dname, loc,  losal, hisal, grade
from emp e join salgrade s on sal BETWEEN s.losal and s.hisal
           join dept d using(deptno);
           
-- 5) self 조인
select e.ename as 사원, m.ename as 관리자
from emp e join emp m on e.mgr = m.empno;

-- 2. outer join
insert into emp ( empno, ename, sal, deptno )
values ( 9999, '홍길동', 500, null );
commit;
-- right outer join
select empno, ename, dname, loc, deptno
from emp right outer join dept using(deptno);

-- left outer join
select empno, ename, dname, loc, deptno
from emp left outer join dept using(deptno);


-- full outer join ( 지원 안됨 )


-- cross join
select empno, ename, dname, loc, emp.deptno
from emp cross join dept;