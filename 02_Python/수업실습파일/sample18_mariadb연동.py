
'''
   mariaDB 연동
   pip install mariadb

'''

import mariadb

# 1. MariaDB 연동
import mariadb

user = "root"
pw = "1234"

con = mariadb.connect(host="localhost",
                      user=user, password=pw,
                      port=3306, database="exam")
print("Database 연결 성공")

# 1. 특정 레코드 하나 얻기. deptno = 10
with con.cursor() as cur: # 자동으로 cursor close 됨
    sql = "select * from dept where deptno ={xxx}".format(xxx=10)
    cur.execute(sql)
    res = cur.fetchone()
    print(res)

# 2. 멀티 레코드 얻기
with con.cursor() as cur:
    cur.execute("select * from dept order by deptno")
    res = cur.fetchall()  # list로 반환
    for row in res:
        print(row)

# 3. 저장- 단일 저장
xxx=3
yyy='개발부'
zzz='서울'
# with con.cursor() as cur:
#     sql = f"insert into dept (deptno, dname, loc) values ({xxx}, '{yyy}', '{zzz}')"
#     print((sql))
#     cur.execute( sql)
#     print("저장된 레코드갯수:", cur.rowcount)
#     con.commit()
# 4. 저장 - 멀티 저장
# with con.cursor() as cur:
#     rows = [(11, "개발","서울"), (12, "개발","서울")]
#     cur.executemany("insert into dept (deptno, dname, loc) values  ( ?, ?, ? )", rows)
#     print("저장된 레코드갯수:", cur.rowcount)
#     con.commit()

# 5. 수정
with con.cursor() as cur:
    cur.execute("update dept set dname = '{}', loc= '{}' "
                " where deptno = {}".format("개발부", "서울시", 11))
    print("수정된 레코드갯수:", cur.rowcount)
    con.commit()

# 6. 삭제
with con.cursor() as cur:
    cur.execute("delete from dept where deptno = {}".format(12))
    print("삭제된 레코드갯수:", cur.rowcount)
    con.commit()

# 가장 마지막에 자원 반납
con.close()