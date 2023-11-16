"""
1. 사용자로부터 5개의 숫자를 읽어서 리스트에 저장하고 숫자들의 평균을 계산하여 출력한다.
또 숫자중에서 평균을 출력하여 보자.
"""
"""
total = 0
for i in range(5):
    n = int(input("정수를 입력하세요: "))
    total = total + n
print("평균=",(total/5))
"""

# 2. 사용자에게서 받은 문자들을 역순으로 출력한다.
"""
a = input("문자열입력: ")
print("결과: ",a[::-1])
"""
"""
3. 사용자에게서 받은 정수들의 평균과 표준편차를 계산하여 출력한다. 
평균과 표준편차를 프로그램을 작성하세요
"""
# import numpy
# total = 0
# n = list(map(int,input("정수리스트입력: ").split()))
# print(len(n))
# for i in n:
#     total = total + i
#
#
# mean = total / len(n)
# print("평균={}".format(mean))
#
# # vsum = 0
# # for val in num:
# #     vsum = vsum + (val - mean)**2
# # variance = vsum / len(vals)
# # print(variance)
# num_var = numpy.var(n)
# std = numpy.std(n)
# print("표준편차 %0.2f" %std)

"""
4. 전화 키패드에는 각 숫자키마다 3개의 문자가 적혀있다. 사용자가 입력한 문자열을 전화기의 숫자키로 변화하는 프로그램을 작성해보자.

"""
num = input("문자열을입력하시오: ")
numberArr = [[], ['A','B','C']]
"""
  2         3      4        5           6           7              8        9
A B C   D E F   G H I    J  K  L    M  N  O    P   Q  R  S    T  U  V    W  X  Y  Z
1 2 3 | 4 5 6 | 7 8 9 | 10 11 12 | 13 14 15 | 16  17 18  19 | 20 21 22 | 23 24 25 26
"""
number = [];
for i in num:
    if(i in ['A', 'B', 'C']):
        number.append(2)
    if (i in ['D', 'E', 'F']):
        number.append(3)
    if (i in ['G', 'H', 'I']):
        number.append(4)
    if (i in ['J', 'K', 'L']):
        number.append(5)
    if (i in ['M', 'N', 'O']):
        number.append(6)
    if (i in ['P', 'Q', 'R', 'S']):
        number.append(7)
    if (i in ['T', 'U', 'V']):
        number.append(8)
    if (i in ['W', 'X', 'Y', 'Z']):
        number.append(9)
for i in number:
    print(i,end="")






