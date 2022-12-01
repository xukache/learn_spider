#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/14 9:30
#@Author: 徐 凯
#@File: 01_多线程.py
#@IDE: PyCharm
'''
from threading import Thread  # 线程
# # 一个函数，多线程多进程中表示一个任务
# def work():
#     for i in range(500):
#         print("work中的打印", i)
#
#
# # 默认的进程和线程，叫主进程和主线程
# if __name__ == '__main__':
#     # work()  # 函数中的调用，和多线程无关
#     t = Thread(target=work)  # 创建一个线程
#     # 想要运行这个线程，需要start()
#     t.start()  # 启动t这个线程
#
#     for i in range(500):
#         print("主线程中的打印", i)


def work(name):
    for i in range(10000):
        print("work中的打印", name, i)


if __name__ == '__main__':
    # target的参数不能加括号
    # args必须是元组，如果只有一个参数，必须加逗号
    t1 = Thread(target=work, args=("线程1",))
    t1.start()

    t2 = Thread(target=work, args=("线程2",))
    t2.start()

    t3 = Thread(target=work, args=("线程3",))
    t3.start()

    # 1. cpu未必扛得住
    # 2. 创建线程也要消耗资源
    # 3. 对方的服务器扛不住
    # 4. 线程数量不宜太多，一般选择cpu核数（8-16）

    # 20000个任务 -> 16
    # python直接提供了线程池，帮助完成上述操作
    # 线程池：装有一堆线程的一个池子，我们只需要把任务扔进去即可