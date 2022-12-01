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
web.get('https://www.chaojiying.com/user/login/')

web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys("15028679697")
time.sleep(0.5)
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys("qweasd123456")
time.sleep(0.5)
img = web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/div/img')
# 截屏
bs = img.screenshot_as_png  # 返回的是字节
# 交给超级鹰来进行识别
chaojiying = Chaojiying_Client('15028679697', 'qweasd123456', '941981')
dic = chaojiying.PostPic(bs, 1004)  # 把图片的字节传递进去即可
print(dic)
code = dic['pic_str']
# 输入验证码
time.sleep(0.5)
web.find_element(By.XPATH, "//p[@class='login_form_pass']/input[@name='imgtxt']").send_keys(code)
# 点击登录
time.sleep(1)
web.find_element(By.XPATH, "//p/input[@class='login_form_input_submit']").click()