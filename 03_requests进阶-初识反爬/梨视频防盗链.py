#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/7 16:41
#@Author: 徐 凯
#@File: 梨视频防盗链.py
#@IDE: PyCharm
'''

import requests

while 1:

    main_url = input("请输入你需要爬取的梨视频的地址：(停止输入quit)")  # "https://www.pearvideo.com/video_1343231"
    if main_url == "quit":
        break
    contId = main_url.split("_")[-1]
    url = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}"
    headers = {
        "Referer": main_url,  # 处理防盗链
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    # print(resp.text)
    dic = resp.json()
    src_url = dic['videoInfo']['videos']['srcUrl']
    systemTime = dic["systemTime"]
    src_url = src_url.replace(systemTime, f"cont-{contId}")
    # print(src_url)
    # 下载视频
    resp = requests.get(src_url, headers=headers)
    with open(f"{contId}.mp4", mode="wb") as f:
        f.write(resp.content)
    print("视频下载完毕！")
    f.close()
