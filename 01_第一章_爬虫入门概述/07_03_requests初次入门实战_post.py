#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/3 21:16
#@Author: 徐 凯
#@File: 07_01_test_requests.py
#@IDE: PyCharm
'''

import requests

url = "https://fanyi.baidu.com/sug"

data = {
    "kw": input("请输入一个单词：")
}

resp = requests.post(url, data=data)

print(resp.text) # 拿到的是文本字符串
print(resp.json()) # 拿到的直接是json数据