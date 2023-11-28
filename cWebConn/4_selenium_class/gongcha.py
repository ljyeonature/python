
from selenium import webdriver
from bs4 import BeautifulSoup
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
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
    # print(lic)


    # 스크롤 수동으로 내리기
    def hand_scroll(amount):
        try:
            scroll = driver.find_element_by_css_selector('.mCSB_dragger_bar')
            # ActionChains생성
            action = ActionChains(driver)
            # 클릭하고 잡기
            action.click_and_hold(scroll).perform()
            # 마우스 내리기
            action.move_by_offset(0, amount).perform()
            # 마우스 놓아주기
            action.release(scroll).perform()
        except:  # 끝 도달시
            return False

    for i in range(1,lic+1):
        if i%4 == 0:
            driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[' + str(i) + ']').click()
            # actions = ActionChains(driver).move_to_element(ele).perform()
            # xy = ele.location_once_scrolled_into_view
            # print(type(xy), xy)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            name = soup.select('.hgroup > .store')
            addr = soup.select('.contents table tbody  tr:first-child td')
            tel = soup.select('.contents  tbody  tr:nth-child(2) > td')
            print(name)
            # print(addr)
            # print(tel)
            addrs.append(addr)
            names.append(name)
            tels.append(tel)
            # xy = ele.
            # ele = driver.find_element_by_css_selector('#store_list')
            # ele.send_keys(Keys.PAGE_DOWN)
            hand_scroll(6)
            time.sleep(1)
            print(1)
        else:
            driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[' + str(i) + ']').click()
            time.sleep(1)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            name = soup.select('.hgroup > .store')
            addr = soup.select('.contents table tbody  tr:first-child td')
            tel = soup.select('.contents  tbody  tr:nth-child(2) > td')
            print(name)
            addrs.append(addr)
            names.append(name)
            tels.append(tel)

print(addrs)
print(names)
print(tels)
