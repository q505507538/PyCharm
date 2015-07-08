#!/usr/bin/env python
# -*- coding:utf-8 -*-
#客户端

import socket
import struct

BUF_SIZE = 1024  #设置缓冲区
server_addr = ('127.0.0.1', 8888)  #IP和端口构成表示地址
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #生成新的套接字对象

while True :
    data = raw_input('Please Input data > ')
    client.sendto(data, server_addr)  #向服务器发送数据
    data, addr = client.recvfrom(BUF_SIZE)  #从服务器接收数据
    print "Data : ", data
client.close()