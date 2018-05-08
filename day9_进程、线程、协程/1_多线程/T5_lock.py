#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

# 全局设备锁下数据依旧可以出错，详情请见：https://images2015.cnblogs.com/blog/720333/201609/720333-20160909174150473-664853910.png
# 比如在python2.X上执行下列代码得到的就不一定是10000( 因为在2.x上设备锁的给予是有时限的，比如100条指令后自动挂起切换)
# import  threading
#
# def running():
# 	global num,buff
# 	if num > 0:
# 		for i in range(10000):
# 			buff += i
# 	num += 1
#
# buff,num = 0,0
#
# t_objs = []
# for i in range(10000):
# 	t = threading.Thread( target=running )
# 	t.start()
# 	t_objs.append(t)
#
# for t in t_objs:
# 	t.join()
#
# print(num)

# 因为GIL：同一时间只有一个线程在修改数据，但是·他把一个数据copy成两份了
# 再加一层用户程序锁，保证同一时间真真正正的只有一个线程修改数据

import  threading,time

def running():
	lock.acquire()					# 获取锁
	global num,buff
	if num > 0:
		for i in range(10000):
			buff += i
	num += 1
	time.sleep(1)					# 现在变成串行的了，所以一个程序执行完至少要10000秒
	lock.release()					# 释放锁


buff,num = 0,0
lock = threading.Lock()				# 实例化一个锁的实例，在3.x上加不加锁无所谓了
t_objs = []
for i in range(10000):
	t = threading.Thread( target=running )
	t.start()
	t_objs.append(t)

for t in t_objs:
	t.join()

print(num)

