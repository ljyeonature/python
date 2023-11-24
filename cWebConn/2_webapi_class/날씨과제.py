url = 'https://weather.naver.com/today/09440111'
from bs4 import BeautifulSoup
from urllib import request as req
site = req.urlopen(url)
page = site.read()
soup = BeautifulSoup(page, 'html.parser')
temp = soup.select('.current ')
print("신촌 : ",temp[0].text)
# print("신촌 : ",temp[0].text)
