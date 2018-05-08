#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = Hero lws
import socket
#建立连接
server = socket.socket()

# 监听端口
server.bind( ("localhost",8080) )		#绑定要监听的端口
server.listen()			#监听
print( "I will need to wait...")

#等待连接
# server.accept()		#直接这样会报错
conn,addr = server.accept()		#accept 返回两个值：连接的标志(实例)，链接的地址（字符串）

#阻塞，其他client无法访问
print("conn = ",conn)
print("addr = ",addr)
print( "the data is here...")

#接受数据
# data = server.recv(1024)		#不能直接用server，否则会出现相当于占线的情况
data = conn.recv(1024)		#官方建议不要超过8192（8K）
#recv默认是阻塞的，即如果没有返回数据，recv就一直在数据
print("recive data:",data)

#发送数据
conn.send( data.upper() )		#将接受的数据变成大写返回，最大就只能发送32768,（32K），不同服务器不一样
# conn.sendall( data.upper() )  #循环send()，直到把数据都发过去
#关闭连接
server.close()