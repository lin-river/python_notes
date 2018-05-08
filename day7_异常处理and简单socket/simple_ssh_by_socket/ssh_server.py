#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import socket,os
server = socket.socket()

server.bind( ("localhost",9999) )
server.listen()
print( "server wait for a connect...")

while True:
	conn,addr = server.accept()
	print( "the connect is building...")
	while True:
		data = conn.recv(10240000)
		print( "recv:",data )
		if not data:
			print("client has lost...")
			break
		#下面代码是实现ssh的核心代码：
		res = os.popen( data.decode() ).read()					#os.popen接受的是字符串，返回的也是字符串
		if len( res ) == 0:
			conn.send(b"The server_cmd has no return")		#python3.0里面必须发送一个byte
			continue
		conn.send( res.encode(encoding = "utf-8") )

server.close()