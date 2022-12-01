#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/14 20:59
#@Author: 徐 凯
#@File: 04_爬虫必备异步的包.py
#@IDE: PyCharm
'''

import asyncio

import aiohttp
import aiofiles


async def download(url):
    print('我要开始下载了', url)
    file_name = url.split('/')[-1]
    # 我要发送请求
    # 如果with后面是一个异步的包，绝大多数这里前面是async
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            # 等待服务器返回结果
            content = await resp.content.read()

            # # 慢
            # with open(file_name, mode='wb') as f:
            #     f.write(content)
            async with aiofiles.open(file_name, mode='wb') as f:
                await f.write(content)

    print("一张图片下载完毕！")


async def main():
    urls = [
        "https://www.xiurenji.vip/uploadfile/202110/20/1F214426892.jpg",
        "https://www.xiurenji.vip/uploadfile/202110/20/91214426753.jpg"
    ]
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(download(url)))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    # asyncio.run(main())
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())