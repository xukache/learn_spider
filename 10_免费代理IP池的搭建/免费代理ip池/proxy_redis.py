#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/29 10:28
#@Author: 徐 凯
#@File: proxy_redis.py
#@IDE: PyCharm
'''
# 负责该项目所有redis相关操作
import random

from redis import Redis
import random
from settings import *


class ProxyRedis:
    # self.red 链接
    def __init__(self):
        self.red = Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            db=REDIS_DB,
            password=REDIS_PASSWORD,
            decode_responses=True
        )

    """
    需要的功能：
        1. 存储
            先判断是否存在该ip，如果存在，就不进行新增操作
            
        2. 需要校验所有的ip
            查询所有ip
        3. 分值拉满 ip可用
        4. 扣分 ip不可用
        
        5. 查询可用的代理ip
        # 先给满分的
        # 没有满分的，给有分的
        # 如果都是没有分的，不给
            
    """

    def add_proxy_ip(self, ip):
        # 1. 判断是否有ip
        if not self.red.zscore(REDIS_KEY, ip):
            self.red.zadd(REDIS_KEY, {ip: DEFAULT_SCORE})
            print("采集到新的ip地址", ip)
        else:
            print("采集的已经存在", ip)

    def get_all_proxy(self):
        return self.red.zrange(REDIS_KEY, 0, -1)

    def set_max_score(self, ip):
        self.red.zadd(REDIS_KEY, {ip: MAX_SCORE})

    def desc_incrby(self, ip):
        # 先查询出分值
        score = self.red.zscore(REDIS_KEY, ip)
        # 如果分值还有，扣1分
        if score and score > MIN_SCORE:
            self.red.zincrby(REDIS_KEY, -1, ip)
        # 如果分值已经扣没了 可以删除
        else:
            self.red.zrem(REDIS_KEY, ip)

    def get_keyong_proxy(self):
        ips = self.red.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE, 0, -1)
        if ips:
            # 随机取一个，返回
            return random.choice(ips)
        else:  # 没有满分的
            ips = self.red.zrangebyscore(REDIS_KEY, DEFAULT_SCORE + 1, MAX_SCORE - 1, 0, -1)
            # 判断
            if ips:
                return random.choice(ips)
            else:
                print("没有能用的了")
                return None

