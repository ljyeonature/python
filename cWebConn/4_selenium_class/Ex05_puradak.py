
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import Select

# 웹 드라이버
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3)

store_name = []
store_tel = []

for num in range(1,6):
    driver.get('https://puradakchicken.com/startup/store.asp')
    driver.implicitly_wait(2)

    #dropdown = Select(driver.find_element_by_id('areadetailidx'))
    dropdown = Select(driver.find_element_by_xpath('//*[@id="areadetailidx"]'))
    dropdown.select_by_value(str(num))
    time.sleep(3)

    # 네트워크 시간 부여 - 기다려주기
    html = driver.page_source
    time.sleep(3)

    soup = BeautifulSoup(html, 'html.parser')
    driver.find_element_by_class_name('dView').click()
    jusos = soup.select('.juso .doro')
    print(jusos)
    #names = soup.select('#result_search p.name')
    #tels = soup.select('#result_search p.tel')


    # store_name = [n.text for n in jusos]
    # store_tel = [n.text for n in tels]


    # 리스트로...
    # print(names)

# for a, b in zip(store_name, store_tel):
#     print('지점명 : {0} / 전화번호 : {1}\n'.format(a,b))