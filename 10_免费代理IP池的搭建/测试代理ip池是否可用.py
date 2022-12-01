#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/29 15:35
#@Author: 徐 凯
#@File: 测试代理ip池是否可用.py
#@IDE: PyCharm
'''

import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}


def get_proxy():
    url = "http://127.0.0.1:5800/get_proxy"
    resp = requests.get(url, headers=headers)
    dic = resp.json()
    proxy = {
        "http": "http://" + dic["ip"],
        "https": "http://" + dic["ip"],
    }
    return proxy


url = "http://www.baidu.com/s?wd=ip"
# 上述url会自动的重定向到https上
# requests会自动的像浏览器一样帮助我们完成这个重定向
# 第一次请求的是http，被重定向了
# 第二次请求的是https
proxy = get_proxy()
resp = requests.get(url, proxies=proxy, headers=headers, timeout=10)
resp.encoding = "utf-8"
print(resp.text)

