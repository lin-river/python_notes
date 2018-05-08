#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import greenlet
# 第三方库
# greelet指的是使用一个任务调度器和一些生成器或者协程实现协作式用户空间多线程的一种伪并发机制，即所谓的微线程。
# greelet机制的主要思想是：
# 	生成器函数或者协程函数中的yield语句挂起函数的执行，直到稍后使用next()或send()操作进行恢复为止。可以使用一个调度器循环在一组生成器函数之间协作多个任务。

from greenlet import greenlet
import time

def t1():
	print(12)						# 2
	gr2.switch()					# 3
	print(34)						# 6
	gr2.switch()					# 7


def t2():
	print(56)						# 4
	gr1.switch()					# 5
	print(78)						# 8


gr1 = greenlet(t1)					# 启动一个协程
gr2 = greenlet(t2)
gr1.switch()						# 手动切换 1