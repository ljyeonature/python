import MySQLdb

conn = MySQLdb.connect(
    host='localhost', port=3306, database='basic',
    user='scott', password='tiger', charset='utf8'
)
cursor = conn.cursor()

import folium
sql = 'SELECT * FROM gongcha'
cursor.execute(sql)
rows = cursor.fetchall()
map_osm = folium.Map([rows[0][5], rows[0][4]], zoom_start=7)

for i in range(len(rows)):
    if rows[i][5] is None or rows[i][4] is None:
        pass
    else:
        if "제주" in rows[i][2]:
            color = 'orange'
        elif ("경기" in rows[i][2] or "인천" in rows[i][2] or "호법" in rows[i][2] or "중앙1길" in rows[i][2] 
              or "만안" in rows[i][2] or "비전" in rows[i][2] or "처인구" in rows[i][2] or "일산" in rows[i][2]
              or "사우" in rows[i][2] or "안성" in rows[i][2] or "열우" in rows[i][2]):
            color = 'green'
        elif ("부산" in rows[i][2] or "대구" in rows[i][2] or "울산" in rows[i][2]or "경상" in rows[i][2]
              or "경남" in rows[i][2] or "경북" in rows[i][2] or "만촌" in rows[i][2] or "학정" in rows[i][2]
                or "성산구" in rows[i][2] or "김해" in rows[i][2] or "동진" in rows[i][2] or "조영동" in rows[i][2]
                or "호명면" in rows[i][2]):
            color = 'blue'
        elif ("세종특별자치시" in rows[i][2] or "세종시" in rows[i][2] or "충청" in rows[i][2] or "엄사" in rows[i][2]
              or "성성" in rows[i][2] or "청주" in rows[i][2] or "노은" in rows[i][2] or "대전" in rows[i][2]
              or "충남" in rows[i][2] or "천안" in rows[i][2] or "충북" in rows[i][2]):
            color = 'beige'
        elif "강원" in rows[i][2] or "설악면" in rows[i][2]:
            color = 'purple'
        elif ("광주" in rows[i][2] or "전라" in rows[i][2] or "전남" in rows[i][2] or "익산" in rows[i][2]
              or "첨단" in rows[i][2]or "전주" in rows[i][2] or "기지" in rows[i][2]):
            color = 'pink'
        elif "서울특별시" in rows[i][2] or "서울" in rows[i][2] or "서울시" in rows[i][2]:
            color = 'red'
        else:
            color = 'red'

        iframe = "주소: " + rows[i][2]+"<br/>"+"전화: "+rows[i][3]
        popup = folium.Popup(iframe, min_width=200, max_width=500)
        folium.Marker(location=[rows[i][5], rows[i][4]],
                      popup=popup,
                      icon=folium.Icon(color=color, icon='info-sign')).add_to(map_osm)
map_osm.save('./map/gongcha.html')















