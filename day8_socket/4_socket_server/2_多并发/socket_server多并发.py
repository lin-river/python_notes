#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
	"""
    每一个请求过来都会实例化这个对象
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

# #python2.X里的写法
# 	def handle(self):
# 		while True:						# 如果没写这个，handle只接受一次处理
# 			# self.request is the TCP socket connected to the client
# 			# 在父类里默认是空的
# 			self.data = self.request.recv(1024).strip()
#
# 			print("{} wrote:".format(self.client_address[0]))  # 打印客户端的IP地址
# 			print(self.data)
#
# 			if not self.data:				# 代表客户端断了
# 				print( self.client_address[0] ,"断开了...")
# 				break
# 			# just send back the same data, but upper-cased
# 			self.request.send(self.data.upper())

# python3 中用这个：直接抓异常
	def handle(self):
		while True:
			try:
				self.data = self.request.recv(1024).strip()
				print("{} wrote:".format(self.client_address[0]))
				print( self.data )

				self.request.send(self.data.upper() )
			except ConnectionResetError as e:
				print("error:", e)
				break

if __name__ == "__main__":
	HOST, PORT = "localhost", 9999

	# Create the server, binding to localhost on port 9999
	# 第三步：实例化
	server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
	# 多线程：每来一个请求，服务器就会新开一个线程

	# server = socketserver.ForkingTCPServer((HOST, PORT), MyTCPHandler)			# 一般不用，因为太耗资源了
	# 多进程 ：每进来一个链接，就会启动一个进程（windows的进程管理和linux的进程管理不太一样，所以执行会报错）
	# AttributeError: module 'socketserver' has no attribute 'ForkingTCPServer'
	# 在linux上百分百好使！

	# Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
	server.serve_forever()