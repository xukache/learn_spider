#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/4 16:40
#@Author: 徐 凯
#@File: 07_bs4解析.py
#@IDE: PyCharm
'''

from bs4 import BeautifulSoup

html = """
<ul>
    <li><a href="zhangwuji.com">张无忌</a></li>
    <li id="abc"><a href="zhouxingchi.com">周星驰</a></li>
    <li><a href="zhubajie.com">猪八戒</a></li>
    <li><a href="wuzetian.com">武则天</a></li>
</ul>
"""

# 1. 初始化BeautifulSoup对象
page = BeautifulSoup(html, "html.parser")
# page.find("标签名", attrs={"属性":"值"})  # 查找某个元素，只会找到一个结果
# page.find_all("标签名", attrs={"属性":"值"})  # 查找某个元素，找到一堆结果

# li = page.find("li", attrs={"id":"abc"})
# a = li.find("a")
# print(a.text)  # 拿文本
# print(a.get("href"))  # 拿属性， get("属性名")

# li_list = page.find_all('li')
# for li in li_list:
#     a = li.find('a')
#     text = a.text
#     href = a.get("href")
#     print(text, href)