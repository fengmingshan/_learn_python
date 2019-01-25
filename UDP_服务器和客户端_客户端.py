# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 21:32:55 2018

@author: Administrator
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    s.sendto(data, ('127.0.0.1', 9999))     # 发送数据:
    print(s.recv(1024).decode('utf-8'))     # 接收数据:
s.close()
