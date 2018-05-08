#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import threading
import time

def running(n):
	print("task : ",n)
	time.sleep(1)			# sleep.() 是不占用CPU的，相当于CPU就把这个线程挂起了，去干别的事情了

print( "t1.t2同时跑")
t1 = threading.Thread( target=running , args= ("t1",) )
t2 = threading.Thread( target=running , args= ("t2",) )
t1.start()
t2.start()
# 默认情况下主线程是不会等待子线程运行结束的，但是可以用t.join()强制等待子线程运行结束才继续执行主线程

print( "t3,t4一个一个跑")
running( "t3")
running( "t4")