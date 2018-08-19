#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

# URLを変数に格納
req_url = "https://cunni.info/list?sex=woman&age=all&region=kanto"

# コンテンツ全体を soupに格納
soup = BeautifulSoup((requests.get(req_url)).content, "html.parser")

# そのうち最新の投稿記事だけを抽出
new_post = soup.find_all("div", class_="card-content black-text")[0]

print (new_post.text.encode('utf-8'))

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
