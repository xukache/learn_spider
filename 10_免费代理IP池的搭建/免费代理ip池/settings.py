#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/30 9:42
#@Author: 徐 凯
#@File: settings.py
#@IDE: PyCharm
'''
# redis相关配置
# redis主机ip地址
REDIS_HOST = "127.0.0.1"
# redis端口号
REDIS_PORT = 6379
# redis的数据库
REDIS_DB = 5
# redis密码
REDIS_PASSWORD = "123456"

# 存储在redis中的代理ip的key，可以进行更换
REDIS_KEY = "proxy_ip"

# 默认的ip分值
DEFAULT_SCORE = 10
# 满分
MAX_SCORE = 100
# 最低分
MIN_SCORE = 0

# 检测ip可用性
# 一次检测ip的数量
SEM_COUNT = 30
# 第一次启动时等待时间
START_VERIFY_WAIT_TIME = 10
