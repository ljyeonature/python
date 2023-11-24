from urllib import request
from bs4 import BeautifulSoup

url = 'https://www.yes24.com/Product/Search?domain=BOOK&query=python'
html = request.urlopen(url)

soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')

# [1] 책제목을 추출
infos = soup.select('div.item_info div.info_row > a.gd_name')
print(len(infos), '권')

for info in infos:
    print(info.text)

# [2] 이미지 정보 추출
imgUrls = soup.select('span.img_grp > a.lnk_img > em.img_bdr > img')
# print(imgUrls)
for imgUrl in imgUrls:
    imgName = imgUrl.attrs['alt']
    imgPath = imgUrl.attrs['data-original']
    print(imgName,":",imgPath)
    print(imgName)

    request.urlretrieve(imgPath,'./imgs/' + imgName + '.jpg')