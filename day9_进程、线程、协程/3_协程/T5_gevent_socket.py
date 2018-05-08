#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import sys
import socket
import time
import gevent

from gevent import socket, monkey

monkey.patch_all()


def server(port):
	s = socket.socket()
	s.bind(('0.0.0.0', port))
	s.listen(500)
	while True:
		cli, addr = s.accept()					# 走到accept()就会创建一个线程
		gevent.spawn( handle_request, cli)		# 但是在这里就交给协程了


def handle_request(conn):
	try:
		while True:
			data = conn.recv(1024)
			print("recv:", data)
			conn.send(data)
			if not data:
				conn.shutdown(socket.SHUT_WR)	# 关闭客户端

	except Exception as  ex:
		print(ex)
	finally:
		conn.close()


if __name__ == '__main__':
	server(8001)

# 比python自带的还要高效
# 一遇到io阻塞就切换