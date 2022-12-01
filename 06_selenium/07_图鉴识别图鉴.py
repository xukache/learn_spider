#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/19 12:31
#@Author: 徐 凯
#@File: 07_图鉴识别图鉴.py
#@IDE: PyCharm
'''
# 用requests来完成登录过程
# 一般情况下，在使用验证码的时候，要保持住会话，否则容易引起验证码识别不成功的现象
import requests
import base64
import json


def base64_api(uname, pwd, img, typeid):
    # 官方的案例是把图片处理成了base64
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": img}  # img已经是base64
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""


session = requests.session()
# 1.设置好头信息
session.headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

# 2. 加载一个最原始的cookie（可能需要可能也不需要，好习惯）
session.get("http://www.ttshitu.com/login.html?spm=null")

# 3. 发送请求，拿到验证码
verify_url = "https://admin.ttshitu.com/captcha_v2?_=1668832956632"
resp = session.get(verify_url)
img = resp.json()['img']
imgId = resp.json()['imgId']  # 不是每个网站都是这样

# 4. 识别验证码
verify_code = base64_api("15028679697", "qweasd123456", img, 1)

username = "15028679697"
password = "qweasd123456"

# 准备登录
login_url = "https://admin.ttshitu.com/common/api/login/user"  # url屁股上总能看见_ t n => 时间戳
data = {
    "captcha": verify_code,
    "developerFlag": False,
    "imgId": imgId,
    "needCheck": True,
    "password": password,
    "userName": username,
}
# Request Payload
# 第一，发送出去的是json
# 第二，请求一定是post
# 第三，请求头里一定有content-type:application/json;
# json.dumps()把字典变成json
# resp = session.post(login_url, data=json.dumps(data), headers={"content-type": "application/json;charset=UTF-8"})
resp = session.post(login_url, json=data)  # 如果给了json参数，自动转化处理，以及请求头的处理
print(resp.text)

