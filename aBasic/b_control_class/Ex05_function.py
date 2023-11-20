"""
    [ 함수 ]

     - 반복적인 구문을 만들어 함수로 선언하여 간단하게 호출만 하고자 한다
     - 역할별 구문을 작성한다

     def 함수명(매개변수):
        수행할 문장들
"""

#(0) 인자도 없고 리턴값도 없는 함수
def func():
    print('inside function')

func()
func()
result = func()
print(result)

# (1) 리턴값이 여러개인 함수
def func(arg):
    return arg+5, arg+6

# 내부적으로 한 덩어리(튜플로 결과를 받음)
result = func(10)
print(result)
print(result[0] + result[1])

# 요소분해
a, b = func(8)
print(a)
print(b)

# (2) 위치인자( positional arguments )
def func(greeting, name):
    print(greeting, '!!!!', name, '님')

func('하이', '존스')
func('홍길동', '안녕')

# (3) 키워드 인자( keyword arguments )
func(name='홍길동', greeting='안녕')

# (4) 매개변수의 갯수 설정과 기본값 지정
def func(greeting, name="홍길동"):
    print(greeting, '!!!!', name, '님')

func("헬로우")
func("헬로우", "홍길순")






'''
#----------------------------------------------------------------
# (5) 위치 인자 모으기 (*)

첫번째와 두번째는 인자가 반드시 들어가고 
세번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다
그러나 네번째 인자부터는 정확히 모른다면?


'''
def func(a, b, c=0, *args):
    sum = a + b + c
    for i in args:
        sum += i
    return sum
print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))       # args에 7,8,9가 튜플로 들어간다

# (6) 키워드인자 모으기(**kwargs) => 이미 정해져있음

def func(a, b, c=0, *args, **kwargs):
    sum = a + b + c
    for i in args:
        sum += i
    print("kwargs: ", kwargs)
    # for v in kwargs:
    #     sum += kwargs[v]
    return sum

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))
print(func(4, 5, 6, kor=50, eng=70)) # 딕셔너리 형태로 나온다.(덩어리)
print(func(4, 5, 6, kor=50, eng=70, math=90))
