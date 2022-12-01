#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/18 15:52
#@Author: 徐 凯
#@File: 05_超级鹰识别超级鹰验证码.py
#@IDE: PyCharm
'''
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
import requests
from hashlib import md5


class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                          headers=self.headers)
        return r.json()

    def PostPic_base64(self, base64_str, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
            'file_base64': base64_str
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


web = Chrome()
web.get('https://www.bilibili.com/')

# 点击进入登录页面
login = web.find_element(By.XPATH, '//*[@id="i_cecream"]/div[2]/div[1]/div[1]/ul[2]/li[1]/li/div[1]/div/span')
login.click()

time.sleep(1)
# 输入账号
user = web.find_element(By.XPATH, '//div[@class="bili-mini-account"]/input').send_keys("15028679697")
# 输入密码
password = web.find_element(By.XPATH, '//div[@class="bili-mini-password"]//input').send_keys("qweasd123456")
# 点击登录
login_btn = web.find_element(By.XPATH, '//div[@class="universal-btn login-btn"]')
login_btn.click()
time.sleep(1)

# 找到图片验证码
img = web.find_element(By.XPATH, '//div[@class="geetest_item_wrap"]')
# 截屏
bs = img.screenshot_as_png  # 返回的是字节
# 交给超级鹰来进行识别
chaojiying = Chaojiying_Client('15028679697', 'qweasd123456', '941981')
dic = chaojiying.PostPic(bs, 9501)  # 把图片的字节传递进去即可
print(dic)
dic_verif = {i[0]:(int(i.split(",")[1]), int(i.split(",")[2])) for i in dic['pic_str'].split("|")}
# 找到识别顺序验证码
img_sort = web.find_element(By.XPATH, '//div[@class="geetest_tip_img"]')
# 截屏
bs = img_sort.screenshot_as_png  # 返回的是字节
# 交给超级鹰来进行识别
dic_sort = chaojiying.PostPic(bs, 2004)  # 把图片的字节传递进去即可
print(dic_sort)

# 图片坐标
x = img.location['x']
y = img.location['y']
# 找到图片坐标
for str_ in dic_sort['pic_str']:
    time.sleep(0.5)
    actions = action_chains.ActionChains(web)
    actions.move_by_offset(x + dic_verif[str_][0], y + dic_verif[str_][1])  # 移动到位置
    actions.click()  # 点击
    actions.perform()  # 实施动作
    actions.reset_actions()
time.sleep(1)
# 点击确认
web.find_element(By.XPATH, '//div[@class="geetest_commit_tip"]').click()



