# DB에 csv 파일 저장
import csv
import MySQLdb

conn = MySQLdb.connect(
    host='localhost', port=3306, database='basic',
    user='scott', password='tiger', charset='utf8'
)

cursor = conn.cursor()
filename = 'files/store_info.csv'
file = csv.reader(open(filename, 'r', encoding="utf-8"), delimiter=',')

for row in file:
    sql = '''
          INSERT INTO gongcha(store_name, store_tel, store_addr) VALUES(%s,%s,%s)
      '''
    data = (row[0], row[1], row[2])
    cursor.execute(sql, data)

conn.commit()
conn.close()




