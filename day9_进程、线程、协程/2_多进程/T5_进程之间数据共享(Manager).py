#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

from multiprocessing import Process, Manager
import os
# 进程之间实现了数据共享(  实际上并不算真正的共享，还是将数据copy一份传给各个进程，最终给合在一块了 )

def f(d, l):
	d[ os.getpid()] = os.getpid()
	l.append( os.getpid() )
	print(l)


if __name__ == '__main__':
	with Manager() as manager:					# manager自己已经帮你加好锁类，所以不需要自己再去加锁
		d = manager.dict()						# 生成一个字典，可在多个进程间共享传递

		l = manager.list(range(5))				# 生成一个列表，可在多个进程间共享传递

		p_list = []
		for i in range(10):
			p = Process(target=f, args=(d, l))
			p.start()
			p_list.append(p)

		for res in p_list:						# 等待结果
			res.join()

		print(d)
		print(l)