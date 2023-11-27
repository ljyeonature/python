'''
Ex05_seoul.py

https://www.seoul.go.kr/seoul/autonomy.do

'''
from bs4 import BeautifulSoup
# from urllib import request
import requests
#  (1) 웹페이지 접속
url = 'https://www.seoul.go.kr/seoul/autonomy.do'
site = requests.get(url)
html = site.content
# html = site.text
# print(html)

# (2) 분석 및 파서
soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
# print(soup)

# (3) 정보 추출
구청이름 = []
구청주소 = []
구청전화번호 = []
구청홈페이지 = []

for i in range(1, 26): # 1_25
    names = soup.select_one('#district%d > strong' % i)
    addrs = soup.select_one('#district%d > ul > li:first-child' % i)
    tels = soup.select_one('#district%d > ul > li:nth-child(2)' % i)
    homepages = soup.select_one('#district%d > ul > li:last-child > a' % i)
    # 구청이름.append(names[0])
    구청이름.append(names.text)
    구청주소.append(addrs.text)
    구청전화번호.append(tels.text)
    구청홈페이지.append(homepages.text)

# (4) 결과확인
# print(구청이름)
# print(구청주소)
# print(구청전화번호)
# print(구청홈페이지)

for a,b,c,d in zip(구청이름, 구청주소, 구청전화번호, 구청홈페이지):
    print('구청이름 : {0} \n구청주소 : {1} \n구청전화번호 : {2}\n구청홈페이지 : {3}\n'.format(a,b,c,d))