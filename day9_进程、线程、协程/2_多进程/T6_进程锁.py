#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

# 进程同步：
# Without using the lock output from the different processes is liable to get all mixed up.
# 如果不使用来自不同流程的锁定输出，则容易混淆。

from multiprocessing import Process, Lock


def f(l, i):
	l.acquire()
	try:
		print('hello world', i)
	finally:
		l.release()


if __name__ == '__main__':
	lock = Lock()					# 进程锁
	# 进程锁存在的意义：
	# 	解决屏幕共享问题，防止一个子进程还没打印完，另一个子进程插进来打印  helhello world 1lo world 2
	# python2.X上会出现这个问题，python3.x上不会了


	for num in range(10):
		Process(target=f, args=(lock, num)).start()