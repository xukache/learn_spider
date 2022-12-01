#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/28 20:26
#@Author: 徐 凯
#@File: 01_mongodb的基本使用.py.py
#@IDE: PyCharm
'''
import pymongo


# 1. 连接
conn = pymongo.MongoClient(host="localhost", port=27017)
# 2. 选择数据库
db = conn['python_1']  # use python_1
# 3. 开始操作
# db.stu.insert_one({"name":"kachex"})
# pymongo     <=>   mongodb
# insert_one  <=>   insertOne
# 下划线命名   <=>   驼峰命名

# db.stu.insert_many([{"name":"sylar"}, {"name":"tory"}])

# 查询
result = db.stu.find({}, {"_id":0, "name":1})
# print(dir(result))
for item in result:
    print(item)