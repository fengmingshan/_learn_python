# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 21:32:55 2018

@author: Administrator
"""

import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))     # 绑定端口
print('Bind UDP on 9999...')
while True:
    data, addr = s.recvfrom(1024)     # 接收数据:
    print('Received from %s:%s.' % (data, addr))
    reply = 'Hello, %s!' % data.decode('utf-8')
    s.sendto(reply.encode('utf-8'), addr)