#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/20 21:09
#@Author: 徐 凯
#@File: 11_处理cookies.py
#@IDE: PyCharm
'''

lst = [{'domain': '.17k.com', 'httpOnly': False, 'name': 'Hm_lpvt_9793f42b498361373512340937deb2a0', 'path': '/', 'secure': False, 'value': '1668950361'}, {'domain': '.17k.com', 'expiry': 1684502360, 'httpOnly': False, 'name': 'c_channel', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.17k.com', 'expiry': 1684502360, 'httpOnly': False, 'name': 'accessToken', 'path': '/', 'secure': False, 'value': 'avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F09%252F69%252F83%252F99398369.jpg-88x88%253Fv%253D1667805118000%26id%3D99398369%26nickname%3DkacheX%26e%3D1684502359%26s%3Df10b48054c0a61a9'}, {'domain': '.17k.com', 'expiry': 1684502360, 'httpOnly': False, 'name': 'c_csc', 'path': '/', 'secure': False, 'value': 'web'}, {'domain': '.17k.com', 'expiry': 1703510360, 'httpOnly': False, 'name': '__bid_n', 'path': '/', 'secure': False, 'value': '1849531718ff5563184207'}, {'domain': '.17k.com', 'expiry': 1668959999, 'httpOnly': False, 'name': 'sajssdk_2015_cross_new_user', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.17k.com', 'expiry': 1700486360, 'httpOnly': False, 'name': 'Hm_lvt_9793f42b498361373512340937deb2a0', 'path': '/', 'secure': False, 'value': '1668950356'}, {'domain': '.www.17k.com', 'expiry': 1700486356, 'httpOnly': False, 'name': 'FPTOKEN', 'path': '/', 'secure': False, 'value': '30$jR9LESKeuJUP4A1NomR5Lzj0lTv6IozxaeH4PeXTAP3Jn6I/dxw5u9HBxRZIHHdnqIhpoWlk8QIDbCc5zwx0JD8WDmu9zSgeglySxE6sLgNeXbp/Hcp6VPd89ZHfls+MBwPVMcN59whkwVWT9blsD4bFIOlE3xlTYSV5X4wdLaeHUkA7Aoe99aaDqW/Yw9fmWqvzLlP+g+innoEVSC9l+G3LibrYzcrOG9rYP8Hs6fXHPOv4ojLAhSRU1X2U39k5/ZwAyi0RqTqOzeSoX+I38GVyg+RxBeFJT0uJM1Esk5n+OlGCKHv3Z1DRdqoM5MbvA+Op9LnY5jRv7fiq8KWQbwBCFIH0pAINt443Do6ZOV34UVME1vp5dKNKqlTOgol8|P3MHkGS0alVOgOKsTYR2wjOEjrTkBiL6QQjd9ZlQSgU=|10|51aa6242059861df48142792b91e55ff'}, {'domain': '.17k.com', 'expiry': 1703510360, 'httpOnly': False, 'name': 'sensorsdata2015jssdkcross', 'path': '/', 'secure': False, 'value': '%7B%22distinct_id%22%3A%2299398369%22%2C%22%24device_id%22%3A%2218495316f4e164-0dae601f7cb9c8-26021e51-921600-18495316f4f7d9%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22c292d259-010b-411e-b558-3caba99ec51a%22%7D'}, {'domain': '.17k.com', 'expiry': 1700486354, 'httpOnly': False, 'name': 'GUID', 'path': '/', 'secure': False, 'value': 'c292d259-010b-411e-b558-3caba99ec51a'}]
result = {}
for item in lst:
    # print(item)  # 一个item就是一个cookie信息
    # print(item['name'], item['value'])
    result[item['name']] = item['value']
# print(result)  # 字典


import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
resp = requests.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919", headers=headers, cookies=result)
print(resp.text)