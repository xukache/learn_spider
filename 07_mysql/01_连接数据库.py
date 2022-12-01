#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#@Time: 2022/11/21 13:55
#@Author: 徐 凯
#@File: 01_连接数据库.py
#@IDE: PyCharm
'''
import pymysql

# 1. 创建连接
# 默认是开启了事务的
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='pachong'  # 连接的数据库
)
print("创建好了连接!")
# 2. 创建cursor, 游标 -> 执行sql语句,以及获取sql执行结果
cur = conn.cursor()
# 3. 准备好sql语句
sql = "insert into men(name, age, address) values ('燕归来', 18, '八宝山')"
# 4. 执行这个sql语句
cur.execute(sql)
print("执行完毕!")
# 5. 提交事务
conn.commit()  # try的最后
# conn.rollback()  # except

cur.close()  # 断开cursor
conn.close()  # 断开连接
"""
事务: 一件事儿
  一件事, 可能牵动很多条数据一起跟着变动
  此时, 如果所有的操作都没有问题, 可以把数据写入数据库
  如果, 其中的任意一步操作有问题的话, 此时如果还要硬向数据库写入 -> 数据就废了

  开启事务
  try
  联通 = 注销手机号
  查询手机余额 财务  -> 手机号数据 = 成功了
  套餐  -> 手机号的数据 => 失败了
  套餐使用情况
  流量使用情况  -> 手机号的数据
  能够正常使用流量的表  -> 你的手机号删掉或者标记一下(修改)
  提交事务(写入磁盘)
  except
      回滚(回归到原来的状态, 刚才的操作, 不写入磁盘)
"""
