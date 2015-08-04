#!/usr/bin/env python
# -*- coding:utf-8 -*-
#服务器端

import socket   # socket模块
import commands # 执行系统命令模块
import sys
import MySQLdb
from datetime import datetime

BUF_SIZE = 1024  #设置缓冲区大小
server_addr = ('0.0.0.0', 8800)  #IP和端口构成表示地址
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #生成一个新的socket对象
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  #设置地址复用
server.bind(server_addr)  #绑定地址
server.listen(5)  #监听, 最大监听数为5

db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="", db="gps_development", port=3306) # 打开数据库连接
cursor = db.cursor() # 使用cursor()方法获取操作游标
while True:
    client, client_addr = server.accept()  #接收TCP连接, 并返回新的套接字和地址
    print 'Connected by', client_addr
    while True :
        data = client.recv(BUF_SIZE)  #接收头包
        f=open('data.txt','a+')  #打开日志文件
        if data.find('hder', 0, 4) <> -1:
            print '收到头包', data
            print >> f, '收到头包', data
            if data.find('1', 4, 5) <> -1:  #设备后续会发送通信请求包
                print '设备后续会发送通信请求包'
                print >> f, '设备后续会发送通信请求包'
                print '发送响应包 hder5'
                print >> f, '发送响应包 hder5'
                client.sendall('hder5')  #发送响应包
                data = client.recv(BUF_SIZE)  #接收通信请求包
                if data.find('1', 0, 1) <> -1:  #用户登录
                    print '用户', data[1:17].replace('\0', ''), '登录成功'
                    print >> f, '用户', data[1:17].replace('\0', ''), '登录成功'
                    print '发送响应包 hder5'
                    print >> f, '发送响应包 hder5'
                    client.sendall('hder5')  #发送响应包
                elif data.find('2', 0, 1) <> -1:  #用户退出
                    print data[1:17].replace('\0', ''), '退出成功'
                    print >> f, data[1:17].replace('\0', ''), '退出成功'
                    exit(db,f,server) # 退出
            elif data.find('2', 4, 5) <> -1:  #设备后续会发送握手包
                print '设备后续会发送握手包'
                print >> f, '设备后续会发送握手包'
                data = client.recv(BUF_SIZE)  #接收通信请求包
                print '用户:', data[0:16].replace('\0', ''), '的握手包'
                print >> f, '用户:', data[0:16].replace('\0', ''), '的握手包'
                if data.find('hder3', 16, 21) <> -1:  #设备后续会发送设备数据包
                    print '设备后续会发送设备数据包'
                    print >> f, '设备后续会发送设备数据包'
                    print '########################'
                    print '用户:', data[72:88].replace('\0', '')
                    print '东经:', float(data[26:29])+float(data[29:38])/60 #东经  
                    print '北纬:', float(data[40:42])+float(data[42:51])/60 #北纬
                    print 'LAC:', data[54:60] #LAC
                    print 'CELL:', data[60:66] #CELL
                    print '########################'
                    print >> f, '########################'
                    print >> f, '用户:', data[72:88].replace('\0', '')
                    print >> f, '东经:', float(data[26:29])+float(data[29:38])/60  #东经  
                    print >> f, '北纬:', float(data[40:42])+float(data[42:51])/60  #北纬
                    print >> f, 'LAC:', data[54:58] #LAC
                    print >> f, 'CELL:', data[60:64] #CELL
                    print >> f, '########################'
                    # SQL 插入语句
                    sql = "INSERT INTO locations(`user_id`, `name`, `lng`, `lat`, `lac`, `cell`, `created_at`, `updated_at`) VALUES ('%d', '%s', '%.11f', '%.11f', '%s', '%s', '%s', '%s')" % \
                           (1, data[72:88].replace('\0', ''), float(data[26:29])+float(data[29:38])/60, float(data[40:42])+float(data[42:51])/60, data[54:58], data[60:64], datetime.now().strftime("%Y-%m-%d %H:%M:%S"), datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    print sql
                    try:
                       # 执行sql语句
                       cursor.execute(sql)
                       # 提交到数据库执行
                       db.commit()
                    except:
                       # Rollback in case there is any error
                       db.rollback()
                print '发送响应包 hder5'
                print >> f, '发送响应包 hder5'
                client.sendall('hder5')  #发送响应包
            elif data.find('3', 4, 5) <> -1:  #设备后续会发送设备数据包
                print '设备后续会发送设备数据包'
                print >> f, '设备后续会发送设备数据包'
                print '########################'
                print '用户:', data[72:88].replace('\0', '')
                print '东经:', data[26:38] #东经
                print '北纬:', data[40:51] #北纬
                print 'LAC:', data[54:60] #LAC
                print 'CELL:', data[60:66] #CELL
                print '########################'
                print >> f, '########################'
                print >> f, '用户:', data[72:88].replace('\0', '')
                print >> f, '东经:', data[26:38] #东经
                print >> f, '北纬:', data[40:51] #北纬
                print >> f, 'LAC:', data[54:58] #LAC
                print >> f, 'CELL:', data[60:64] #CELL
                print >> f, '########################'
                print '发送响应包 hder5'
                print >> f, '发送响应包 hder5'
                client.sendall('hder5')  #发送响应包
            else:
                print '不能识别此数据', data
                print >> f, '不能识别此数据', data
                exit(db,f,server) # 退出
        elif len(data) > 0:
            print '不能识别此数据', data
            print >> f, '不能识别此数据', data
            exit(db,f,server) # 退出
        else:
            print '错误数据'
            print >> f, '错误数据'
            exit(db,f,server) # 退出
        f.close() #关闭日志文件

db.close() # 关闭数据库连接
server.close() #关闭套接字流
sys.exit(0) #退出程序

def exit(db,f,server):
    db.close() # 关闭数据库连接
    f.close() #关闭日志文件
    server.close() #关闭套接字流
    sys.exit(0) #退出程序