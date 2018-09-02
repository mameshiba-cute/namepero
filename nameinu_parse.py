#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

""" 初期変数の定義 """

# URLを変数に格納
req_url = "https://cunni.info/list?sex=woman&age=all&region=kanto"

# コンテンツ全体を soupに格納
soup = BeautifulSoup((requests.get(req_url)).content, "html.parser")

# そのうち直近 3postを抽出
new_post = [
    soup.find_all("div", class_="card-content black-text")[0],
    soup.find_all("div", class_="card-content black-text")[1],
    soup.find_all("div", class_="card-content black-text")[2],
    ]


""" 関数定義 """

# bs4.element.Tag -> str。ついでに投稿者情報(改行+余白)の置換
def __hoge__(mike):
    o = mike.encode("utf-8").replace('\n                  ', ' ')
    return o

""" メイン """

for post in new_post:
    print __hoge__(post.text)
    print ("------------------------------------------------------------")
