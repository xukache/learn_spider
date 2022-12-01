#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/15 9:16
#@Author: 徐 凯
#@File: 05_协程爬明朝那些事.py
#@IDE: PyCharm
'''
import asyncio

import requests
from lxml import etree
import asyncio
import aiohttp
import aiofiles
import os


# 1. 拿到主页面源代码，不需要异步
# 2. 拿到页面源代码后，需要解析出《卷名》，《章节，href》
# 3. xxxxx

headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
def get_chapter_info(url):
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    page_source = resp.text
    # 解析
    tree = etree.HTML(page_source)
    result = []
    divs = tree.xpath("//div[@class='mulu']")  # 每个div就是一卷
    for div in divs:
        trs = div.xpath(".//table/tr")
        juan_name = trs[0].xpath(".//a/text()")
        juan_name = "".join(juan_name).strip().replace("：", "_")

        for tr in trs[1:]:
            # texts = tr.xpath("./td//text()")
            # urls = tr.xpath("./td//a/@href")
            # print(texts, urls)
            tds = tr.xpath("./td")
            for td in tds:
                txt = td.xpath(".//text()")
                href = td.xpath(".//@href")
                txt = "".join(txt).replace(" ", "_").strip()
                href = "".join(href)
                dic = {
                    "juan_name": juan_name,
                    "chapter_name": txt,
                    "chapter_url": href
                }
                result.append(dic)
    return result


async def download_one(url, file_path):
    print('我要下载了')
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            page_source = await resp.text(encoding='utf-8')
            # 拿到文章
            tree = etree.HTML(page_source)
            content = tree.xpath("//div[@class='content']/p/text()")
            content = "".join(content).replace("上一章：", "").strip()

            # 写入文件
            async with aiofiles.open(file_path, mode='w', encoding='utf-8') as f:
                await f.write(content)

    print("下载完一篇", file_path)


async def download_chapter(chapter_list):
    tasks = []
    for chapter in chapter_list:  # {juan_name:xxx,chapter_name:xxx,href:xxx}
        juan_name = chapter['juan_name']  # 文件夹名
        chapter_name = chapter['chapter_name']  # 文件名
        url = chapter['chapter_url']  # 用来下载 -> 异步任务

        if not os.path.exists(f"./明朝那些事儿/{juan_name}"):  # 判断文件夹是否存在
            os.makedirs(f"./明朝那些事儿/{juan_name}")  # 不存在就创建

        # 给出文件保存路径
        file_path = f"./明朝那些事儿/{juan_name}/{chapter_name}.txt"

        t = asyncio.create_task(download_one(url, file_path))
        tasks.append(t)
    await asyncio.wait(tasks)


def main():
    url = "https://www.mingchaonaxieshier.com/"
    chapter_list = get_chapter_info(url)
    # print(chapter_list)
    # 协程，异步下载
    # asyncio.run(download_chapter(chapter_list))
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(download_chapter(chapter_list))


if __name__ == '__main__':
    main()