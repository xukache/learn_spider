#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/20 20:00
#@Author: 徐 凯
#@File: 10_12306滑块.py
#@IDE: PyCharm
'''
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


# 添加代码规避自动化检测
option = Options()
# 可以去掉显示的那个“自动化工具xxxx”
option.add_experimental_option('excludeSwitches', ['enable-automation'])
# 它可以取消webdriver
option.add_argument('--disable-blink-features=AutomationControlled')
web = Chrome(options=option)
web.maximize_window()
web.implicitly_wait(10)

web.get("https://kyfw.12306.cn/otn/resources/login.html")

web.find_element(By.ID, "J-userName").send_keys("15028679697")
web.find_element(By.ID, "J-password").send_keys("qweasd123456")

web.find_element(By.ID, "J-login").click()

# 滑块处理
btn = web.find_element(By.ID, "nc_1_n1z")

action = ActionChains(web)
action.click_and_hold(btn)  # 按住
action.move_by_offset(300, 0)  # 拖拽
action.release()  # 松开
action.perform()