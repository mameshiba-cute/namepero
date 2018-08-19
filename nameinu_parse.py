#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

# URLを変数に格納
req_url = "https://cunni.info/list?sex=woman&age=all&region=kanto"

# コンテンツ全体を soupに格納
soup = BeautifulSoup((requests.get(req_url)).content, "html.parser")

# そのうち直近 3postを抽出
new_post = [soup.find_all("div", class_="card-content black-text")[0],
            soup.find_all("div", class_="card-content black-text")[1],
            soup.find_all("div", class_="card-content black-text")[2]]
