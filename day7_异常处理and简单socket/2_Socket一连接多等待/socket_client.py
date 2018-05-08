#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import socket

client = socket.socket()
client.connect( ("localhost",6969))

while True:
	msg = input(">>:").strip()
	if len( msg ) == 0:			#解决了send为空卡死的情况
		continue
	client.send( msg.encode(encoding= "utf-8"))
	data = client.recv(1024)
	print( "recv:",data.decode() )

client.close()