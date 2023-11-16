msg = '행복해'            # 문자열
li = ['a','b','c']       # 리스트
tpl = ('ㄱ','ㄴ','ㄷ')    # 튜플
di = {'k': 5, 'j': 6, 'l':7 }    # 딕셔너리


# (1) unpacking : 요소분해
c1, c2, c3 = di
print(c1)
print(c2)
print(c3)

# (2)
alist = [(1,2),(3,4),(5,6)]
"""
1 + 2 = 3
3 + 4 = 7
5 + 6 = 11
"""
# 요소분해
for a,b in alist:
    print('{} + {} = {}'.format(a, b, a+b))

#--------------------------
# enumerate() : 각 요소와 인덱스 같이 추출
# [참고] 자바에서 Enumeration -> Iterator
user_list = ['개발자','코더','노가다','전문가']
for value in user_list:
    print(value)
for value in enumerate(user_list):
    print(value)

for idx, value in enumerate(user_list):
    print(idx, '>', value)

#---------------------------------
# zip()

days=['월', '화', '수']
doit = ['잠자기','공부','놀기','밥먹기']
month = [1,2,3]
print(zip(days,doit))
print(list(zip(days,doit)))
print(dict(zip(days,doit)))
print('@'*40)
a = list(zip(days, doit))
b = dict(zip(days, doit))
for data in b:
    print(data)