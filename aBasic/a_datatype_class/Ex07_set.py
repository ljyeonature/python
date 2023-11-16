# -----------------------------------------------
#  집합
#       - 집합에 관련된 자료형
#       - 순서를 지정하지 않는다
#       - 중복을 허용하지 않는다
#       - { }

s = set()
print(type(s))
# 빈 집합을 생성
s = set([1,2,3,1,1])
print(s)
print(type(s))

s = { 1,2,3,2,1 }
print(s)
print(type(s))

# [주의]
# print(s[0]) --> 에러발생

s = {}      # 빈 set이 아님
print(type(s))

a = {3,4,5,6,7,7,7}
b = {1,2,3}

print(a.union(b))
print(a.intersection(b))

print(a & b)
print(a | b)


