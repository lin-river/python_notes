#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import socketserver
import json,os

class MyTCPHandler(socketserver.BaseRequestHandler):
	"""
    每一个请求过来都会实例化这个对象
    """
# python3 中用这个：直接抓异常
	def handle(self):
		while True:
			try:
				self.data = self.request.recv(1024).strip()
				print("{} wrote:".format(self.client_address[0]))
				print( self.data )
				cmd_dic = json.loads( self.data.decode() )
				action = cmd_dic["action"]

				# 判断存不存在
				if hasattr( self,action ):
					func = getattr(self,action )
					func( cmd_dic )

			except ConnectionResetError as e:
				print("error:", e)
				break

	def put(self,*args ):
		"""
		接受客户端文件
		:return:
		"""
		cmd_dic = args[0]
		filename = cmd_dic["filename"]
		filesize = cmd_dic["filesize"]
		if os.path.isfile( filename ):
			f = open( "new_"+filename,"wb")

		else:
			f = open( filename, "wb")
		self.request.send( b"200 OK" )

		received_size = 0
		while received_size < filesize:
			data = self.request.recv(1024)
			f.write( data )
			received_size += len( data )
		else:
			print( "file [%s] has uploaded..." % filename )



if __name__ == "__main__":
	HOST, PORT = "localhost", 9999
	# 第三步：实例化
	server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
	# 多线程：每来一个请求，服务器就会新开一个线程

	server.serve_forever()