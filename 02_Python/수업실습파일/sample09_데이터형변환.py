
'''
  일반형 데이터의 형변환
  int(값) : int로 변경
  float(값) : float로 변경
  bool(값) : bool로 변경


  집합형 데이터의 형변환
  str(값) : str로 변경
  list(값) : list로 변경
  tuple(값) : tuple로 변경
  set(값) : set로 변경
  dict(값) : dict로 변경

'''

### 일반 데이터 형변환 ###

# 1. int 로 변환
print( int(3.5) )    # 3
print( int(-3.5) )   # -3
print( int(True) )   # 1
print( int(False) )  # 0
print( int("123") )  # 123

# 2. float 로 변환
print( float(3) )                     # 3.0
print( float(-3) )                    # -3.0
print( float(True) )                  # 1.0
print( float(False) )                 # 0.0
print( float("123.34") )              # 123.34
print( float("123") )                 # 123.0

# 3. bool 로 변환
print( bool(0) )     # False
print( bool("") )    # False
print( bool(None) )  # False
print( bool([]) )    # False
print( bool({}) )    # False
print( bool() )      # False
print()
print( bool(10) )          # True
print( bool("123") )       # True
print( bool([10,20,30]) )  # True
print( bool({"age":20}) )  # True
print( bool(10,) )         # True

# 4. str 로 변환
print(str(123), type(str(123)))   # "123" <class 'str'>
print(str(3.14))  # "3.14"
print(str(True))  # "True"