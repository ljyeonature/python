"""

[ 연습문제 ]

- 리스트를 인자로 받아 짝수만 갖는 리스트 반환하는 함수 ( 함수명 : even_filter )
    [ 실행 ]
        print(even_filter([1, 2, 4, 5, 8, 9, 10]))

- 주어진 수가 소수인지 아닌지 판단하는 함수 ( 함수명 : is_prime_number )
    [ 실행 ]
        print(is_prime_number(60))
        print(is_prime_number(61))

- 주어진 문자열에서 모음의 개수를 출력하는 함수 ( 함수명 : count_vowel )
    [ 실행 ]
        print(count_vowel("pythonian"))




"""

# 1.
def even_filter(listArr):
    evenList = []
    for even in listArr:
        if even % 2 == 0:
            evenList.append(even)
    return evenList

print(even_filter([1, 2, 4, 5, 8, 9, 10]))

# 2.
# 소수 : 자기 자신과 1만 약수로 가짐.
def is_prime_number(num):
    cnt = 0
    for n in range(1,num+1):
        if num % n == 0:
            cnt += 1
    if cnt == 2:
        return True
    else:
        return False

print(is_prime_number(60))
print(is_prime_number(61))

# 3.
def count_vowel(strArr):
    cnt = 0
    for s in strArr:
        if s in ["a", "e", "i", "o", "u"]:
            cnt += 1
    return cnt


print(count_vowel("pythonian"))