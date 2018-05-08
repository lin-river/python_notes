#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import multiprocessing
# 使用方法基本和多线程一样
import threading,time

def thread_run( pro,thr):
	print( "进程 -%s 线程 - %s 线程编号：%s" % ( pro,thr,threading.get_ident() ) )

def run(name):
	"""
	多进程多线程模式
	:param name:
	:return:
	"""
	time.sleep(2)
	print('hello', name)
	for i in range(3):
		t = threading.Thread( target= thread_run, args=(name,i) )
		t.start()

if __name__ == '__main__':
	p_objs = []
	for i in range(10):
		p = multiprocessing.Process( target=run, args=('bob-%s' % i,) )
		p.start()
		p_objs.append(p)

	for p in p_objs:
		p.join()

	print( "进程都执行完毕")

