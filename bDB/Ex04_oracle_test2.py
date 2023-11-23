'''
Ex03_oracle_test.py

'''

import cx_Oracle

def createTable():
    conn = cx_Oracle.connect('scott/tiger@127.0.0.1:1521/xe')
    #print('디비연결성공-oracle', conn.version)
    cursor = conn.cursor()

    sql = '''
    CREATE TABLE supply
    (
        id               number  primary key,
        supplier_name    varchar2(30),
        invoice_number   varchar2(30),
        part_number      varchar2(30),
        cost             number,
        purchase_date    date
    )
    '''
    cursor.execute(sql)

    sql2 = 'CREATE SEQUENCE seq_supply_id'
    cursor.execute(sql2)

    conn.commit()
    conn.close()


def insertTable(data):
    conn = cx_Oracle.connect('scott/tiger@127.0.0.1:1521/xe')
    cursor = conn.cursor()
    sql = '''
        INSERT INTO supply
        VALUES(seq_supply_id.nextval, :0,:1,:2,:3,:4)
        '''
    cursor.execute(sql, data)
    conn.commit()
    conn.close()

if __name__ == '__main__':

    # (1) 테이블 생성
    createTable()

    # (2) 임시데이터 입력
    imsi = ['홍길동','9999', '8888',1000, '2050-09-12']
    insertTable(imsi)














