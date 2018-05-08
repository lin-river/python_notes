#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import socket
client = socket.socket()

client.connect( ("localhost",8888) )

while True:
	cmd = input(">>:").strip()

	if len(cmd) == 0:
		continue

	client.send( cmd.encode("utf-8") )

	cmd_res_size = client.recv(1024)				#接受命令结果的大小
	print( "命令结果大小为：",cmd_res_size )

	received_size = 0
	received_data = b""
	# while received_size != int( data_size.decode() ):		#只要判断点和服务器数据大小不一样，则继续循环,但是这样会报错
	while int(cmd_res_size) > received_size:
		data = client.recv(1024)
		received_size += len(data)					#每次收到的不一定是1024，所以必须要用len()去判断 ,因为中文的原因
		received_data += data
		print( received_size )
	else:
		print("The data receive done,and the data size is {0} KB...".format(received_size))
		print( received_data.decode() )
client.close()
