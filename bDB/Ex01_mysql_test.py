'''
Ex01_mysql_test.py
mysqlclient 2.2.0  버전 설치
'''

import MySQLdb

conn = MySQLdb.connect(
    host='127.0.0.1', port=3306, database='pythondb', user='lee', password='1234'
)

cursor = conn.cursor()
print('디비연결 성공')

# 레코드 하나만 입력확인
# sql = '''
#     INSERT INTO emp(empno, ename, job, hiredate, sal, comm)
#     VALUES (9999, 'hong', 'it', sysdate(), 1000, 2000)
#
# '''
#
# cursor.execute(sql)
# conn.commit()
# conn.close()

# csv 파일을 디비에 저장
import csv
filename = 'files/emp.csv'
file = csv.reader(open(filename, 'r'), delimiter=',')

for row in file:
    # print(row)
    sql = '''
        INSERT INTO emp VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
    '''
    cursor.execute(sql, row)

conn.commit()
conn.close()



