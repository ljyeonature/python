import MySQLdb
import json
import requests

conn = MySQLdb.connect(
    host='localhost', port=3306, database='basic',
    user='scott', password='tiger', charset='utf8'
)
cursor = conn.cursor()

sql = 'SELECT * FROM gongcha'
cursor.execute(sql)
rows = cursor.fetchall()
address = [addr for no,name,addr,tel,lati,longi in rows]
api_key = '26aed070885f816d90df060a204495b5'

for n, addr in enumerate(address):
    try :
        if '제주특별차지도' in addr:
            addr = addr.replace('제주특별차지도', '제주특별자치도')

        url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + addr
        headers = {"Authorization": "KakaoAK " + api_key}
        result = json.loads(str(requests.get(url, headers=headers).text))
        match_first = result['documents'][0]['address']
        # print(match_first)
        lati = float(match_first['x'])
        longi = float(match_first['y'])
        num = n

    except Exception:
        pass

    else:
        sql = '''
                  UPDATE gongcha SET store_lati = %s, store_longi = %s WHERE no = %s
              '''
        data = (lati, longi, num + 1)
        cursor.execute(sql, data)

conn.commit()
conn.close()



