#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import socket

client = socket.socket()
host = "localhost"
port = 8000

client.connect( (host,port) )

while True:
	msg = bytes( input(">>:"), encoding="utf-8" )
	client.sendall(msg)
	data = client.recv(1024)
	print( data )