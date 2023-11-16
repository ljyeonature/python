"""
        숫자형 종류
            - 정수형
            - 실수형
            - 복소수형 1 + 2j, 3i  ( 많이 사용안함 )
            - 8진수   0o25 = 2 * 8*(1) + 5 * 8(0) = 16 + 5 = 21
            - 16진수  0x25 = 2 * 16(1) + 5 * 16(0) = 32 + 5 = 37
"""

# 파이션의 모든 자료형은 객체로 취급한다
# 실행 : alt + shift + F10

""" [ 기초 연산자 ]
        + : 더하기
        - : 빼기
        * : 곱하기
        / : 나누기(실수값 결과)
        // : 나누기(정수값 결과)
        % : 나머지
        ** : 자승 (n제곱)
    
    2. 관계연산자
        <   >   <=  >=  ==  !=
    
    3. 논리연산자
        not     or      and
        
    4. 이진(비트) 연산자
        ~   :  이진 not   
        |   :  이진 or
        &   :  이진 and
        ^   :  이진 xor
        <<  :  shift
        >>  :  shift
        
    5. 대입연산자
        =
        +=  -=  *=  /=  //= %=
        &=  |=  ^=
        >>= <<=
    
    6. 기타연산자 : 딕셔너리, 문자열, 리스트, 튜플 등의 자료형에서 사용
        is      : 비교하는 객체의 주소가 같으면 True, 다르면 False
        is not  : 비교하는 객체의 주소가 다르면 True, 같으면 False 
        in      : 요소에 포함되면 True, 없으면 False
        not in  : 요소에 포함되지 않으면 False, 없으면 True
      

    [참고] 증가(++), 감소(--) 연산자 없음         
"""

a = 5
b = 2

""" [ 출력결과 ] 
        a + b = 7
        a - b = 3
        a * b = 10
        a / b = 2.5
        a // b = 2
        a % b = 1
        a ** b = 25
"""

print('a + b = ', a+b)
print('a - b = ', a-b)
print('a * b = ', a*b)
print('a / b = ', a/b)
print('a // b = ', a//b)
print('a % b = ', a%b)
print('a ** b = ', a**b)

print(' a / b = ', a/b)
print(' a / b = ', str(a/b))

# 복소수형 - 많이 사용 안 함
# print(2j + 5j)

print('H' in 'Hello')
print('h' in 'Hello')
print('h' not in 'Hello')

print('Hello' is 'Hello')
print('Hello' is 'hello')


