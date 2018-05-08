#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import  socket,os,hashlib
server = socket.socket()

host = "localhost"
port = 8888
server.bind( (host,port) )

server.listen()
print( "server wait for a connect...")

while True:
	conn,addr = server.accept()
	print("the connect is building...")

	while True:
		data = conn.recv( 1024)

		#检验
		if not data:
			print("client has lost...")
			break

		cmd,filename = data.decode().split()
		print( filename )

		if os.path.isfile( filename ):
			md5 = hashlib.md5()
			file_size = os.stat( filename ).st_size
			conn.send(str(file_size).encode() )

			fflush = conn.recv( 1024)		# 刷新缓冲区
			print( fflush.decode() )
			with open(filename,"rb") as f:
				for line in f:
					md5.update( line )
					conn.send( line )
				print( "file md5 ",md5.hexdigest() )
		conn.recv(1024)
		conn.send( md5.hexdigest().encode() )


server.close()
