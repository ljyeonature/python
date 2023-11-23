'''
Ex03_oracle_test.py

'''

import cx_Oracle
conn = cx_Oracle.connect('scott/tiger@127.0.0.1:1521/xe')
print('디비연결성공-oracle', conn.version)

cursor = conn.cursor()
sql = 'select * from imsi'
cursor.execute(sql)
# datas = cursor.fetchall()

for row in cursor:
    print(row)

conn.close()






