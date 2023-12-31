import requests
import ssl
import csv
import pandas as pd
import urllib.request
# url = "http://apis.data.go.kr/B551011/KorService1/areaBasedList1?serviceKey=aRoMlzYVu3EFwc8zi7gclb8VDPOjNqr0m6BfcLcXL3gebBiPZ4mXPM4XhtOboghDiVIOTzO4UDuJB4Lmy3jk5g==&MobileApp=AppTest&_type=json&MobileOS=ETC&numOfRows=12813&arrange=A&contentTypeId=12"
# context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
# response = urllib.request.urlopen(url, context=context)
# content = response.read()
# print(content)

# ==============================================================================================
# ssl._create_default_https_context = ssl._create_unverified_context
# url = "http://apis.data.go.kr/B551011/KorService1/detailCommon1"
# params = {
#     "serviceKey": "lbOvUjFPDGFHQpbUWMJeTwzByNcyZTOfZFRdVNhCSX1KHq6h9tZDG82RqEGCPj5lD1VNB/Kbe5dLoPClziQtXA==",
#     "MobileApp": "AppTest",
#     "_type": "json",
#     "MobileOS": "ETC",
#     "arrange": "A",
#     "contentTypeId": 39,
#     "overviewYN" : "Y"
# }
addrs = []
restaurant = []
contentId = []
image1 = []
image2 = []
mapx = []
mapy = []
homepage = []
tel = []
telname = []
overviews =[]

csv_file_path = 'files/restaurants_data.csv'  # 실제 파일 경로로 변경해주세요.
data = pd.read_csv(csv_file_path)
# print(data)
for index, row in data.iterrows():
    # 검색할 주소
    contentId.append(row.iloc[6])

print(contentId)

for i in range(100):
    url = "http://apis.data.go.kr/B551011/KorService1/detailCommon1?ServiceKey=lbOvUjFPDGFHQpbUWMJeTwzByNcyZTOfZFRdVNhCSX1KHq6h9tZDG82RqEGCPj5lD1VNB/Kbe5dLoPClziQtXA==&contentTypeId=39&contentId="+str(contentId[i])+"&MobileOS=ETC&MobileApp=AppTest&defaultYN=Y&firstImageYN=Y&areacodeYN=Y&catcodeYN=Y&addrinfoYN=Y&mapinfoYN=Y&overviewYN=Y&_type=json"
    print(url)
    # params["contentId"] = contentId[i]
    # response = requests.get(url, params=params)
    response = requests.get(url)
    print(response)
    data = response.json()
    print(data)
    datas = data["response"]["body"]["items"]["item"]
    addrs.append(datas[0]["addr1"])
    restaurant.append(datas[0]["title"])
    contentId.append(datas[0]["contentid"])
    image1.append(datas[0]["firstimage"])
    image2.append(datas[0]["firstimage2"])
    mapx.append(datas[0]["mapx"])
    mapy.append(datas[0]["mapy"])
    homepage.append(datas[0]["homepage"])
    tel.append(datas[0]["tel"])
    telname.append(datas[0]["telname"])
    overviews.append(datas[0]["overview"])


# CSV 파일로 저장

csv_filename = "files/restaurantdetail_data.csv"

with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
    # CSV 파일을 작성하기 위한 writer 객체 생성
    csv_writer = csv.writer(csvfile)

    # 헤더 쓰기 (예시: 데이터의 필드명)
    header = ["addr", "restaurantlist_name", "image1", "image2", "mapx", "mapy", "contentId", "homepage", "tel", "telname", "overviews"]
    csv_writer.writerow(header)

    # 데이터 쓰기
    for row in zip(addrs,restaurant,image1,image2,mapx,mapy,contentId,homepage,tel,telname,overviews):
        csv_writer.writerow(row)

print(f"Data has been saved to {csv_filename}")