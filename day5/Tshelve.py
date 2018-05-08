#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = Hero lws
import datetime
import shelve			#shelve模块是一个简单的k,v将内存数据通过文件持久化的模块，可以持久化任何pickle可支持的python数据格式
# shelve模块比pickle模块简单，只有一个open函数，返回类似字典的对象，可读可写;key必须为字符串，而值可以是python所支持的数据类型

f = shelve.open( 'shelve_test')		#打开一个文件

print("---------------写入-----------------")
# info = { 'age':'18','job':'IT'}
# name = { 'lin','hehehehe','hahahaha'}
# f["name"] = name
# f["info"] = info
# f["date"] = datetime.datetime.now()
# f.close()
#执行后自动多了三个目录文件，bak，dat,dir


print("---------------读取-----------------")
print( f.get( "name" ) )
print( f.get( "info" ) )
print( f.get( "date" ) )