#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/14 10:45
#@Author: 徐 凯
#@File: 03_多线程的应用.py
#@IDE: PyCharm
'''

import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
import time


def str_tool(lst):
    lst = "".join(lst)
    return lst.strip()


def get_movie_info(year):
    # 抓取1996年的票房
    f = open(f"./历年电影票房/{year}.csv", mode="w", encoding="utf-8")
    url = f"http://www.boxofficecn.com/boxoffice{year}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    tree = etree.HTML(resp.text)
    trs = tree.xpath("//table/tbody/tr")[1:]
    for tr in trs:
        num = tr.xpath("./td[1]//text()")
        year = tr.xpath("./td[2]//text()")
        name = tr.xpath("./td[3]//text()")
        money = tr.xpath("./td[4]//text()")

        num = str_tool(num)
        year = str_tool(year)
        name = str_tool(name)
        money = str_tool(money)
        f.write(f"{num}, {year}, {name}, {money}\n")


if __name__ == '__main__':
    # s1 = time.time()  # 当前系统时间的时间戳
    # for y in range(1994, 2023):
    #     get_movie_info(y)
    # s2 = time.time()  # 执行之后的时间戳
    # print(s2 - s1)  # 37.70

    s1 = time.time()
    with ThreadPoolExecutor(8) as t:
        for y in range(1994, 2023):
            t.submit(get_movie_info, y)
    s2 = time.time()
    print(s2 - s1)  # 23.09