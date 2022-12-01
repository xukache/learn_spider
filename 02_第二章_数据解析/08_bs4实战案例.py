#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/5 19:15
#@Author: 徐 凯
#@File: 08_bs4实战案例.py
#@IDE: PyCharm
'''

import requests
from bs4 import BeautifulSoup

"""
注意：
    子页面的url如果开头是/，直接在其前面拼接上域名即可
    子页面的url不是/开头，此时需要找到主页面的url，去掉最后一个/后面的所有内容，和当前获取到的url进行拼接
    
"""
domain = "https://www.umei.cc"
url = "https://www.umei.cc/bizhitupian/xiaoqingxinbizhi/"

headers = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
resp = requests.get(url, headers=headers)
resp.encoding = "utf-8"
# print(resp.text)

main_page = BeautifulSoup(resp.text, "html.parser")
a_list = main_page.find_all("a", attrs={"class":"img_album_btn"})
# print(len(a_list))
n = 1
for a in a_list:
    href = a.get("href")
    child_url = domain + href
    child_resp = requests.get(child_url, headers=headers)
    child_resp.encoding = "utf-8"
    # 子页面的bs对象
    child_bs = BeautifulSoup(child_resp.text, "html.parser")
    div = child_bs.find("div", attrs={"class":"big-pic"})
    img_src = div.find("img").get("src") # 拿到图片的下载路径
    # print(img_src)
    # 下载图片
    img_resp = requests.get(img_src)
    with open(f"./image/{n}.jpg", mode="wb") as f:  # 注意，此时写入到文件的是字节，所以必须是wb
        f.write(img_resp.content)  # 把图片信息写入到文件中

    print(f"图片{n}下载完毕。")
    n += 1