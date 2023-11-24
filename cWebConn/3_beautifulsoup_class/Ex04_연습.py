# 1.
from urllib import request
from bs4 import BeautifulSoup
# 녹색 글자만 추출하여 출력
# url = 'http://www.pythonscraping.com/pages/warandpeace.html'

# html = request.urlopen(url)
# soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')

# greens = soup.select('span.green')
# for green in greens:
#     print(green.text)

# http://www.pythonscraping.com/pages/page3.html
# 아이템과 가격을 추출
# url = 'http://www.pythonscraping.com/pages/page3.html'
# html = request.urlopen(url)
# soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
#
# contains = soup.select('.gift > td:nth-child(odd)')
# for contain in contains:
#     print(contain.text)

# https://wikidocs.net/
#
#  1) 책 제목과 저자만 추출
#  2) 이미지 다운
# encoding=utf8

url = 'https://wikidocs.net/'
html = request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')

imgs = soup.select('.book-image')
titles = soup.select('.book-subject')
authors = soup.select('.menu_link')
print(titles)
for result in zip(titles,authors):
    print(result[0].text, ":", result[1].text)

from urllib import parse
for result in zip(titles,imgs):
    imgPath = 'https://wikidocs.net' + parse.quote(result[1].attrs['src'])
    request.urlretrieve(imgPath, './images/' + result[0].text.replace(":","") + '.jpg')

