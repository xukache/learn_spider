#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/17 18:51
#@Author: 徐 凯
#@File: 01_初始selenium.py
#@IDE: PyCharm
'''

# 导入驱动的py包
from selenium.webdriver import Chrome

web = Chrome()

# 打开url
web.get("https://baidu.com/")

web.maximize_window()  # 设置为最大窗口

# 拿到一些内容
print(web.title)