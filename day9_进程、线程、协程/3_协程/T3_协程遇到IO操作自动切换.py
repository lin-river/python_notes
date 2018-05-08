#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import gevent
# Gevent 是一个第三方库，可以轻松通过gevent实现并发同步或异步编程，在gevent中用到的主要模式是Greenlet, 它是以C扩展模块形式接入Python的轻量级协程。
# Greenlet全部运行在主程序操作系统进程的内部，但它们被协作式地调度。

def func1():
	print('\033[31;1mrunning in func1...\033[0m')
	gevent.sleep(2)
	print('\033[31;1mrunning in func1 again...\033[0m')


def func2():
	print('\033[32;1mrunning in func2...\033[0m')
	gevent.sleep(1)
	print('\033[32;1mrunning in func2 again...\033[0m')

def func3():
	print( "running func3")
	gevent.sleep(0)
	print( "RUNNING func3 again")

gevent.joinall([
	gevent.spawn(func1),
	gevent.spawn(func2),
	gevent.spawn(func3),
])

# 结果：
# running in func1...
# running in func2...
# running func3
# RUNNING func3 again
# running in func2 again...
# running in func1 again...

# 执行过程：
# 先执行的func1，打印"running in func1...",遇到gevent.sleep(2),切换至下一个函数
# 执行func2，打印"running in func2...",遇到gevent.sleep(1),切换至下一个函数
# 执行func3，打印"running func3",遇到gevent.sleep(0),切换至下一个函数
# 执行func1，gevent.sleep(2)，时间未到，函数还在卡着，切换至下一个函数
# 执行func2，gevent.sleep(1)，时间未到，函数还在卡着，切换至下一个函数
# 执行func3，遇到gevent.sleep(0),打印"RUNNING func3 again",函数执行完毕,切换至下一个函数
# 执行func1，gevent.sleep(2)，时间未到，函数还在卡着，切换至下一个函数
# 执行func2，gevent.sleep(1)，时间到，打印"running in func2 again..."，函数执行完毕,切换至下一个函数
# 执行func1，gevent.sleep(2)，时间到，打印"running in func1 again..."，函数执行完毕,切换至下一个函数