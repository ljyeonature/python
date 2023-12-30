import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(2)

addrs = []  # 주소
names = []  # 주소로 검색 안 될 경우
# tourist_destination_data에서 검색할 주소 가져오기
csv_file_path = 'files/tourlist_destination_data.csv'  # 실제 파일 경로로 변경해주세요.
data = pd.read_csv(csv_file_path)
# print(data)
for index, row in data.iterrows():
    # 검색할 주소
    addrs.append(row.iloc[0])
    names.append(row.iloc[1])
    # print(row[1])
# print(names)
# print(addrs)


# ------------------------------------------------
# 네이버지도에서 방문자수(건수) / 평점 / 리뷰 수 가져오기
visitors = []  # 방문자 수
rates = []  # 평점 수
reviews = []  # 리뷰 건수

# 검색어 창에 관광지 이름 넣고 검색
for n in range(len(names)):
    try:
        driver.get("https://map.naver.com/p/search/" + names[n])  # 네이버 신 지도

        driver.implicitly_wait(2)
        # 표시 기다리기
        time.sleep(5)
        # 만약 검색 후 바로 검색 결과나 나오지 않고, 목록이 나오는 경우
        # iframe 전환
        try:
            frame = driver.find_element(By.CSS_SELECTOR,"iframe#searchIframe")
            driver.switch_to.frame(frame)
            time.sleep(5)
            driver.find_element(By.CSS_SELECTOR,
                '#_pcmap_list_scroll_container > ul > li:nth-child(1) > div.qbGlu > div.ouxiq > a:nth-child(1)').click()
            time.sleep(5)
            driver.switch_to.default_content()
            entryFrame = driver.find_element(By.CSS_SELECTOR,"iframe#entryIframe")
            driver.switch_to.frame(entryFrame)
            time.sleep(5)
            # driver.switch_to.frame(frame(driver.find_element(By.CSS_SELECTOR,"iframe#entryIframe")));
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            time.sleep(5)
            rate = soup.select_one(
                "#app-root > div > div > div > div.place_section.no_margin.OP4V8 > div.zD5Nm.undefined > div.dAsGb > span.PXMot.LXIwF")
            visitor = soup.select_one(".PXMot > a:-soup-contains('방문자')")
            review = soup.select_one(".PXMot > a:-soup-contains('블로그')")

            rates.append(rate.text if rate else "")
            visitors.append(visitor.text if visitor else "")
            reviews.append(review.text if review else "")

            print('rate : {0} | visitor : {1} | review : {2}'.format(rates[n], visitors[n], reviews[n]))

        except Exception as e:
            print(f"클릭할 목록이 없다")
            driver.switch_to.default_content()
            entryFrame = driver.find_element(By.CSS_SELECTOR,"iframe#entryIframe")
            driver.switch_to.frame(entryFrame)
            time.sleep(5)
            # driver.switch_to.frame(frame(driver.find_element(By.CSS_SELECTOR,"iframe#entryIframe")));
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            time.sleep(5)
            rate = soup.select_one(
                "#app-root > div > div > div > div.place_section.no_margin.OP4V8 > div.zD5Nm.undefined > div.dAsGb > span.PXMot.LXIwF")
            visitor = soup.select_one(".PXMot > a:-soup-contains('방문자')")
            review = soup.select_one(".PXMot > a:-soup-contains('블로그')")

            rates.append(rate.text if rate else "")
            visitors.append(visitor.text if visitor else "")
            reviews.append(review.text if review else "")

            print('rate : {0} | visitor : {1} | review : {2}'.format(rates[n], visitors[n], reviews[n]))
    except Exception as e:
        print(f"아무것도 출력되지 않늗다.")
        # # 이름을 쳤는데 안 나오면 주소입력
        # # text = names[n].split()[0]
        # driver.get("https://map.naver.com/p/search/" + addrs[n])  # 네이버 신 지도
        # driver.implicitly_wait(2)
        # html = driver.page_source
        # soup = BeautifulSoup(html, 'html.parser')
        # time.sleep(5)
        # # 주소입력 후 한 번에 안 뜨는 경우 - 장소에서 찾아서 클릭
        # no_space_name = ''.join(names[n].split())
        # search_name = soup.select_one(
        #     "#app-layout > div.sc-wli0gr.grTceJ > div > div.sc-1wsjitl.dunggE.overlap > div > div > div > div > div > div.scroll_box > div.end_area > div:nth-child(3) > ul > li:nth-child(1) > button > strong").text
        # no_space_search_name = ''.join(search_name.split())
        # if no_space_search_name in no_space_name:
        #     driver.find_element(By.CSS_SELECTOR,
        #         "#app-layout > div.sc-wli0gr.grTceJ > div > div.sc-1wsjitl.dunggE.overlap > div > div > div > div > div > div.scroll_box > div.end_area > div:nth-child(3) > ul > li > button").click()
        #     time.sleep(5)
        #
        # entryFrame = driver.find_element(By.CSS_SELECTOR,"iframe#entryIframe")
        # driver.switch_to.frame(entryFrame)
        # time.sleep(5)
        # # driver.switch_to.frame(frame(driver.find_element(By.CSS_SELECTOR,"iframe#entryIframe")));
        # html = driver.page_source
        # soup = BeautifulSoup(html, 'html.parser')
        # time.sleep(5)
        # rate = soup.select_one(
        #     "#app-root > div > div > div > div.place_section.no_margin.OP4V8 > div.zD5Nm.undefined > div.dAsGb > span.PXMot.LXIwF")
        # visitor = soup.select_one(".PXMot > a:-soup-contains('방문자')")
        # review = soup.select_one(".PXMot > a:-soup-contains('블로그')")
        #
        rates.append("")
        visitors.append("")
        reviews.append("")
        #
        print('rate : {0} | visitor : {1} | review : {2}'.format(rates[n], visitors[n], reviews[n]))

import csv

output_file = 'files/tourlist_rates.csv'
file = csv.writer(open(output_file, 'w', encoding='utf-8', newline=''), delimiter=',')
header = ["tourlist_name", "addr", "rates", "visitors", "reviews"]
file.writerow(header)
for row in zip(names, addrs, rates, visitors, reviews):
    file.writerow(row)
