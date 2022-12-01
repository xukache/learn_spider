#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/19 15:45
#@Author: 徐 凯
#@File: 09_抓bilibili.py
#@IDE: PyCharm
'''
import time

import requests
from lxml import etree
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


web = Chrome()


def get_page_source(url):
    web.get(url)
    time.sleep(3)
    return web.page_source  # selenium中的page_source 是elements



if __name__ == '__main__':
    url = "https://search.bilibili.com/all?keyword=%E5%91%A8%E6%9D%B0%E4%BC%A6%E6%BC%94%E5%94%B1%E4%BC%9A2022"
    page_source = get_page_source(url)
    time.sleep(5)
    tree = etree.HTML(page_source)
    text = tree.xpath("//*[@class='mt_sm video-list row']//text()")
    print(text)