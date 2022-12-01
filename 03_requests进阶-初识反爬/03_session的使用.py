#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/7 16:16
#@Author: 徐 凯
#@File: 03_session的使用.py
#@IDE: PyCharm
'''
import requests

# 可以自动地保持会话（自动处理cookie）
# 1. 创建一个session
session = requests.session()

# 2. 可以提前给session设置好请求头或cookie
session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

# # 可用可不用
# session.cookies = {
#     # 可以把一些放进来，格式是字典
# }

# # 3. 发请求
# session.get()
# session.post()

# 登录
url = "https://passport.17k.com/ck/user/login"
data = {
    "loginName": "15028679697",
    "password": "qweasd123456+"
}
# requests.post()
session.post(url, data=data)

# 后续的请求，都会带着cookie
url = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"
resp_2 = session.get(url)
print(resp_2.text)

