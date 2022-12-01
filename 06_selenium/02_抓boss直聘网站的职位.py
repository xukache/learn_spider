#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/17 19:01
#@Author: 徐 凯
#@File: 02_抓boss直聘网站的职位.py
#@IDE: PyCharm
'''
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains


web = Chrome()

web.get("https://www.5iai.com/#/jobList")

# 1. 找到搜索框
input_btn = web.find_element(By.XPATH, '//*[@id="app"]/div/section/section/div/div[2]/div[1]/ul/li[1]/div/label[4]/span')
# 找不到就会报错，可能是浏览器加载没有完成
# 调用鼠标点击选择算法工程师
actions = action_chains.ActionChains(web)
actions.move_to_element(input_btn)  # 移动到位置
actions.click(input_btn)  # 点击
actions.perform()  # 实施动作
time.sleep(1)
# 抓取数据
li_list = web.find_elements(By.XPATH, "//div[@class='jobListBlock']/ul//li")
for li in li_list:
    # 不是标准xpath
    # 最后一项不可是@href，text()
    span_name = li.find_element(By.XPATH, ".//span[@class='position']")  # 岗位名称
    span_datePay = li.find_element(By.XPATH, ".//span[@class='datePay']")  # 月薪
    name = span_name.text  # 直接节点.text
    datePay = span_datePay.text  # 直接节点.text
    print(name, datePay)

    span_name.click()  # 点击
    time.sleep(2)
    # 如果出现新窗口，需要把程序跳转到新窗口，否则会报错
    web.switch_to.window(web.window_handles[-1])  # 进去新窗口
    div_job_desc = web.find_element(By.XPATH, "//div[@class='cTxt'][3]")
    job_desc = div_job_desc.text
    print(job_desc)
    print("="*30)
    # 关闭当前窗口
    web.close()  # 关闭后，selenium需要手动调整窗口到原来的窗口上
    web.switch_to.window(web.window_handles[0])  # 回到原窗口




