#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = Hero lws
import socket
#socket.socket(Socket Families(地址簇),Socket Types,...)
# Socket Families(地址簇)
# socket.AF_UNIX unix  本机进程间通信
# socket.AF_INET　IPV4　
# socket.AF_INET6  IPV6

# Socket Types
# socket.SOCK_STREAM  #for tcp
# socket.SOCK_DGRAM   #for udp
# socket.SOCK_RAW     #原始套接字，普通的套接字无法处理ICMP、IGMP等网络报文，而SOCK_RAW可以；
			#其次，SOCK_RAW也可以处理特殊的IPv4报文；此外，利用原始套接字，可以通过IP_HDRINCL套接字选项由用户构造IP头。
# socket.SOCK_RDM  #是一种可靠的UDP形式，即保证交付数据报但不保证顺序。SOCK_RAM用来提供对原始协议的低级访问，
			#在需要执行某些特殊操作时使用，如发送ICMP报文。SOCK_RAM通常仅限于高级用户或管理员运行的程序使用。
# socket.SOCK_SEQPACKET #废弃了

client = socket.socket()		#声明地址簇和协议类型（默认IPv4和TCP）,同时生成socket连接对象
client.connect( ("localhost",9999) )				#连接

while True:
	# 发送数据
	# client.send( "Hello World!")		#python3会报错 ： TypeError: a bytes-like object is required, not 'str'
	# python2可以发字符串等，但python3只能发送byte类型
	str = input("请输入一个数据：")
	client.send(str.encode(encoding="utf-8"))  # 不能send空，会卡死
	# 接受数据
	data = client.recv(1024)  # 收多少数据，1024代表1024个字节=1KB
	print("recive data : ", data.decode() )

#关闭连接
client.close()
