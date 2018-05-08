#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

#_*_coding:utf-8_*_
__author__ = 'Alex Li'


import socket
import sys

messages = [ b'This is the message. ',
             b'It will be sent ',
             b'in parts.',
             ]
server_address = ('192.168.221.130', 8000)

# Create a TCP/IP socket
socks = [ socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(10000) ]
# socks = [ socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(600) ]
# window下1000不行，太多了会报错：ValueError: too many file descriptors in select()
# 放到linux上就可以了，但是需要改参数，应为：Linux对于每个用户，系统限制其最大进程数。( 默认1024 )
# 修改 ulimit -SHn 65535
# 但多了还是会有问题：
# OSError: [WinError 10055] 由于系统缓冲区空间不足或队列已满，不能执行套接字上的操作。( 20000个连接时挂了)

# Connect the socket to the port where the server is listening
print('connecting to %s port %s' % server_address)

for s in socks:
    s.connect(server_address)

for message in messages:
    # Send messages on both sockets
    for s in socks:
        print('%s: sending "%s"' % (s.getsockname(), message) )
        s.send(message)

    # Read responses on both sockets
    for s in socks:
        data = s.recv(1024)
        print( '%s: received "%s"' % (s.getsockname(), data) )
        if not data:
            print(sys.stderr, 'closing socket', s.getsockname() )
