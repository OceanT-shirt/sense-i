import requests
import re
from bs4 import BeautifulSoup
import uuid

# https://qiita.com/NakaokaRei/items/03dd5587babcc5f772d3

i = 0
for page in range(1, 223):
    r = requests.get('https://wear.jp/men-coordinate/?pageno='+str(page))
    soup = BeautifulSoup(r.text,'lxml')
    imgs = soup.find_all('img', attrs={"data-originalretina": re.compile('^//cdn.wimg.jp/coordinate')})
    goods = soup.find_all('p', attrs={"class" : "btn"})
    goods = goods[1::2]
    for img, good in zip(imgs, goods):
        i = i+1
        print('http:' + img["data-originalretina"])
        good_ = good.find('span')
        r = requests.get('http:' + img["data-originalretina"])
        with open(str('picture/')+str(i)+'_'+str(good_.string)+str('.jpeg'),'wb') as file:
                file.write(r.content)


for page in range(1, 223):
    r = requests.get('https://wear.jp/women-coordinate/?pageno='+str(page))
    soup = BeautifulSoup(r.text,'lxml')
    imgs = soup.find_all('img', attrs={"data-originalretina": re.compile('^//cdn.wimg.jp/coordinate')})
    goods = soup.find_all('p', attrs={"class" : "btn"})
    goods = goods[1::2]
    for img, good in zip(imgs, goods):
        i = i+1
        print('http:' + img["data-originalretina"])
        good_ = good.find('span')
        r = requests.get('http:' + img["data-originalretina"])
        with open(str('picture/')+str(i)+'_'+str(good_.string)+str('.jpeg'),'wb') as file:
                file.write(r.content)
