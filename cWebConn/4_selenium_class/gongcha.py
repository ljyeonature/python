
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import Select

# 웹 드라이버
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3)

store_name = []
store_tel = []

addrs = []
tels = []
names = []

for city in range(1,3):
    driver.get('https://www.gong-cha.co.kr/brand/store/search.php')
    driver.implicitly_wait(2)

    # 서울특별시
    dropdown = Select(driver.find_element_by_id('etc9'))
    #dropdown = Select(driver.find_element_by_xpath('//*[@id="areadetailidx"]'))
    if len(str(city)) == 1:
        city='0'+str(city)
    dropdown.select_by_value(city)
    time.sleep(3)

    # 네트워크 시간 부여 - 기다려주기
    html = driver.page_source
    time.sleep(3)

    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    licounts = driver.find_element_by_id('mCSB_1_container')
    licount = licounts.find_element_by_tag_name('li')
    lic = len(soup.select('#mCSB_1_container > ul > li'))
    print(lic)
    print(licount.size['height']*lic)
    for i in range(1,lic+1):
        driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[' + str(i) + ']/a').click()
        time.sleep(3)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        name = soup.select('.hgroup > .store')
        addr = soup.select('.contents table tbody  tr:first-child td')
        tel = soup.select('.contents  tbody  tr:nth-child(2) > td')
        print(name)
        print(addr)
        print(tel)
        addrs.append(addr)
        names.append(name)
        tels.append(tel)

    # 리스트로...
    # print(names)

# for a, b in zip(store_name, store_tel):
#     print('지점명 : {0} / 전화번호 : {1}\n'.format(a,b))
print(addrs)
print(names)
print(tels)