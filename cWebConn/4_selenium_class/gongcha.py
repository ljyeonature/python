
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import Select

# 웹 드라이버
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(2)

addrs = []
tels = []
names = []
snames = []

for city in range(1,18):
    names = []
    driver.get('https://www.gong-cha.co.kr/brand/store/search.php')
    driver.implicitly_wait(2)

    dropdown = Select(driver.find_element_by_id('etc9'))
    if len(str(city)) == 1:
        city='0'+str(city)
        dropdown.select_by_value(city)
        time.sleep(3)
    else:
        dropdown.select_by_value(str(city))
        time.sleep(3)
    html = driver.page_source
    time.sleep(3)
    soup = BeautifulSoup(html, 'html.parser')

    store_name = soup.select('#mCSB_1_container > ul > li > a > span.store')
    for name in store_name:
        names.append(name.text)

    for i in range(len(names)):
        search_txt = driver.find_element_by_id("subject")
        # 검색어 초기화
        search_txt.clear()
        search_txt.send_keys(names[i])
        driver.find_element_by_xpath('//*[@id="frmSearch"]/div/div/input[2]').click()
        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li').click()
        time.sleep(2)
        # 한 번 더 페이지 불러오기
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        name = soup.select_one('div.hgroup > p')
        addr = soup.select_one('.contents table tbody  tr:first-child > td')
        tel = soup.select_one('.contents  tbody  tr:nth-child(2) > td')
        snames.append(name.text)
        addrs.append(addr.text)
        tels.append(tel.text)

# 각 정보 csv 파일에 저장
import csv
output_file = 'files/store_info.csv'
file = csv.writer(open(output_file, 'w', encoding='utf-8', newline=''),delimiter=',')
for row in zip(snames,addrs,tels):
    file.writerow(row)

# DB에 연결
import MySQLdb

conn = MySQLdb.connect(
    host='localhost', port=3306, database='basic',
    user='scott', password='tiger', charset='utf8'
)

cursor = conn.cursor()
conn.close()


