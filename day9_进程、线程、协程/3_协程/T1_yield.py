#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import time
import queue

# 注意到yield是个表达式而不仅仅是个语句，所以可以使用x = yield r 这样的语法。

def consumer(name):
	print("--->starting eating baozi...")
	while True:
		new_baozi = yield								# 每次调用yield会暂停，而可以使用next()函数和send()函数可以恢复生成器。
		print("[%s] is eating baozi %s" % (name, new_baozi))
	# time.sleep(1)

def producer():
	r = con.__next__()
	r = con2.__next__()
	n = 0
	while n < 5:
		n += 1
		con.send(n)
		con2.send(n)
		print("\033[32;1m[producer]\033[0m is making baozi %s" % n)


if __name__ == '__main__':
	# 第一次调用知识将函数变成生成器，卡在了yield那
	con = consumer("c1")
	con2 = consumer("c2")
	p = producer()