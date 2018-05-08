#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

class Dog(object):
	def __init__(self,name):
		self.name = name
		self.__food = None

	@ property
	def eat(self ):
		print( "%s is eating %s" % ( self.name,self.__food  ) )

	# --begin-- : 给属性变量传参数
	@eat.setter
	def eat(self,food):
		print( "set to food :",food )
		# 不写这一段会报以下错误
		# d.eat = "food"					# 不能这样传参数
		# AttributeError: can't set attribute
		self.__food = food
	# -- end -- : 给属性变量传参数

	# --begin-- : 删除属性方法
	@eat.deleter
	def eat(self):
		del self.__food
		print( "删完了！")
		# 没有这个，直接删除属性方法会出现如下异常：
		# del d.eat
		# AttributeError: can't delete attribute
	# -- end -- : 删除属性方法

	def talk(self):
		print( "%s is talking" % self.name )

d = Dog( "旺财")
# d.eat

# d.eat()
# TypeError: 'NoneType' object is not callable


d.eat
d.eat = "baozi"
d.eat

print( "-------------------属性方法的删除------------------")
print( "正常删除：")
# del d.name
# print( d.name )
# AttributeError: 'Dog' object has no attribute 'name'

print( "正常删除属性方法：")
del d.eat					# @eat.deleter

d.eat
# AttributeError: 'Dog' object has no attribute '_Dog__food'