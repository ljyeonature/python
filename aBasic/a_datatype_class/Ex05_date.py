#
# import datetime
# today = datetime.date.today();
# print('today is ', today)

from datetime import date, timedelta
today = date.today()
print('today is ', today)

print(today.year, '년')
print(today.month, '월')
print(today.day, '일')
# 0부터 월요일
print(today.weekday(), '요일')

# 날짜 계산
print('어제 : ', today + timedelta(days=-1))
print('일주일전:',today + timedelta(days=-7))
print('일주일전:',today + timedelta(weeks=-1))
print('일주일후',today + timedelta(days=7))
print('일주일후',today + timedelta(weeks=1))

print('10일후',today + timedelta(days=10))

# [참고] 달(month) 계산 -> 외부라이브러리 설치
#from dateutil.relativedelta import relativedelta
# delta = relativedelta(end, start)  # 두 날짜의 차이 구하기
# result = 12 * delta.years + delta.months  # 두 날짜의 차이나는 개월수
#
# for i in range(result):
# count = start + relativedelta(months=i)      # 달수 증가
#
# print(count.strftime('%Y%m')



from datetime import datetime
# import datetime
today = datetime.today()
print(today)

# 날짜를 문자열 형식( sfrftime() )
print(today.strftime('%Y 년 %m월 %d일 %H시'))

# 문자열을 날짜 형식 형식(strptime())
naljja = '2020-08-20 12:25:44'
print(type(naljja))
mydate = datetime.strptime(naljja, '%Y-%m-%d %H:%M:%S')
print(type(mydate))