#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

from multiprocessing import Process
import os

def info(title):
	print(title)
	print('module name:', __name__ )
	print('parent process:', os.getppid()	)		# 打印父进程id
	print('process id:', os.getpid()	)			# 打印本进程id
	print("\n\n")


def child_info(name):
	info('\033[31;1mcalled from child process function child_info \033[0m')
	print('hello', name)


if __name__ == '__main__':
	info('\033[32;1mmain process line\033[0m')
	p = Process(target=child_info, args=('bob',))
	p.start()
	p.join()

# main process line
# module name: __main__
# parent process: 6316				# pycharm的pid
# process id: 21144					# 主进程的id
#
#
#
# function fcalled from child process function child_info
# module name: __mp_main__
# parent process: 21144				父进程
# process id: 23068					本进程