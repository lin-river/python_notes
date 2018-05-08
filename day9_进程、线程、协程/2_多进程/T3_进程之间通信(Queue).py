#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

# 不同进程间内存是不共享的，要想实现两个进程间的数据交换，可以用以下方法：
# Queues
# 使用方法跟threading里的queue差不多，只不过前者作用于多进程，后者作用于多线程
import multiprocessing

def func(q):
	q.put( [42,None,'hello'] )

# Queues 进程通信：
if __name__ == '__main__':
	q = multiprocessing.Queue()
	p = multiprocessing.Process( target= func, args=(q,) )			# 进程q传给子进程是可以的,是以copy的方式传过去的
	# 实际上是将q序列化给第三方,第三方再反序列化给子进程(因为两个进程之间的内存也是没办法直接访问的)
	p.start()

	print( q.get() )
	p.join()

# queue 进程间无法通信
# import queue
# def f2(q2):
# 	"""子进程"""
# 	q2.put( [42,None,'hello'] )
#
# def f():
# 	"""子进程"""
# 	q.put( [42,None,'hello'] )
#
# if __name__ == '__main__':			# 主进程
# 	q = queue.Queue()
# 	# first:
# 	# p = multiprocessing.Process( target= f, )				# 因为是两个进程，q并不相同
# 	# 报错：NameError: name 'q' is not defined，不同进程的线程无法通信
#
# 	# second:
# 	p = multiprocessing.Process( target= f2, args= (q,) )		# 将一个线程q传给一个子进程是不可以的
# 	# TypeError: can't pickle _thread.lock objects
#
# 	p.start()
# 	print( q.get() )
# 	p.join()
