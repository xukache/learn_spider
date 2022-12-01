#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/7 15:57
#@Author: 徐 凯
#@File: 02_模拟登录.py
#@IDE: PyCharm
'''

import requests

# 用户名，密码，url -> 抓包

url = "https://passport.17k.com/ck/user/login"
data = {
    "loginName": "15028679697",
    "password": "qweasd123456+"
}
resp = requests.post(url, data=data)
# print(resp.text)
# print(resp.headers)
# 如何拿到cookie
d = resp.cookies

# 书架
url = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"
resp_2 = requests.get(url, cookies=d)
print(resp_2.text)

