# -*- coding: UTF-8 -*-
# !/usr/bin/python

import MySQLdb

'''
创建数据表
'''
# 打开数据库连接
db = MySQLdb.connect(host="117.28.237.21", user="root", passwd="root", db="test", port=29960)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 创建数据表SQL语句
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

# 关闭数据库连接
db.close()