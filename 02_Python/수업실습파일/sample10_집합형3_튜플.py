# 2. 튜플
# 1) 튜플 생성
xx = (10,20,30,43)
xx2 = tuple([9,8,7,7,6,8,9])
xx3 = (100,)  # 값 하나 가진 튜플 생성
print(xx, xx2) # (10, 20, 30, 43) (9, 8, 7, 7, 6, 8, 9)
print(tuple("hello")) # ('h', 'e', 'l', 'l', 'o')

# 2) 튜플 함수
print(dir(tuple))
'''
 'count', 'index'
'''
print("튜플 길이:" , len((1,2,3,4)))
print("포함 갯수:" , (10,2,3,2,9,2).count(2))
x3 = (100,200,300)
print("특정 위치:" , x3.index(200))
print("포함 여부1:" , 9 in (9,8,7))
print("포함 여부2:" , 6 in (9,8,7))
print()

# 3) 인덱싱 및 슬라이싱
kk = (1,2,3,4,5)
print("특정 값:" , kk[0])
print("slice:" , kk[0:3])
print("slice:" , kk[:6])
print("slice:" , kk[3:])
print("slice:" , kk[:])
print()
kk3 =(1,2,3,(9,8,7))
print("중첩 :" , kk3)
print("특정 값 출력1:" , kk3[3][0])
print("특정 값 출력2:" , kk3[3][2:])
print("특정 값 출력3:" , kk3[3][:2])