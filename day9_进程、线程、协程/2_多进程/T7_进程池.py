#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

# 线程也可以弄线程池，用信号量来做，但是python没有给你做线程池，因为线程启动的开销太小了
# 线程过多唯一的不好就是：导致CPU切换过于频繁，导致系统过慢
# 但是如果进程过多就会容易把系统搞瘫

# 进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，如果进程池序列中没有可供使用的进进程，那么程序就会等待，直到进程池中有可用进程为止。
# 进程池中有两个方法：
	# apply					同步执行(串行)
	# apply_async			异步执行(并行)

from  multiprocessing import Process, Pool
import time,os


def Foo(i):
	time.sleep(2)
	print( "in process:",os.getpid() )
	return i + 100


def Bar(arg):
	print('-->exec done:', arg,os.getpgid() )

# windows下进程池会出问题，因为windows下的多进程和windows下的多进程不一样
if __name__ == "__main__":				# 在windows上必须加这一句话，否则会报错
	pool = Pool(5)						# Pool( processes=5) 允许进程池内同时放入5个进程，所以，虽然开了10个进程，但是其余五个实际上只是挂起了等待进程池空出位置后再进去

	print(	"主进程pid：",os.getpid() )
	for i in range(10):
		# pool.apply_async(func=Foo, args=(i,), callback=Bar)			# callback=回调(执行完func再执行，func执行没完就不执行 ),这回调还是主进程执行
		# pool.apply(func=Foo, args=(i,))								# 串行
		pool.apply_async(func=Foo, args=(i,))							# 并行

	print('end')
	pool.close()  # 先close再join
	pool.join()  							# 进程池中进程执行完毕后再关闭，如果注释，那么不等子进程结束程序就直接关闭。
