import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

driver=webdriver.Chrome('chromedriver')
driver.get('https://www.google.com/search?q=oklahomacitythunder&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjVp-SoseXnAhUBBKYKHU97C5UQ_AUoBHoECBoQBg&biw=929&bih=888')

html=driver.page_source
soup=BeautifulSoup(html, 'html.parser')

id_res = soup.find("div", {"id":"res"})

all_news_url = []
for link in id_res.findAll("a"):
    if 'href' in link.attrs:
        all_news_url.append(link.attrs['href'])
news_text = []
for news_url in all_news_url:
    try:
        req = requests.news_url
        ht = req.text
        so = BeautifulSoup(ht, 'html.parser')
        news_text.append(so.get_text())
    except:
        print(news_url)
print(news_text)