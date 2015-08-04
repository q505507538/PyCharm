# -*- coding: UTF-8 -*-
# !/usr/bin/python

import MySQLdb

'''
查询数据
'''
# 打开数据库连接
db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="", db="gps_development", port=3306)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 更新语句
sql = "UPDATE locations SET name = 'wxd_01' WHERE id = 1"

try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭数据库连接
db.close()