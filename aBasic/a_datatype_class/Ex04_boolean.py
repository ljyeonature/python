# 부울형 - 첫글자는 반드시 대문자 True, False, None 여야 한다
t = True
f = False
n = None    # 다른 언어의  null 값과 유사

# 파이썬은 pep8 규칙을 따르기

hungry = True
sleepy = False
print(type(hungry))
print(not hungry) # False
print(hungry and sleepy) #False
print(hungry or sleepy)  #True
print(hungry & sleepy)   #False
print(hungry | sleepy)   #True
print(hungry ^ sleepy)   #True




"""
        자료형         값           부울형
    -----------------------------------------------------
        문자형       "문자"          True
                    ""                     False
        리스트       [1,2,3]         True       
                    []                     False
        튜플         ()                     False
        딕셔너리     {}                     False
        숫자형       0이아닌 숫자     True
                    0                      False
                    None                   False

"""
if '아':
    print('True')
else:
    print('False')

if []:
    print('True2')
else:
    print('False2')

if 0:
    print('True3')
else:
    print('False3')

if -1:
    print('True4')
else:
    print('False4')

# 0번째여서 Fasle5가 나온다...
msg = '행복합시다'
if msg.find('행') >= 0:
    print('True5')
else:
    print('False5')
# -1이 나옴 : 값이 없어서... 그래서 0이 아니여서 True6이 나온다.
if msg.find('가') >= 0:
    print('True6')
else:
    print('False6')




