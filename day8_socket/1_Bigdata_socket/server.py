#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import  socket,os
server = socket.socket()

host = "localhost"
port = 8888
server.bind( (host,port) )

server.listen()
print( "server wait for a connect...")

while True:
	conn,addr = server.accept()
	print("the connect is building...")

	while True:
		cmd = conn.recv( 1024)

		#检验
		if not cmd:
			print("client has lost...")
			break
		print("recv cmd:",cmd)

		res = os.popen( cmd.decode() ).read()

		res_byte_size = len( res.encode() )
		print("The size 0f res_byte_size:",res_byte_size,"          byte类型下，一个中文字符相当于2个单位" )
		print("The size Of res_data_size:",len(res),"          字符串下的len()，一个中文字符相当于1个单位")

		conn.send( str( res_byte_size ).encode() )
		conn.send( res.encode("utf-8") )
		print("the data was send for client...")

		print("the connect also building,and server wait for a now cmd...")

server.close()
