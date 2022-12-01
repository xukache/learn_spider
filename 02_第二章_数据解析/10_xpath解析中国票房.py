#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/7 13:41
#@Author: 徐 凯
#@File: 10_xpath解析中国票房.py
#@IDE: PyCharm
'''

import requests
from lxml import etree

# 1. 拿页面源代码
# 2. xpath提取数据

url = "http://www.boxofficecn.com/boxoffice2022"
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
resp = requests.get(url, headers=headers)
# print(resp.text)

page = etree.HTML(resp.text)
trs = page.xpath("//table/tbody/tr")[1:-6]

f = open('2022中国票房',mode="w", encoding="utf-8")
for tr in trs:
    num = tr.xpath('./td[1]//text()')
    year = tr.xpath('./td[2]//text()')
    name = tr.xpath('./td[3]//text()')
    money = tr.xpath('./td[4]//text()')
    if name:
        name = ["".join(name)]  # 这是合理的方案
    if len(money) != 1:
        money.remove('&')

    t = ",".join([num[0], year[0], name[0], money[0]]) + '\n'
    f.write(t)

print("保存完毕！")
f.close()