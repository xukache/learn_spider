#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/14 11:43
#@Author: 徐 凯
#@File: 04_多进程.py
#@IDE: PyCharm
'''

from threading import Thread
from multiprocessing import  Process


def work(name):
    for i in range(999):
        print(name, i)


if __name__ == '__main__':
    p1 = Process(target=work, args=("进程1", ))
    p2 = Process(target=work, args=("进程2", ))
    p3 = Process(target=work, args=("进程3", ))

    p1.start()
    p2.start()
    p3.start()

    # 进程，单独的，独立的程序
    # 线程，用多线程，让一个程序变得高效
