#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

# 管道通信：
# The Pipe() function returns a pair of connection objects connected by a pipe which by default is duplex (two-way).
# Pipe（）函数返回一对由管道连接的连接对象，默认情况下为双工（双向）

import multiprocessing


def f(conn):
	conn.send([42, None, 'hello from child'])
	print( "From parent: ",conn.recv() )
	conn.send([42, None, 'hello2 from child'])				# 子进程多发无所谓。父进程如果多收主进程就会等待( 和socket差不多 )
	conn.close()


if __name__ == '__main__':
	parent_conn, child_conn = multiprocessing.Pipe()			# 生成管道实例，parent_conn为管道这头，child为管道另一头( 其实哪头传给子进程都无所谓)
	p = multiprocessing.Process(target=f, args=(child_conn,))
	p.start()
	print( parent_conn.recv() )  # prints "[42, None, 'hello']"
	parent_conn.send( "子进程你好！" )
	p.join()