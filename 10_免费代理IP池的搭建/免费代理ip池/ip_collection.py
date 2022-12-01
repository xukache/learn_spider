#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/29 10:26
#@Author: 徐 凯
#@File: ip_collection.py
#@IDE: PyCharm
'''
# 这里负责代理ip的抓取
from proxy_redis import ProxyRedis
import requests
from lxml import etree
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}


def get_kuai_ip(red):
    url = "https://www.kuaidaili.com/free/intr/"
    resp = requests.get(url=url, headers=headers)
    tree = etree.HTML(resp.text)
    trs = tree.xpath("//table//tr")
    for tr in trs:
        ip = tr.xpath("./td[1]/text()")
        port = tr.xpath("./td[2]/text()")
        if not ip:
            continue
        ip = ip[0]
        port = port[0]
        proxy_ip = ip + ":" + port
        print(proxy_ip)
        red.add_proxy_ip(proxy_ip)  # 增加新的ip地址


def get_another_ip(red):
    url = "https://ip.jiangxianli.com/?page=1"
    resp = requests.get(url=url, headers=headers)
    tree = etree.HTML(resp.text)
    trs = tree.xpath("//tbody/tr")
    for tr in trs:
        ip = tr.xpath("./td[1]/text()")
        port = tr.xpath("./td[2]/text()")
        if not ip:
            continue
        ip = ip[0]
        port = port[0]
        proxy_ip = ip + ":" + port
        print(proxy_ip)
        red.add_proxy_ip(proxy_ip)  # 增加新的ip地址


def run():  # 启动爬虫
    red = ProxyRedis()  # 创建好存储
    while 1:
        try:
            get_kuai_ip(red)
            get_another_ip(red)
        except:
            print("崩了")
        time.sleep(60)  # 每分钟跑一次

if __name__ == '__main__':
    pass
    # from multiprocessing import Process
    # p = Process(target=run)  # 子进程
    # p.start()

