#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/4 12:00
#@Author: 徐 凯
#@File: 04_手刃豆瓣电影TOP250.py
#@IDE: PyCharm
'''

# 思路
# 1. 拿到页面源代码
# 2. 编写正则，提取页面数据
# 3. 保存数据

import requests
import re

f = open('top250.csv', mode='w', encoding='utf-8')

url = "https://movie.douban.com/top250"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
resp = requests.get(url, headers=headers)
# resp.encoding = 'utf-8' # 解决乱码问题
pageSource = resp.text
# print(pageSource)

# 编写正则表达式
# re.S 可以让正则中的.匹配换行符
obj = re.compile(
    r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
    r'.*?<p class="">.*?导演: (?P<director>.*?)&nbsp;'
    r'.*?<br>(?P<year>.*?)&nbsp;'
    r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
    r'.*?<span>(?P<score_number>.*?)</span>', re.S)

result = obj.finditer(pageSource)
for item in result:
    print("-" * 50)
    name = item.group("name")
    print("电影：", name)
    director = item.group("director")
    print("导演：", director)
    year = item.group("year").strip() # 去掉字符串左右两边的空白
    print("年份：", year)
    score = item.group("score")
    print("评分：", score)
    score_number = item.group("score_number")
    print("评价人数：", score_number)
    f.write(f'{name},{director},{year},{score},{score_number}\n')

f.close()
resp.close()
print("豆瓣TOP250提取完毕.")

# 如何翻页提取？
# (页数 - 1) * 25
