#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import socket

HOST = 'localhost'  			# The remote host
PORT = 8001  					# The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
	msg = bytes(input(">>:"), encoding="utf8")
	s.sendall(msg)
	data = s.recv(1024)
	# print(data)

	print('Received', repr(data))			# repr() 格式化输出
s.close()