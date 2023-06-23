#########################################################################
### 집합형 데이터 ###########################################################
#########################################################################

# 1 . 셋 ( set ) ==> immutable 값만 저장 가능하다. 대표적으로 list는 저장 불가 (매우 중요 )

# 1.셋 생성
m = {1,2,3,1} # {1, 2, 3}
m2 = set() # set()
print(m, m2)
print(set("hello")) # {'e', 'o', 'l', 'h'}

# 여러 요소값 저장 가능하지만 mutable 값 저장 불가
m3 = {10,20,"홍길동",(100,200)}
print(m3) # {10, 20, '홍길동', (100, 200)}
#m4 = {10,20,"홍길동",[1,2]}  # mutable 데이터인 리스트 저장 불가
# print(m4)  # 에러
#print(m*2) # error , 반복출력 불가

# 2. set 함수
print(dir(set))
'''
'add', 'clear', 'copy', 'difference', 'difference_update', 
'discard', 'intersection', 'intersection_update', 'isdisjoint', 
'issubset', 'issuperset', 'pop', 
'remove', 'symmetric_difference', 'symmetric_difference_update', 
'union', 'update'
'''

# 가. 값 추가 ==> 반드시 immutable 만 가능
m = {1,2,3}
m.add(10)
m.add("홍길동")
m.add((9,8))
print("add:",m) # {1, 2, 3, 10, (9, 8), '홍길동'}


# 나. union 연산되는 update ==> 병합(집합형에 저장된 데이터를 꺼내서 처리)
m2 = {1,2}
m2.update({3,4})
print("update1_set:" , m2) # {1, 2, 3, 4}
m2.update([5,6,7])
print("update2_list:" , m2) # {1, 2, 3, 4, 5, 6, 7}
m2.update((9,10))
print("update3_tuple:" , m2) # {1, 2, 3, 4, 5, 6, 7, 9, 10}

# 다. 삭제 ==> discard 와 remove
m2 = {1,2,3,4}
# m2.discard(4)  #  If the element is not a member, do nothing.
print(m2)
# m2.remove(3)  #  If the element is not a member, raise a KeyError.
print(m2)
m2.pop()      # 임의의 값을 삭제,  Raises KeyError if the set is empty.
print(">>>>>>>>>>>>>>>>>", m2)
# help(m2.discard)
# help(m2.remove)
# help(m2.pop)

# 라. set 함수
print("set 길이:" , len({1,2,3,4,5}))
x3 = {100,200,300}
print("포함 여부1:" , 9 in {9,8,7})
print("포함 여부2:" , 6 in {9,8,7})
print()
x3.clear()
print(x3)
print()

# 6) set 연산자 및 함수
a = {1,2,3,1}
b = {3,4}
print("union(합집합):" , a.union(b)) # {1, 2, 3, 4}
print("intersection(교집합):" , a.intersection(b)) # {3}
print("difference: 차집합" , a.difference(b)) # {1, 2}
print("exclusive difference: 대칭 차집합" ,
      a.symmetric_difference(b)) # {1, 2, 4}