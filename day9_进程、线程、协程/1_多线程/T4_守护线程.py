#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

# 原本：
#     一个进程可以有多个子进程，他们是互相独立的，主进程挂掉后，子进程照样运行
#     主线程执行完毕后，依然会等待子进程执行完毕后才结束程序
#
# 守护进程：
#     守护进程依赖于主进程，主进程挂掉之后，守护进程也跟着挂掉了
#     主进程程执行完毕后，直接关闭程序，不等待其他守护进程的结果( 但是会等待非守护进程的结果 )

import threading,time

class MyThread(threading.Thread):

	def __init__(self,n):
		super(MyThread,self).__init__()
		self.n = n

	def run(self):
		time.sleep(2)
		print( "runnint task ",self.n )

t_objs = []
start_time = time.time()
for i in range(50):
	t = MyThread("T-%s" % i)
	t.setDaemon(True)						# 把当前线程设置为守护线程，必须在t.start()之前设置，否则会报错
	t.start()
	t_objs.append(t)


print( "cost time:" ,time.time() - start_time )