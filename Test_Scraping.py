#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs4
from datetime import datetime
# import re

# URLを変数に格納
req_url = "https://cunni.info/list?sex=woman&age=all&region=kanto"

# コンテンツ全体を soupに格納
soup = bs4((requests.get(req_url)).content, "html.parser")

# そのうち直近 3postを抽出
new_post = [soup.find_all("div", class_="card-content black-text")[0].encode('utf-8').replace('\n                  ', ''),
            soup.find_all("div", class_="card-content black-text")[1].encode('utf-8').replace('\n                  ', ''),
            soup.find_all("div", class_="card-content black-text")[2].encode('utf-8').replace('\n                  ', '')]

"""
# macでバックスラッシュは "Option + ¥"な。改行コード記載するときにいつも間違える。
print ("------------------------------------------------------------")
print new_post[0]
print ("------------------------------------------------------------")
print new_post[1]
print ("------------------------------------------------------------")
print new_post[1]
print ("------------------------------------------------------------")
"""

hoge = bs4(new_post[0], "html.parser").find_all("p")[0].text.encode('utf-8')

tdatetime = datetime.strptime(hoge, '%Y/%m/%d %H:%M:%S')
print ('直近の投稿時刻: ' + str(tdatetime))
print ('現在の時刻   : ' + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))



"""
#for div in soup.find_all('div'):
#    print (soup.find_all(class_="card-content black-text"))

# タイトル文字列を表示
#print (soup.title.string.encode('utf-8'))
s1 = soup.title.string
#type(s1)
print(s1.encode('utf-8'))


print ("▼--- コンテンツの勉強 ------------------------------------------")

#for link in soup.find_all("div", class_="card-content black-text"):
#print (soup.find_all("div", class_="card-content black-text").encode('utf-8'))

#for div in soup.find_all("div", class_="card-content black-text"):
#    print ("------------------------------------------------------------")
#    print (div.text.encode('utf-8'))
#    print (div.encode('utf-8'))
print (soup.find_all("div", class_="card-content black-text")[0])

"""
"""
print ("▼--- tagの勉強 -----------------------------------------------")
tag = soup.div
print (tag)
print ("------------------------------------------------------------")
print (tag['class'])

"""
