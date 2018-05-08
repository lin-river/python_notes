#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import threading
import time

class MyThread(threading.Thread):

	def __init__(self,n):
		super(MyThread,self).__init__()
		self.n = n

	def run(self):
		time.sleep(2)
		print("task %s" % self.n,threading.current_thread() )
		# task t-0 <MyThread(Thread-1, started 9228)>

t_objs = []							# 用于存线程实例
start_time = time.time()
for i in range(50):
	"""
	启动了50个线程，实际上该程序有51个线程，因为包括主线程
	"""
	t = MyThread("t-%s" % i)
	t.start()
	t_objs.append(t)

print( "运行的线程个数：",threading.active_count() )

for t in t_objs:
	"""
	等待所有子线程执行完毕后主线程才继续往下走
	在此之前，主线程和子线程完全是并行关系，互相独立；加了join()之后，主线程依赖子线程执行完毕之后才往下走
	"""
	t.join()

print( "cost time:" ,time.time() - start_time,threading.current_thread() )
# cost time: 2.0089566707611084 <_MainThread(MainThread, started 13372)>
print( "运行的线程个数：",threading.active_count() )
