#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import socket
count = 0
# server = socket.socket()
# server.bind( ("localhost",6969) )
# server.listen()
# 如果accept在循环内相当于接电话的同时又接了一个电话，占线
# while True:
# 	conn,addr = server.accept()
# 	print( "The data is here...")
# 	data = conn.recv(1024)
# 	print( "recv:",data.decode())
# server.close()

server = socket.socket()
server.bind( ("localhost",6969) )

server.listen()
while True:		#加这层循环后，一个客户端断开，服务器就又回到监听的阶段
					#但每一次只能一个客户端连接，client1连接client2就占线等待，直到client1断开，服务器才响应client2
	conn, addr = server.accept()
	print("The connect beginning...")

	while True:
		data = conn.recv(1024)
		print( "recv:",data.decode())
		conn.send( data.upper() )
		#在windows下，如果客户端断掉了，那么循环结束，服务器关闭
		# 在linux下，如果客户端断掉了，那么服务器不会关闭，进入死循环
		# count += 1			# 用于判断何时退出
		# if count > 10 : break
		if not data:			#linux下要加这一句，如果数据为空，跳出循环，避免了linux下死循环
			print( "client has lost...")
			break

server.close()