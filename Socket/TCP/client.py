#!/usr/bin/env python
# -*- coding:utf-8 -*-
#客户端

import socket # socket模块

BUF_SIZE = 1024  #设置缓冲区的大小
server_addr = ('127.0.0.1', 8888)  #IP和端口构成表示地址
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #返回新的socket对象
client.connect(server_addr)  #要连接的服务器地址
while True:
    data = raw_input("Please input some string > ")
    client.sendall(data)  #发送数据到服务器
    # data = client.recv(BUF_SIZE)  #从服务器端接收数据
    # print data
client.close()