#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

# Events:事件
# An event is a simple synchronization object;
# 事件是一个简单的同步对象;
# the event represents an internal flag, and threads
# 该事件表示一个内部标志和线程
# can wait for the flag to be set, or set or clear the flag themselves.
# 可以等待标志被设置，或者自己设置或清除标志。
#
# event = threading.Event()
#
# # a client thread can wait for the flag to be set
# 客户端线程可以等待标志被设置
# event.wait()
#
# # a server thread can set or reset it
# 服务器线程可以设置或重置它
# event.set()
# event.clear()
#
# If the flag is set, the wait method doesn’t do anything.
# 如果该标志已设置，则等待方法不会执行任何操作。
# If the flag is cleared, wait will block until it becomes set again.
# 如果标志被清除，等待将被阻塞，直到它再次被设置。
# Any number of threads may wait for the same event.
# 任何数量的线程都可能等待相同的事件。

import threading,time

event = threading.Event()					# 实例化一个事件

def light():
	count = 0
	event.set()								# 先设为绿灯(设置一个标志，所有线程都能看到)
	while True:
		if count > 5 and count <10 :		# 改成红灯
			event.clear()					# 把标志位清了
			print( "\033[41;1m red light is on ...\033[0m")
		elif count > 10:					# 变绿灯
			event.set()
			count = 0
		else:
			print("\033[42;1m green light is on ...\033[0m")

		time.sleep(1)
		count+= 1

def car(name):
	while True:
		if event.is_set():						# 代表绿灯(查看evernt标志是否set )
			print( "[%s] running..." % name )
			time.sleep(1)
		else:
			print( "[%s] sees red light,waiting...." % name )
			event.wait()						# 挂起，等待到event的标志set后再进行
			print("[%s] sees green light,start going...." % name)

light = threading.Thread(target=light)
light.start()

car1 = threading.Thread( target= car,args=("Tesla",) )
car2 = threading.Thread( target= car,args=("BMW",) )
car1.start()
car2.start()