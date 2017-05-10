# -*- coding: utf-8 -*-
"""
Created on Wed May 10 02:08:42 2017

@author: Edison Song
"""
from time import strftime
from urllib import request
from bs4 import BeautifulSoup

#Daily Horoscope
date_t = strftime("%Y%m%d")
date = date_t[0:4] + '-' + date_t[4:6] + '-' + date_t[6:8]
constellation = [
    [u'牡羊座', 'aries', '0'],
    [u'金牛座', 'taurus', '1'],
    [u'雙子座', 'gemini', '2'],
    [u'巨蟹座', 'cancer', '3'],
    [u'獅子座', 'leo', '4'],
    [u'處女座', 'virgo', '5'],
    [u'天秤座', 'libra', '6'],
    [u'天蠍座', 'scorpio', '7'],
    [u'射手座', 'sagittarius', '8'],
    [u'魔羯座', 'capricorn', '9'],
    [u'水瓶座', 'aquarius', '10'],
    [u'雙魚座', 'pisces', '11'],
]
for s in constellation:
    try:
        num = s[2]
        url = 'http://astro.click108.com.tw/daily_{0}.php?iAcDay={1}&iAstro={2}'.format( num, date, num)
        data = request.urlopen(url)
        soup = BeautifulSoup(data, "html.parser")
        div_lotstars = soup.find('div', {'class': 'TODAY_CONTENT'}) # 找出 div class="TODAY_CONTENT"
        if div_lotstars == None:
            print("div .TODAY_CONTENT NOT FOUND!!")
            continue
        soup2 = BeautifulSoup(str(div_lotstars), "html.parser")
        p = soup2.findAll("p")
        ind = soup2.findAll('span')
        print(date + ' ' + s[0] + ':')
        i = len(ind)
        while i>=0:
            p[(i-1)*2] = ind[i-1]
            i-=1
        for value in p:  
            print( value.contents[0])
    except:
        print('NOT FOUND')