# -*- coding: UTF-8 -*-
# !/usr/bin/python

import MySQLdb

'''
插入数据2
'''
# 打开数据库连接
db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="", db="gps_development", port=3306)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭数据库连接
db.close()