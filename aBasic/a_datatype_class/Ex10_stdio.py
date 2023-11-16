"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨
    - int() / float() / str() 자료형변환  ( eval() 사용보다는 형변환을 권장 )
"""
# name = input("이름을 입력하세요")
# print("당신은 ", name, '입니다')
# print('당신은 %s입니다' %name)
# print('당신은 {0}입니다'.format(name))


#-------------------------------------------
# 나이를 입력받아 +1을 하여 출력하고 키를 실수형으로 입력받아 출력
# age = int(input("나이를 입력하세요"))
# print(age+1)
# print('당신은 {}입니다'.format(age+1))
# height = eval(input("키를 입력하세요"))
# print(type(height))

print('1+2')
# eval : 자료형 변환 자동으로 잡아주는 함수
print(eval('1+2'))

#----------------------------------
# 단을 입력받아 구구단을 구하기
dan = int(input('단을 입력하세요 => '))
for i in range(1,10):
    print('{0}x{1}={2}'.format(dan,i,dan*i))
    print('end')

'''[자바스타일]
    for(int i:[1,2,3,....9]) {
        print()
    }
'''
#-----------------------------------------
# print() 함수



# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
# [ 콘솔에서 실행 ] python Ex10_stdio.py ourserver scott tiger
#                                   0      1      2      3
