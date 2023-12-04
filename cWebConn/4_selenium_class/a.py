import csv
names = ['1','2']
addrs = ['하','이']
tels = ['010','031']
output_file = 'files/a_info.csv'
file = csv.writer(open(output_file, 'w', newline=''),delimiter=',')
for row in zip(names,addrs,tels):
    file.writerow(row)


import MySQLdb

conn = MySQLdb.connect(
    host='172.20.10.2', port=3306, database='basic', user='scott', password='tiger'
)

cursor = conn.cursor()
print('디비연결 성공')