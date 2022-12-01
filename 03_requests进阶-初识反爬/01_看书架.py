#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/7 14:48
#@Author: 徐 凯
#@File: 01_看书架.py
#@IDE: PyCharm
'''

import requests

url = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"

# 需要带经过验证后的cookie
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Cookie": "GUID=8f55b413-2a9e-4408-8bb9-706501407d1b; Hm_lvt_9793f42b498361373512340937deb2a0=1667804516; sajssdk_2015_cross_new_user=1; __bid_n=18450e55070cff1d834207; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F09%252F69%252F83%252F99398369.jpg-88x88%253Fv%253D1667805118000%26id%3D99398369%26nickname%3DkacheX%26e%3D1683357189%26s%3Db600e7dc3ab02f11; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2299398369%22%2C%22%24device_id%22%3A%2218450e54f1213d-0e07635427683d-26021e51-921600-18450e54f1352d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%228f55b413-2a9e-4408-8bb9-706501407d1b%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1667805418"
}

resp = requests.get(url, headers=headers)
print(resp.json())
