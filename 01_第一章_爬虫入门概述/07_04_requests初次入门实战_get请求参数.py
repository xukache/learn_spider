#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/3 21:16
#@Author: 徐 凯
#@File: 07_01_test_requests.py
#@IDE: PyCharm
'''

import requests

url = "https://movie.douban.com/j/chart/top_list"

params = {
    "type": "13",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20",
}

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

# 处理一个小小的反爬
resp = requests.get(url, params=params, headers=headers)

# print(resp.text)
print(resp.json())
print(resp.request.url)
