#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/3 21:16
#@Author: 徐 凯
#@File: 07_01_test_requests.py
#@IDE: PyCharm
'''

import requests

content = input('请输入你要检索的内容：')
url = f"https://www.sogou.com/web?query={content}"

headers = {
    # 添加一个请求头信息，UA
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
# 处理一个小小的反爬
resp = requests.get(url, headers=headers)
print(resp.text)

print(resp.request.headers) # 可以查看到请求头信息
