#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/14 16:56
#@Author: 徐 凯
#@File: 01_协程概念.py
#@IDE: PyCharm
'''

import asyncio

# 加上async 就是协程函数
async def func():
    print('我是任务!')


if __name__ == '__main__':
    # func()  # 协程函数在加上括号后，产生的是一个协程对象
    # 执行协程函数的固定逻辑
    # 1. 创建好协程对象
    # 2. 用asyncio包来运行该对象
    f = func()
    # 运行方案：
    # 1. 直接run
    asyncio.run(f)
    # 2. 需要获取一个事件循环的东西
    # 创建事件循环
    event_loop = asyncio.get_event_loop()
    # 运行协程对象，直到结束
    event_loop.run_until_complete(f)

