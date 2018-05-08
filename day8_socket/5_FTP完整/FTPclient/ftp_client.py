#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import socket,hashlib,os
import json
client = socket.socket()

class FtpClient(object):
	def __init__(self):
		self.client = socket.socket()

	def connect(self,ip,port):
		"""
		连接
		:return:
		"""
		self.client.connect( (ip,port) )


	def interactive(self):
		"""
		交互
		:return:
		"""
		# self.authenticate()	登陆验证方法
		while True:
			cmd = input(">>:").strip()
			if len( cmd ) == 0:continue

			cmd_str = cmd.split()[0]
			if hasattr(self,"cmd_%s" % cmd_str):
				func = getattr( self, "cmd_%s" % cmd_str )
				func(cmd)
			else:
				self.help()

	def cmd_put(self,*args):
		cmd_split = args[0].split()
		if len( cmd_split ) > 1:
			filename = cmd_split[1]
			if os.path.isfile( filename ):
				fileszie = os.stat(filename).st_size

				# mst_str = "%s|%s" % (filename,fileszie)			# 这样写并不是不行，但是从长远考虑最好写成jason格式
				msg_dic = {
					"action":"put",
					"filename":filename,
					"filesize":fileszie,
					"overridden":True,			# 遇到重名的是否覆盖
				}
				self.client.send( json.dumps( msg_dic ).encode("utf-8") )

				# 防止粘包，等待服务器确认
				# 另外，这里应该接受客户端的状态，以确保接下来进行的操作是否进行
				server_response = self.client.recv(1024)

				with open( filename,"rb") as f:
					for line in f:
						self.client.send( line )
					else:
						print( "file upload success...")

			else:
				print( filename,"is not exist!")

	def cmd_get(self):
		pass

	def help(self):
		"""
		打印帮助信息
		:return:
		"""
		msg = '''
		ls				:
		pwd				:
		cd ..			:
		get filename	:
		put filename	:
		'''
		print( msg )

ftp = FtpClient()
ftp.connect( "localhost",9999 )
ftp.interactive()