#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/4 14:35
#@Author: 徐 凯
#@File: 04_抓取电影天堂电影信息.py
#@IDE: PyCharm
'''

"""
1. 提取到主页面中的每一个电影的背后的那个url地址
    1. 拿到“2022新片精品”区域的代码
    2. 从拿到的HTML代码中提取href的值
2. 访问子页面，提取到电影的名称以及下载地址
    1. 拿到子页面的页面源代码
    2. 数据提取
"""

import requests
import re

url = "https://www.dy2018.com/"

resp = requests.get(url)
resp.encoding = "gb2312"
# print(resp.text)


# 1. 提取2022必看热片部分的HTML代码
obj1 = re.compile(r"2022新片精品.*?<ul>(?P<new>.*?)</ul>", re.S)
result1 = obj1.search(resp.text)
new_html = result1.group("new")
# print(new_html)

# 2. 提取a标签中的href值
obj2 = re.compile(r"<li><a href='(?P<movie_link>.*?)' title")

result2 = obj2.finditer(new_html)

obj3 = re.compile(r'<div id="Zoom">.*?片　　名(?P<movie>.*?)<br />'
                  r'.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S)
for item in result2:
    movie_link = item.group("movie_link")
    # 拼接子页面的url
    child_url = url.strip("/") + movie_link
    child_resp = requests.get(child_url)
    child_resp.encoding = 'gb2312'

    result3 = obj3.search(child_resp.text)
    print('-'*50)
    print(f'片名：{result3.group("movie")}\n下载地址：{result3.group("download")}')


