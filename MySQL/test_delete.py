# -*- coding: UTF-8 -*-
# !/usr/bin/python

import MySQLdb

'''
删除数据
'''
# 打开数据库连接
db = MySQLdb.connect(host="117.28.237.21", user="root", passwd="root", db="test", port=29960)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 删除语句
sql = "DELETE FROM EMPLOYEE WHERE SEX = 'M'"

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