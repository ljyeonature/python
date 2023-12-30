import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(2)


search_text = [] # 주소
names = [] # 주소로 검색 안 될 경우
# tour_info에서 검색할 주소 가져오기
csv_file_path = './files/tour_info.csv'  # 실제 파일 경로로 변경해주세요.
data = pd.read_csv(csv_file_path, header=None)
# print(data)
for index, row in data.iterrows():
    # 검색할 주소
    names.append(row[0])
    search_text.append(row[1])
    # print(row[1])
print(names)
print(search_text)

#------------------------------------------------
# 카카오맵에서 방문자수(건수) / 평점 / 리뷰 수 가져오기
visitors = [] # 방문자 수
rates = [] # 평점 수
reviews = [] #리뷰 건수

driver.get('https://map.kakao.com/')
driver.implicitly_wait(2)

for n in range(len(search_text)):
    search = driver.find_element_by_id('search.keyword.query')
    search.clear()
    search.send_keys(search_text[n])
    driver.find_element_by_id('search.keyword.submit').send_keys(Keys.ENTER)
    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(3)

    rate = soup.select_one('#info\.search\.place\.list > li:nth-child(1) > div.rating.clickArea > span.score > em')
    visitor = soup.select_one('#info\.search\.place\.list > li:nth-child(1) > div.rating.clickArea > span.score > a')
    review = soup.select_one('#info\.search\.place\.list > li:nth-child(1) > div.rating.clickArea > a > em')
    print(rate)

    if rate is None or visitor is None or review is None:
        search_name = driver.find_element_by_id('search.keyword.query')
        search_name.clear()
        search_name.send_keys(names[n])
        driver.find_element_by_id('search.keyword.submit').send_keys(Keys.ENTER)
        time.sleep(3)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        time.sleep(3)

        rate = soup.select_one('#info\.search\.place\.list > li:nth-child(1) > div.rating.clickArea > span.score > em')
        visitor = soup.select_one('#info\.search\.place\.list > li:nth-child(1) > div.rating.clickArea > span.score > a')
        review = soup.select_one('#info\.search\.place\.list > li:nth-child(1) > div.rating.clickArea > a > em')

        print(rate)
        if rate is None or visitor is None or review is None:
            rates.append(rate)
            rates.append(visitor)
            rates.append(review)
        else:
            rates.append(rate.text)
            visitors.append(visitor.text)
            reviews.append(review.text)

    else:
        rates.append(rate.text)
        visitors.append(visitor.text)
        reviews.append(review.text)



print(rates)

import csv
output_file = 'files/jeonbuk_rates.csv'
file = csv.writer(open(output_file, 'w', encoding='utf-8', newline=''),delimiter=',')
for row in zip(names, search_text, rates, visitors, reviews):
    file.writerow(row)