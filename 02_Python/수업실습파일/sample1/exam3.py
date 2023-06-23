# exam3.py
# 역할: modul1.py 접근하여 연동하는 파일

# 경로지정 방법
# 1)  import 패키지명.모듈명
# 2)  import 패키지명.모듈명 as 별칭
# 3)  from  패키지명 import 모듈명 as 별칭, 모듈명2,...

from sample1 import module1, module2



#  관례적으로 항상 시작해야되는 모듈에 지정한다.
if __name__ == '__main__':
    print(module1.num)
    module1.fun()
    c = module1.Person()

    print(module2.num2)
    module2.fun2()
    c2 = module2.Person2()