# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/5 20:54
#@Author: 徐 凯
#@File: 09_xpath解析.py
#@IDE: PyCharm
'''''

# 直接导入etree会找不到，卸载安装最新版lxml
from lxml import etree

f = open('./html/index.html', mode="r", encoding="utf-8")
content = f.read()  # 页面源代码

# 1. etree.HTML(页面源代码) BeautfulSoup(页面源代码)
page = etree.HTML(content)
# 2. xpath()筛选
# page.xpath()

# 语法1，根节点
# / 出现在开头，表示根节点
# xpath得到的结果永远是列表
# root = page.xpath('/')
# print(type(root))

# / 出现在中间 直接子节点
# p = page.xpath('/html/body/div/p')
# print(p)

# / 出现在中间 也有可能是找某个节点内部的东西
# text() 提取内部的文本
# s = page.xpath('/html/body/div/p/text()')
# print(s)

# // 提取的后代节点
# s = page.xpath('/html/body/div/p//text()')
# print(s)

# // 查找所有子节点 /p 所有子节点中的p
# p = page.xpath('//div/p/text()')
# print(p)

# 在xpath里 [] 里面可以给出位置，位置是从1开始数的
# zi = page.xpath('//ol/ol/li[2]/text()')
# print(zi)

# li[3]表示 上层标签中第三个li
# r = page.xpath('//li[3]/text()')
# print(r)

# 我要周大强
# 属性上的限定
# xpath语法中 @属性
# z1 = page.xpath('//ol/li[@id="10086"]/text()')
# print(z1)
# z2 = page.xpath('//li[@id="10086"]/text()')
# print(z2)

# 这里写属性选择的时候，直接复制即可（页面源代码）
# j = page.xpath('//li[@id="jay"]/text()')
# print(j)

# * 单个任意标签
# x = page.xpath('//*[@id="jolin"]/text()')
# print(x)

# 拿到ul中每一个href
# @href 拿href的值
# 方案一 A
# href = page.xpath('//ul/li/a/@href')
# print(href)
# for h in href:
#     print(h)

# 方案二 B 可扩展性更好一些
# a_list = page.xpath('//ul/li/a')
# print(a_list)
# for a in a_list:
#     href = a.xpath('./@href')[0]
#     txt_list = a.xpath('./text()')
#     if txt_list:  # 判断
#         txt = txt_list[0]
#     else:
#         txt = ""
#     # 需要把文字和href写入文件
#     print(txt, href)

# 我想要火车
# last() 最后一个
# li = page.xpath('//body/ol/li[last()]/a/text()')  # last()拿到最后一个
# print(li)
