#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import socket
client = socket.socket()

host = "localhost"
port = 8888
client.connect( (host,port) )

while True:
	cmd = input(">>:").strip()

	#检验
	if 0 == len( cmd ):
		continue

	client.send( cmd.encode() )

	cmd_res_size = client.recv(1024)				#接受命令结果的大小
	print( "命令结果大小为：",cmd_res_size )

	client.send( "准备好了，client可以发送了！".encode("utf-8") )

	received_size = 0
	received_data = b""
	while int( cmd_res_size ) > received_size:
		data = client.recv(1024)
		received_size += len(data)
		received_data += data
	else:
		print("The data receive done,and the data size is {0} KB...".format(received_size))
		print( received_data.decode() )

client.close()