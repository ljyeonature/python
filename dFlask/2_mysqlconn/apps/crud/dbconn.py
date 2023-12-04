''' apps/crud/dbconn.py '''


import pymysql


class Database():
    # 생성자
    def __init__(self):
        self.db = pymysql.connect(
            host ='localhost',
            user='scott',
            password='tiger',
            db='basic',
            charset='utf8'
        )

        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def commit(self):
        self.db.commit()

    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        rows = self.cursor.fetchall()
        return rows