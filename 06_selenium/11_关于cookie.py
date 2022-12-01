#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/20 20:31
#@Author: 徐 凯
#@File: 11_关于cookie.py
#@IDE: PyCharm
'''
# 以前的逻辑：requests登录，requests爬数据
# 现在可以换，selenium登录，拿到cookie，存起来，requests去爬数据
import time

import requests
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


url = "https://www.17k.com/"
web = Chrome()
web.get(url)
web.implicitly_wait(10)

# 进入登陆
web.find_element(By.XPATH, "//*[@class='cont_box']//dd[@class='login']/a[1]").click()
iframe = web.find_element(By.XPATH, "//div[@class='QUI_POP_BOX ']//div[@class='QUI_POP_CONT']/iframe")
web.switch_to.frame(iframe)

time.sleep(1)
web.find_element(By.XPATH, "/html/body/form/dl/dd[2]/input").send_keys("15028679697")
web.find_element(By.XPATH, "/html/body/form/dl/dd[3]/input").send_keys("qweasd123456+")

web.find_element(By.XPATH, "//*[@id='protocol']").click()  # 阅读并同意
time.sleep(1)
web.find_element(By.XPATH, "/html/body/form/dl/dd[5]/input").click()

# 登陆成功后，睡眠一下
time.sleep(3)
# 记录cookie
cookies = web.get_cookies()  # 加载的cookie是浏览器上的cookie，所以，包括了服务器返回的cookie和js执行加载的cookie

# 处理cookie
cookie = {}
for item in cookies:
    name = item['name']
    value = item['value']
    cookie[name] = value

# requests就可以直接使用cookie了
import requests

resp = requests.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919", cookies=cookie)
print(resp.text)