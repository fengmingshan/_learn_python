# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 21:17:47 2018

@author: Administrator
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 实例化端口
s.connect(('127.0.0.1', 9999)) # 链接服务器端口

print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:     # 发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()