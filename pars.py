# -*- coding: utf-8 -*-


import requests 
from bs4 import BeautifulSoup as bs
import webbrowser
from lxml import html
import re
 
headers = {'access-control-allow-origin' : '*',
           'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
link = 'https://www2.hm.com'


def hm_parse(base_url, headers, size, color):
    session = requests.Session() #созжание сессии
    request = session.get(base_url, headers = headers) #запрос на получения html-страницы
    if request.status_code == 200: #проверка полученного ответа
        soup = bs(request.content, 'html.parser')   #использование дополнительной библиотеки BeautifulSoup
                                                    #для многопоточного поиска
        lis = soup.find_all('li', attrs = {'class' : 'product-item'})   #поиск определенных тегов,
                                                                        #содержащих нужную информацию  
        for li in lis: #цикл по списку найденной информации для дальнейшего поиска
            #pr = li.find('span', attrs = {'class' : 'price regular'}).text //поиск ценника
            #r = re.compile(r'<.*?>')//вытаскиваем из тегов
            res = (re.compile(r'<.*?>')).sub('', (li.find('span', attrs = {'class' \
                  : 'price regular'}).text)) #использование регулярного выражения для выделения цены из тегов
            res = int(("".join(filter(lambda res: res.isnumeric(),res.split()))))#превращаем в число для сравнения
            if()
            title = li.find('a', attrs = {'class' : 'link'}).text
            href = li.find('a', attrs = {'class' : 'link'})['href']
            pic = li.find('img')['data-altimage']
            
            print(res)
            #webbrowser.open(pic, new=2)
            #print(pic)
        
size = '36'
#input('введи размер')
color = 'белый'
#input('введи цвет')
base_url = 'https://www2.hm.com/ru_ru/zhenshchiny/vybrat-kategoriyu/dresses.html?product-type=ladies_dresses&sort=stock&sizes=298_s_1_womenswear&colorWithNames=' + color + '_ffffff&image-size=small&image=model&offset=0&page-size=' + size
hm_parse('https://www2.hm.com/ru_ru/zhenshchiny/vybrat-kategoriyu/dresses.html?product-type=ladies_dresses&sort=stock&colorWithNames=%D0%B1%D0%B5%D0%B6%D0%B5%D0%B2%D1%8B%D0%B9_f5f5dc&image-size=small&image=model&offset=0&page-size=36', headers, size, color)