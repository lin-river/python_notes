#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import socket,os
server = socket.socket()

server.bind( ("localhost",8888) )

server.listen()
print( "server wait for a connect...")

while True:
	conn,addr = server.accept()
	print("the connect is building...")

	while True:
		data = conn.recv(1024)

		#检验
		print("recv:", data)
		if not data:
			print("client has lost...")
			break

		res = os.popen(data.decode("utf-8") ).read()

		# 检验
		if len( res ) == 0:
			conn.send(b"The server_cmd has no return")		#python3.0里面必须发送一个byte
			continue

		# 为了解决缓冲区问题，要先计算返回数据的大小，然后发给客户端
		#len(res) 和 len( res.encode() )的长度可能是不一样的(中文情况)：
		print(len(res))											# 计算的事字符的长度（中文占1）
		print( len( res.encode() ) )							# 计算的是字节的长度（中文占2）

		conn.send( str( len(res) ).encode("utf-8"))				#整数是不能直接encode的

		conn.send( res.encode("utf-8") )
		print("the data was send for client...")

		print("the connect also building,and server wait for a now cmd...")

server.close(s)