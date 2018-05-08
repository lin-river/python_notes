#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

class Dog(object):

	def __init__(self,name):
		self.name = name

	@staticmethod						# 静态方法实际上和类没什么关系
	#将其和类的关联截断了，相当于一个单纯的函数，（中国与台湾的关系）
	def eat(self):
		print( "%s is eating %s" % ( self.name,"food" ) )

	def talk(self):
		print( "%s is talking" % self.name )


d = Dog("旺财")
# d.eat()
# TypeError: eat() missing 1 required positional argument: 'self'

d.eat(d)
d.talk()