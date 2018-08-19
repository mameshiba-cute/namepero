#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs4
from datetime import datetime


# URLを変数に格納
req_url = "https://cunni.info/list?sex=woman&age=all&region=kanto"

# コンテンツ全体を soupに格納
soup = bs4((requests.get(req_url)).content, "html.parser")

# そのうち最新の投稿記事だけを抽出
new_post = soup.find_all("div", class_="card-content black-text")[0]

# [Debug]念のため型を確認
#print (type(new_post))

# 投稿記事から投稿時間を「文字列」で格納
#new_post_date_s = new_post.find_all("p")[0].text
# 投稿時間を文字列から「時間」に変換
#new_post_date_s = datetime.strptime(new_post_date_s, '%Y/%m/%d %H:%M:%S')

# 現在時刻を「時間」で格納
#now_date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")


print ("------------------------------------------------------------")
#print ("最新記事時刻: " + new_post_date_s)
#print ("現時刻     : " + now_date_s)
#print ("------------------------------------------------------------")
#print (new_post)
print ("------------------------------------------------------------")
print (new_post.text.encode('utf-8').replace('\n                  ', ''))
print ("------------------------------------------------------------")
