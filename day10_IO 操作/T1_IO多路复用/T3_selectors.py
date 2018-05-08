#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import selectors
import socket


# 默认用的epoll，如果找不到epoll( 例如window上没有)，就会使用select
sel = selectors.DefaultSelector()				# 生成selectors对象


def accept(sock, mask):
	conn, addr = sock.accept()  # Should be ready
	print('accepted', conn, 'from', addr)
	conn.setblocking(False)						# 把链接设为非阻塞模式
	sel.register(conn, selectors.EVENT_READ, read)		# 将socket实例扔到注册事件，read是回调函数


def read(conn, mask):
	data = conn.recv(1000)  # Should be ready
	if data:
		print('echoing', repr(data), 'to', conn)
		conn.send(data)  # Hope it won't block
	else:
		print('closing', conn)
		sel.unregister(conn)							# 取消注册
		conn.close()


sock = socket.socket()
sock.bind(('localhost', 8000))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)		# 把一个socket扔进注册事件，accept是回调函数

while True:
	events = sel.select()								# 虽然写的select()但是可能调用的是epoll。看系统调用的是什么，默认阻塞，有活动链接就返回活动的链接列表
	for key, mask in events:
		callback = key.data								# 这里相当于就是调用accept()
		callback(key.fileobj, mask)						# key.fileobj = 文件句柄