# (0) 문자열을 "" 이나 '' 으로 표현



# -----------------------------------------
# (1) 개행을 포함한 문자열
msg = """
    안녕하세요.
    저는 성이 파이이고,
    이름은 썬입니다.
    잘 부탁합니다.
"""
print(msg)

msg = '''
    행복합시다
    즐깁시다
    오늘도
'''
print(msg)

# -----------------------------------------
#  (2) 문자열 연산
#       문자열 합치기 : 문자열 + 문자열
#       문자열 반복 : 문자열 * 숫자

a = '독도는 '
b = "한국이다. "
""" [ 출력결과 ] 
        --------------------------------------------------
        독도는 한국이다. 
        oxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxox
        독도는 한국이다. 독도는 한국이다. 독도는 한국이다. 
        ==================================================
"""
print('-'*50)
print(a + b)
print('ox'*25)
print((a + b)*3)
print('='*50)






# -----------------------------------------
#  (3) 문자열의 인덱싱과 슬라이싱
#       - 인덱스는 0부터 시작한다
#       - s[i] : s 문자열에서 i번째 문자 추출
#       - s[i:j] : s 문자열에서 i번째에서 j-1까지의 문자 추출
#       - s[i:j:k] : s 문자열에서 i번째에서 j-1까지에서 k개씩 건너뛰어 문자 추출
#
#       - s[-i] : s 문자열에서 뒤에서부터 i번째 문자 추출
#                 ( 뒤에서 인덱스는 1부터 센다 )

msg ='오늘도 행복도 하다'

""" [ 출력결과 ]
        오
        오늘
        늘도 행복
        오도행
        다
"""
print(msg[0])
print(msg[0:2])
print(msg[1:6])
print(msg[0:5:2])
print(msg[-1])
print(msg[-0])
msg[0]
msg[-0]

""" [ 참고 ] 
       ` msg[0] == msg[-0] 같은 값을 추출
       ` msg[:] 전체 추출
       ` msg[i:-j] i번째부터 뒤에서 j-1 까지 추출
"""
print(msg[3:-2])





""" [ 확인 ]
    1- 문자열 끝까지라면 두번째 숫자 생략 가능
    2- 처음부터 시작하는 것이라면 첫번째 숫자 생략 가능
"""
# 1) 5번째부터
print(msg[5:])
# 2) 5번째 전의 문자까지
print(msg[:5])

# 3) 5번째 전의 문자까지에서 2개씩 건너뛰어
print(msg[:5:2])

# 4) 문자열 전체에서 2개씩 건너뛰어
print(msg[::2])

s = '1234'
ss = s[::-1]
print(ss)

s='1321'
ss = s[::-1]
print(ss)



""" [ 연습-1 ]
    날짜와 시간을 표현하는 문자열에서 '2020-02-22 : 12:05:12'
    '2020년 2월 22일' 출력
    '12시 5분' 출력
"""
timeDate = '2020-02-22 : 12:05:12'
print(timeDate[0:4]+"년 "+timeDate[6]+"월 "+timeDate[8:10]+"일")
print(timeDate[13:15]+"시 " + timeDate[17]+"분")



# -----------------------------------------
#  (4-1) 문자열 관련 함수
#       s.count('글') : s 문자열에서 '글'이라는 문자 개수 세기
#       s.index('글') : s 문자열에서 문자 '글' 위치 알려주기
#       s.find('글') : s 문자열에서 문자 '글' 위치 알려주기
#       s.rfind('글') : s 문자열에서 문자 '글' 오른쪽에서 왼쪽으로 찾아서 위치 알려주기
#       len(s) : s 문자열 길이

msg ='오늘도 행복도 하다'

""" [ 출력결과 ]
    1) '행복'이라는 글자 위치 찾기
    2) '가자'라는 글자 위치 찾기
    3) '행복'이라는 글자를 오른쪽에서 왼쪽으로 찾기
    4) 문자열 전체 길이 구하기
    5) '도'라는 단어의 갯수 구하기
"""
print('문자열')
print(msg.index('행복'))
# print(msg.index('가자'))
print(msg.find('가자'))
print(msg.rfind('행복'))
print(len(msg))
print(msg.count('도'))
# print(msg.count())



# -----------------------------------------
#  (4-2) 문자열 관련 함수
#   s.upper() : 소문자를 대문자로
#   s.lower() : 대문자를 소문자로
#   s.lstrip() : 왼쪽 공백 지우기
#   s.rstrip() : 오른쪽 공백 지우기
#   s.strip() : 양쪽 공백 지우기

msg = '  This is My Life  '
print(msg.upper())
print(msg.lower())
print(msg.lstrip())
print(msg.rstrip())
print(msg.strip())

print(msg.replace(" ", ""))

# -----------------------------------------
#  (4-3) 문자열 관련 함수
#   s.replace("a","b")  :  s 문자열에서 단어 a를 단어 b로 바꾸기
#   s.split() : s 문자열을 공백으로 나누기
#   s.split('z') : s 문자열을 z 기호로 나누기
#   d.join(s) : d 단어를 s 문자열에 삽입

msg = "우리는 독도를 지킨다"
print(msg.replace('독도를','대한민국을'))
print(msg)
print(msg.split())
print(','.join(msg))
print(','.join(msg.split()))







