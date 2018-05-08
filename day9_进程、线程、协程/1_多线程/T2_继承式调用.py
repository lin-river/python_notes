#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import threading
import time

class MyThread(threading.Thread):

	def __init__(self,n):
		super(MyThread, self).__init__()				# 重构__init__()时也要把原来的__init__()继承过来
		self.n = n


	def run(self):										# 覆盖重写的，所以run名字不能改
		time.sleep(2)
		print( "runnint task ",self.n )


start_time = time.time()
for i in range(50):
	t = MyThread("t-%s" % i )
	t.start()

print( "cost time:" ,time.time() - start_time )
# cost time: 0.015632152557373047
#结果很明显没有等到线程执行完time.sleep()就结束计时了
# 并行就是这样子的，这里计算的是主线程(就是程序本身)的的运行时间，t.start()创建的线程独立运行
# 默认情况下主线程是不会等待子线程运行结束的，但是可以用t.join()强制等待子线程运行结束才继续执行主线程
# 主线程执行完毕后依然会等待子进程执行完毕后才结束程序