#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = Hero lws
import sys,random
# sys.argv           命令行参数返回List，脚本的名称总是sys.argv列表的第一个参数，接着是参数
if random.randint(1,2) == 1:
	sys.exit(0)        	 # 退出程序，正常退出时exit(0)
print( sys.version )         #获取Python解释程序的版本信息

# print( sys.maxint)			#最大的Int值,python3后没了,改为以下方法
print( sys.maxsize )

print( sys.path )           # 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
print( sys.platform )       		#返回操作系统平台名称
# 当今的程序比较流行的是跨平台。简单的说就是这段程序既可以在windows下，换到linux下也可以不加修改的运行起来
# 假设，我们想实现一个清除终端，linux下用clear, windows下用cls,则有：
ostype = sys.platform
if ostype == 'linux' or ostype == 'linux2':
	cmd = "clear"
else:
	cmd = "cls"
print( cmd )