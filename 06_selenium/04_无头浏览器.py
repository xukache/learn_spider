#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/18 10:35
#@Author: 徐 凯
#@File: 04_无头浏览器.py
#@IDE: PyCharm
'''
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 无头浏览器
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")
opt.add_argument("--window-size=1920,1080")  # 设置窗口大小

web = Chrome(options=opt)
web.get("http://www.boxofficecn.com/boxofficecn")

for i in range(1, 5):
    for j in range(1, 11):
        time.sleep(2)
        movie = web.find_element(By.XPATH, f'//*[@id="tablepress-1"]/tbody/tr[{i}]/td[{j}]')
        if movie.text.strip() == "":
            continue
        time.sleep(2)
        movie.click()  # 点击
        web.switch_to.window(web.window_handles[-1])  # 跳转新页面

        tr_list = web.find_elements(By.XPATH, '//tbody/tr')
        for tr in tr_list[1:]:
            text = tr.text
            if len(text.strip()) <= 3:
                continue
            print(text)
        print("="*30)

        web.close()
        web.switch_to.window(web.window_handles[0])
