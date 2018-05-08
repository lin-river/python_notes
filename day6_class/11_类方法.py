#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

class Dog(object):
	name = "class var name"				# 如果没有这一句会报错# AttributeError: type object 'Dog' has no attribute 'name'

	def __init__(self,name):
		self.name = name

	@classmethod					 # 只能访问类变量，不能访问实例变量
	def eat(self):
		print( "%s is eating %s" % ( self.name,"food" ) )

	def talk(self):
		print( "%s is talking" % self.name )

d = Dog( "旺财")
d.eat()
