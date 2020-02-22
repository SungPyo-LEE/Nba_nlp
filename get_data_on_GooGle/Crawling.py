import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import sys
driver=webdriver.Chrome('chromedriver')
driver.get('https://www.google.com/search?q=oklahomacitythunder&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjVp-SoseXnAhUBBKYKHU97C5UQ_AUoBHoECBoQBg&biw=929&bih=888')

all_news_url = []

for i in range(3, 12):
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    xpath = """//*[@id="nav"]/tbody/tr/td[%s]/a/span""" % i
    e=driver.find_element_by_xpath(xpath)
    e.click()
    id_res = soup.find("div", {"id": "res"})
    for link in id_res.findAll("a"):
        if 'href' in link.attrs:
            all_news_url.append(link.attrs['href'])


news_text = []
sequence = []
for news_url in all_news_url:
    try:
        a = 1
        req = requests.get(news_url)
        ht = req.text
        so = BeautifulSoup(ht, 'html.parser')
        p = so.find_all("p")
        for t in p:
            news_text.append(t.get_text())
            sequence.append(a)
            a+=1
    except:
        print(news_url)

#2차원 array로 만든다
News_text_2array = np.array([news_text, sequence])
News_text_2array = np.transpose(News_text_2array)
my_df=pd.DataFrame(data = News_text_2array)

my_df.to_csv("C:/Users/sunng/PycharmProjects/Nba_Playoff_predic/raw_data/raw_data.csv", sep=',', encoding='utf-8')

