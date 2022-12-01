#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/3 21:16
#@Author: 徐 凯
#@File: 07_01_test_requests.py
#@IDE: PyCharm
'''

import requests

# 爬取百度的页面源代码
url = "http://www.baidu.com"
resp = requests.get(url)
resp.encoding = 'utf-8'

print(resp.text) # 拿到页面源代码
