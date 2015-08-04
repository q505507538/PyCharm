# -*- coding: UTF-8 -*-
# !/usr/bin/python

import MySQLdb
from datetime import datetime
'''
插入数据1
'''
# 打开数据库连接
db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="", db="gps_development", port=3306)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = "INSERT INTO locations(`user_id`, `name`, `lng`, `lat`, `cell`, `lac`, `created_at`, `updated_at`) \
       VALUES ('%d', '%s', '%.11f', '%.11f', '%s', '%s', '%s', '%s')" % \
       (1, 'wxd_01', 118.09697266249, 24.62181344676, '5925', '0c51', datetime.now().strftime("%Y-%m-%d %H:%M:%S"), datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print sql
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# 关闭数据库连接
db.close()