-- 서브쿼리
-- 1. 단일행 서브쿼리
-- 1) where 절 서브쿼리
select empno, ename, job, sal
from emp
where sal > ( select sal
              from emp
              where ename ='WARD');
              
-- 2) 그룹함수 이용
select empno, ename, job, sal
from emp
where sal > ( select avg(sal)
              from emp );


-- 2. 복수행 서브쿼리
-- 업무별 최소급여를 받는 사원 조회
select empno, ename, job, sal
from emp
where sal IN ( select MIN(sal)
               from emp
               Group by job );
               
-- 업무가 MANAGER인 사원의 최소급여보다 적은 급여를 받는 사원 조회               
select empno, ename, job, sal
from emp
where sal < ALL ( select sal
                  from emp
                  where job = 'MANAGER');
                  
-- 업무가 MANAGER인 사원의 최대급여보다 많은 급여를 받는 사원 조회               
select empno, ename, job, sal
from emp
where sal > ALL ( select sal
                  from emp
                  where job = 'MANAGER');
                  
-- 업무가 MANAGER인 사원의 최대급여보다 적은 급여를 받는 사원 조회               
select empno, ename, job, sal
from emp
where sal < ANY ( select sal
                  from emp
                  where job = 'MANAGER'); 
                  
                  
-- 업무가 MANAGER인 사원의 최소급여보다 많은 급여를 받는 사원 조회               
select empno, ename, job, sal
from emp
where sal > ANY ( select sal
                  from emp
                  where job = 'MANAGER');
                  
-- exists
-- 서브쿼리 결과값이 존재하는 경우
select *
from emp
where EXISTS ( select empno
               from emp
               where comm is not null );
               
-- 서브쿼리 결과값이 존재하지 않는 경우
select *
from emp
where EXISTS ( select empno
               from emp
               where ename is null );                  