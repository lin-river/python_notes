#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

class myselfException(Exception):			# 继承基类Exception异常
	def __init__(self, msg):
		self.message = msg

	# 因为继承了基类Exception，所以这里注释掉也没关系
	# def __str__(self):					# E返回的内容在这里规定
	# 	return self.message					# 也可以返回其他值

try:
	raise myselfException("数据库连不上")				# raise : 触发	 自己写的异常不会自动触发，只能用raise自己触发
except myselfException as e:
	print( e )





class IndexError(Exception):
	def __str__(self):
		return "lalalala"
try:
	name = []
	name[3]
except IndexError as e:
	print( e )
# 还是会报以下错，自定义的类重名会影响原来的，会使原来的错误无法抓住
# IndexError: list index out of range