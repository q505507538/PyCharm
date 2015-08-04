# -*- coding: UTF-8 -*-
# !/usr/bin/python

import MySQLdb

'''
测试数据库
'''
# 打开数据库连接
db = MySQLdb.connect(host="117.28.237.21", user="root", passwd="root", db="test", port=29960)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据库。
data = cursor.fetchone()

print "Database version : %s " % data

# 关闭数据库连接
db.close()
