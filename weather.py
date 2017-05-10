# -*- coding: utf-8 -*-
"""
Created on Wed May 10 14:09:49 2017

@author: Edison Song
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

#web crawler(weather data)
#http://e-service.cwb.gov.tw/HistoryDataQuery/index.jsp 
#Station is a number which represents a weather station of CWB
#ex: '466910'
#date is the day you want to know the weather data
#ex: '2017-05-09'
#file_place is where u want to save the data
#ex: 'C:/Users/Edison Song/Desktop'
def crawler(station, date, file_place):
    #Daily weather data
    url = 'http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station={0}&stname=%25E9%259E%258D%25E9%2583%25A8&datepicker={1}'.format(station, date)
#    url = 'http://e-service.cwb.gov.tw/HistoryDataQuery/MonthDataController.do?command=viewMain&station={0}&stname=%25E9%259E%258D%25E9%2583%25A8&datepicker={1}'.format(station, date)
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    body = soup.find('tr', {'class': 'second_tr'})
    p = body.findAll("th")
    parameter=[]
    for title in p:
        title = title.contents[0]+title.contents[2]+title.contents[4]
        parameter.append(title)
    vbody = soup.find('tbody')
    v = vbody.findAll('tr')
    tempvalue = []
    for k in v[2:]:
        temp = k.find_all('td')
        p =[]
        for strtmp in temp:
            strtmp = strtmp.string
            p.append(strtmp)
        tempvalue.append(p)
    value=[]
    for i in tempvalue:
        for j in range(1,len(i)):
            i[j] = i[j].replace(u'\xa0','')
            value.append(i)
    value = pd.DataFrame(value, columns=parameter)
    value.to_csv(file_place+'/'+date+".csv")

station = '466910'
date = '2017-05-09'
file_place = 'C:/Users/Edison Song/Desktop'
crawler(station, date, file_place)