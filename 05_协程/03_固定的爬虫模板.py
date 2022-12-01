#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/14 20:26
#@Author: 徐 凯
#@File: 03_固定的爬虫模板.py
#@IDE: PyCharm
'''

import asyncio

async def get_page_source(url):
    # 网络请求, requests不支持异步
    print("发送请求到", url)
    await asyncio.sleep(3)
    print('拿到了页面源代码')
    return "我就是源代码"

async def main():
    urls = [
        "http://www.baidu.com",
        "http://www.taobao.com",
        "http://www.google.com",
        "http://www.jd.com",
    ]
    tasks = []
    for url in urls:
        f = get_page_source(url)
        t = asyncio.create_task(f)
        tasks.append(t)

    # 如果需要返回值
    # 方案一
    # result, pending = await asyncio.wait(tasks)
    # for r in result:
    #     print(r.result())  # 拿结果
    # 方案二
    results = await asyncio.gather(*tasks)  # 和wait差不多
    for r in results:
        print(r)
if __name__ == '__main__':
    asyncio.run(main())