#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/19 13:48
#@Author: 徐 凯
#@File: 08_selenium搞定bilibili登录.py
#@IDE: PyCharm
'''
import time
import json
import base64
import requests
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def base64_api(uname, pwd, img, typeid):
    # 官方的案例是把图片处理成了base64
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""


web = Chrome()
web.implicitly_wait(10)  # 软等待
web.get("https://www.bilibili.com/")

web.find_element(By.XPATH, '//*[@class="header-login-entry"]/span').click()

web.find_element(By.XPATH, '//*[@class="bili-mini-account"]/input').send_keys("15028679697")
web.find_element(By.XPATH, '//*[@class="bili-mini-password"]//input').send_keys("qweasd123456")

time.sleep(2)  # 网络原因，需要硬等待
web.find_element(By.XPATH, '//*[@class="universal-btn login-btn"]').click()

# 获取验证码区域
time.sleep(1)
tu = web.find_element(By.XPATH, '//*[@class="geetest_panel_box geetest_no_logo geetest_panelshowclick"]')
tu.screenshot("./tu.png")  # 拿到图片
# tu.screenshot_as_png()  # 拿到字节
result = base64_api("15028679697", "qweasd123456", "./tu.png", 27)
time.sleep(3)
print(result)

rs = result.split("|")
for r in rs:
    x, y = r.split(",")
    x = int(x)
    y = int(y)
    # 找到截图的那个位置的左上角，横向移动xxx，纵向移动xxx，点击
    ActionChains(web).move_by_offset(tu.location['x']+x, tu.location['y']+y).click().perform()
    ActionChains(web).reset_actions()
    # 有点问题，相对图片中心点坐标移动
    # ActionChains(web).move_to_element_with_offset(tu, xoffset=x, yoffset=y).click().perform()  # 移动到元素的左上角，依次点击

time.sleep(1)
web.find_element(By.XPATH, '//*[@class="geetest_commit_tip"]').click()