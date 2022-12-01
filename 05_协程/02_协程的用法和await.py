#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/14 17:05
#@Author: 徐 凯
#@File: 02_协程的用法和await.py
#@IDE: PyCharm
'''
import asyncio
import time


async def func1():
    print('我是func1要开始了')
    # 模拟
    # time.sleep(5)  # 这里不能用time.sleep() 因为sleep不支持协程
    # await 挂起，等，等着任务结束，回到这里继续执行
    # 被挂起的时候，cpu切换到其他任务身上了
    await asyncio.sleep(3)
    print('我是func1结束了')

async def func2():
    print('我是func2要开始了')
    # 模拟
    # time.sleep(5)  # 这里不能用time.sleep() 因为sleep不支持协程
    # await 挂起，等，等着任务结束，回到这里继续执行
    # 被挂起的时候，cpu切换到其他任务身上了
    await asyncio.sleep(5)
    print('我是func2结束了')

async def func3():
    print('我是func3要开始了')
    # 模拟
    # time.sleep(5)  # 这里不能用time.sleep() 因为sleep不支持协程
    # await 挂起，等，等着任务结束，回到这里继续执行
    # 被挂起的时候，cpu切换到其他任务身上了
    await asyncio.sleep(2)
    print('我是func3结束了')

async def main():
    f1 = func1()
    f2 = func2()
    f3 = func3()
    # 把协程对象都封装成任务对象
    t1 = asyncio.create_task(f1)
    t2 = asyncio.create_task(f2)
    t3 = asyncio.create_task(f3)

    # 等待三个任务结束
    tasks = [t1, t2, t3]
    # await 挂起 => 拉出来，外面等着
    await asyncio.wait(tasks)
    print(123456)

if __name__ == '__main__':
    s1 = time.time()
    asyncio.run(main())
    s2 = time.time()
    print(s2 - s1)
