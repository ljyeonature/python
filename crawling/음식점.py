import requests
import ssl
import csv
import urllib.request
# url = "http://apis.data.go.kr/B551011/KorService1/areaBasedList1?serviceKey=aRoMlzYVu3EFwc8zi7gclb8VDPOjNqr0m6BfcLcXL3gebBiPZ4mXPM4XhtOboghDiVIOTzO4UDuJB4Lmy3jk5g==&MobileApp=AppTest&_type=json&MobileOS=ETC&numOfRows=12813&arrange=A&contentTypeId=12"
# context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
# response = urllib.request.urlopen(url, context=context)
# content = response.read()
# print(content)

# ==============================================================================================
# ssl._create_default_https_context = ssl._create_unverified_context
url = "http://apis.data.go.kr/B551011/KorService1/areaBasedList1"
params = {
    "serviceKey": "aRoMlzYVu3EFwc8zi7gclb8VDPOjNqr0m6BfcLcXL3gebBiPZ4mXPM4XhtOboghDiVIOTzO4UDuJB4Lmy3jk5g==",
    "MobileApp": "AppTest",
    "_type": "json",
    "MobileOS": "ETC",
    "numOfRows": 16890,
    "arrange": "A",
    "contentTypeId": 39
}

response = requests.get(url, params=params)
# response = requests.get(url)
data = response.json()
datas = data["response"]["body"]["items"]["item"]
addrs = []
restaurant = []
print(datas)

for i in range(params["numOfRows"]):
    addrs.append(datas[i]["addr1"])
    restaurant.append(datas[i]["title"])

print(addrs)
print(restaurant)

# CSV 파일로 저장

csv_filename = "files/restaurants_data.csv"

with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
    # CSV 파일을 작성하기 위한 writer 객체 생성
    csv_writer = csv.writer(csvfile)

    # 헤더 쓰기 (예시: 데이터의 필드명)
    header = ["addr", "restaurantlist_name", "image1", "image2", "mapx", "mapy", "contentId", ]
    csv_writer.writerow(header)

    # 데이터 쓰기
    for item in datas:
        row = [item["addr1"], item["title"], item["firstimage"], item["firstimage2"], item["mapx"], item["mapy"], item["contentid"]]
        csv_writer.writerow(row)

print(f"Data has been saved to {csv_filename}")