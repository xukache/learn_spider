#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/4 10:33
#@Author: 徐 凯
#@File: 03_re模块讲解.py
#@IDE: PyCharm
'''

import re

# result = re.findall(r"a", "我afbfbf，我有200元")
# print(result)

# result = re.findall(r"\d+", "我今年18岁，我有200元")
# print(result)

# # 重点，多多练习
# result = re.finditer(r"\d+", "我今年18岁，我有200元")
# for item in result: # 从迭代器中拿到内容
#     print(item.group()) # 从匹配到的结果中拿到数据

# # 只会匹配到第一次匹配的内容
# result = re.search(r"\d+", "我叫周杰伦，今年32岁，我的班级是3年2班")
# print(result.group())

# # match，在匹配时，从字符串的开头进行匹配，类似在正则前面加上了^
# result = re.match(r"\d+", "我叫周杰伦，今年32岁，我的班级是3年2班")
# print(result)

# # 预加载，提前吧正则对象加载完毕
# obj = re.compile(r"\d+")
# # 直接把加载好的正则进行使用
# result = obj.findall("我叫周杰伦，今年32岁，我的班级是3年2班")
# print(result)

# 想要提取数据必须用小括号括起来，可以单独起名字
# (?P<名字>正则)
# 提取数据的时候，需要group("名字")
s = """
<div class='西游记'><span id='10010'>中国联通</span></div>
<div class='西游记'><span id='10086'>中国移动</span></div>
"""
obj = re.compile(r"<span id='(?P<id>\d+)'>(?P<name>.*?)</span>")

result = obj.finditer(s)
for item in result:
    id = item.group("id")
    print(id)
    name = item.group("name")
    print(name)