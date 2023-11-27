"""
네이버 로그인 페이지를 실행하기
    크롬에서 네이버 로그인 페이지를 개발자모드에서 확인하여
    로그인 폼의 아이디와 비밀번호 입력 name 확인
    아이디 : id
    비밀번호 : pw
"""

from selenium import webdriver

# 0. 네이버 로그인 정보
myID = 'sam5834@naver.com'
myPW = 'pIguru22!'

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(2)

# 2. 페이지 접속
driver.get('https://accounts.kakao.com/login/?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fwww.daum.net#login')

# 3. 동작
# driver.find_element("id", "id")
# driver.find_element("name", "id")
# driver.find_element("class", "id")
userId = driver.find_element_by_id("loginId--1")
userPw = driver.find_element_by_id("password--2")
userId.send_keys(myID)
userPw.send_keys(myPW)

driver.find_element_by_class_name("submit").click()





