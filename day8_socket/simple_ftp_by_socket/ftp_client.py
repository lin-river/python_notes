#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import socket,hashlib
client = socket.socket()

host = "localhost"
port = 8888
client.connect( (host,port) )

while True:
	cmd = input(">>:").strip()

	#检验
	if 0 == len( cmd ):continue
	if cmd.startswith("get"):
		client.send( cmd.encode() )

	file_size = client.recv(1024)				#接受文件大小
	print( "文件大小为：",file_size )
	client.send( b"ready to recv file")
	file_total_size = int( file_size.decode() )

	received_size = 0
	filename = cmd.split()[1]
	md5 = hashlib.md5()
	with open(filename+".NEW","wb") as f:
		while received_size < file_total_size:
			data = client.recv(1024)
			md5.update(data)
			received_size += len( data )
			f.write( data )
			# print( file_total_size,received_size )
		else:
			new_file_md5 = md5.hexdigest()
			print( "file recv done...",received_size,new_file_md5 )

	client.send( b"ready to recv md5")
	server_file_md5 = client.recv(1024)
	print( "server file md5:",server_file_md5)
	print( "client file md5:",new_file_md5 )


client.close()