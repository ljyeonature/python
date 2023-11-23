'''
Ex01_mysql_test.py
mysqlclient 2.2.0  버전 설치
'''

import MySQLdb

conn = MySQLdb.connect(
    host='127.0.0.1', port=3306, database='pythondb', user='lee', password='1234'
)

cursor = conn.cursor()
print('디비연결 성공2')

sql = 'SELECT * FROM emp'
cursor.execute(sql)
rows = cursor.fetchall()
# for row in rows:
#     print(row)

import csv
output_file = 'files/emp_output.csv'
file = csv.writer(open(output_file, 'w', newline=''),delimiter='!')

for row in rows:
    file.writerow(row)






