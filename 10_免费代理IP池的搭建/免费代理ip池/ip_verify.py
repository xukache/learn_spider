#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/29 10:26
#@Author: 徐 凯
#@File: ip_verify.py
#@IDE: PyCharm
'''
# 这里负责代理ip的验证工作
from proxy_redis import ProxyRedis
import asyncio
import aiohttp
import time


# 用协程最合适
async def verify_one(ip, sem, red):
    print(f"开始检测{ip}可用性")
    timeout = aiohttp.ClientTimeout(total=10)  # 10秒不行就扣分
    async with sem:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url="http://www.baidu.com", proxy="http://" + ip, timeout=timeout) as resp:
                    page_source = await resp.text()
                    if resp.status in [200, 302]:
                        # 没问题, 分值拉满
                        red.set_max_score(ip)
                        print(f"检测到{ip}，是可用的，分值设置成100分")

                    else:
                        # 有问题，扣分
                        red.desc_incrby(ip)
                        print(f"检测到{ip}，是不可用的，扣1分")
        except Exception as e:
            print("校验IP时，出错了", e)
            # 有问题，扣分
            red.desc_incrby(ip)
            print(f"检测到{ip}，是不可用的，扣1分")


async def main(red):
    # 1. 把ip全部查出来
    all_proxies = red.get_all_proxy()
    sem = asyncio.Semaphore(SEM_COUNT)  # 控制并发量，默认30
    tasks = []
    for ip in all_proxies:
        tasks.append(asyncio.create_task(verify_one(ip, sem, red)))
    if tasks:
        await asyncio.wait(tasks)


def run():
    red = ProxyRedis()
    time.sleep(START_VERIFY_WAIT_TIME)  # 初始的等待. 等待采集到数据
    while 1:
        try:
            asyncio.run(main(red))
            time.sleep(100)  # 每隔100秒跑一次
        except Exception as e:
            print("在校验时，报错了", e)
            time.sleep(100)  # 每隔100秒跑一次


if __name__ == '__main__':
    run()
