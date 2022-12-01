#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/28 20:39
#@Author: 徐 凯
#@File: 02_爬链家.py
#@IDE: PyCharm
'''
import requests
from lxml import etree
import pymongo

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}


def get_page_source(url):  # 获取页面源代码
    resp = requests.get(url, headers=headers)
    return resp.text


def parse_data(page_source):  # 解析页面源代码，获取到数据
    tree = etree.HTML(page_source)
    li_list = tree.xpath("//*[@class='sellListContent']/li")

    result = []
    for li in li_list:
        title = li.xpath(".//*[@class='title']/a/text()")
        if not title:
            continue
        title = title[0]

        position = li.xpath(".//*[@class='positionInfo']//text()")
        position = "".join(position).strip().replace(" ", "")

        house_infos = li.xpath(".//*[@class='houseInfo']//text()")
        infos = house_infos[0].replace(" ", "").split("|")

        total_price = li.xpath(".//*[@class='priceInfo']/div[1]//text()")
        unit_price = li.xpath(".//*[@class='priceInfo']/div[2]//text()")
        total_price = "".join(total_price).replace(" ", "")
        unit_price = "".join(unit_price).replace(" ", "")

        dic = {
            "title": title,
            "position": position,
            "infos": infos,
            "total_price": total_price,
            "unit_price": unit_price,
        }
        result.append(dic)
    return result


def save_data(data):
    conn = pymongo.MongoClient(host="localhost", port=27017)
    db = conn['lianjia']
    db.house_info.insert_many(data)
    conn.close()


def main():
    url = "https://wh.lianjia.com/ershoufang/"
    page_source = get_page_source(url)
    data = parse_data(page_source)
    save_data(data)


if __name__ == '__main__':
    main()
