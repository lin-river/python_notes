#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

# 单线程下的多路复用，不需要threading

import select
import socket
import queue

server = socket.socket()
host = "localhost"
port = 8000
server.bind( (host,port) )
server.listen( 1000 )

# 在接收客户端之前先要把服务端设置成非诸塞模式,
# 但是非诸塞模式下的accept()会报错，因为没有连接进来，recv()也会报错，因为没有数据传进来
# server.setblocking( False )					# recv()不阻塞，accept()也不阻塞，这时候accept()没有链接就会报错
# server.accept()								# BlockingIOError: [WinError 10035] 无法立即完成一个非阻止性套接字操作。

# 所以我们一开始就不应该让accept()执行，先让select去监听
server.setblocking( False )
# inputs = []										# 内核要检测的列表
# 但是检测列表为空会报以下错：OSError: [WinError 10022] 提供了一个无效的参数。
# 解决方法：    			刚开始没有链接进来那么server就是个链接
# 现在没有client链接但是server也是个socket，所有的client都要从server进来，在没有其他链接的时候server也是个链接，server就交给内核去检测，如果返回活动了就代表有链接进来
inputs = [server]
outputs = []
msg_dic = dict()

while True:
	readable,writeable,exceptional = select.select( inputs,outputs,inputs )
	# select.select(rlist,wlist,xlist,timeout)
	# rlist		: 要检测的列表
	# wlist		: 放什么下一次就直接出来什么，并不检测
	# xlist		: 异常的连接，(实际上存放的还是rlist，因为xlist检测的是异常连接，所以它需要一个检测列表 )
	# 返回三个数据：
	# readable 		: 列表，可活动的，可以读数据的链接( 但是select在底层已经帮我们做了封装，虽然有很多活动的链接，但是他只提供一个 )
	# writeable 	:
	# exceptional	: 列表，交给xlist检测的链接如果出异常了就会把异常连接放在这

	print( readable,writeable,exceptional )
	# [<socket.socket fd=424, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8000)>] [] []
	# fd		: 文件句柄

	# conn,addr = server.accept()
	# print( conn )
	# print("接受的数据为：",conn.recv(1024) )			# 非诸塞下没有数据传进来，recv()马上接受，于是就报错了
	# 报错：BlockingIOError: [WinError 10035] 无法立即完成一个非阻止性套接字操作。
	# 所以要想实现这个客户端发来数据时server端能知道，就需要让select在监测这个conn

	for r in readable:
		if r is server:						# 代表来了一个新链接，防止返回[server，conn]时不知道是新链接还是数据
			conn, addr = server.accept()
			print("新链接：",conn)
			inputs.append( conn )			# 让select在监测这个conn是否活动
			msg_dic[conn] = queue.Queue()	# 初始化一个队列，后面存要返回给client的数据
		else:
			data = r.recv(1024)				# 这里不能用conn去收，因如果多个链接的话，conn不知道是哪个，会出错，所以要改成r
			print( data )
			msg_dic[r].put( data )
			outputs.append(r)

	for w in writeable:						# 要返回给客户端的连接列表
		data_to_client = msg_dic[w].get()
		w.send( data_to_client )			# 返回给客户端源数据

		outputs.remove( w )					# 确保下次循环的时候writeable不返回这个已经处理完的链接了

	for e in exceptional:
		if e in outputs:
			outputs.remove( e )
		inputs.remove( e )
		del msg_dic[e]