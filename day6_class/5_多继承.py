#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

# class People: 经典类
class People(object): 				# 新式类,object:基类

	def __init__(self,name,age):
		self.name = name
		self.age = age
		self.friends = []

	def eat(self):
		print( "%s is eating..." % self.name )

	def talk(self):
		print( "%s is talking..." % self.name )

	def sleep(self):
		print( "%s is sleeping..." % self.name )

class Relation(object):
	def make_friends(self,obj):							# obj :传进来的参数
		print( "%s is making friend with %s" % (self.name,obj.name))
		self.friends.append(obj)						# 地址，这样即使改名了还是那个人

class Man( People,Relation ):

	# --begin--:重构__init__函数
	def __init__(self,name,age,money):								# 当需要添加参数的时候就需要重构__init__函数
		People.__init__(self,name,age)								# 将父类的值传过来，经典类写法
		# super(Man,self).__init__(name,age )						# 作用和上面那个是一样的，方便一点，一句话搞定，是新式类的写法
		self.money = money
		print( "%s 一出生就有 %s money" % (self.name, self.money ) )
	# --end--:重构__init__函数

	def sex(self):
		print( "%s is sexing ...... done " % self.name )

	def sleep(self):					# 修改父类方法
		People.sleep(self)
		print( "man is sleeping...")

class Woman( People,Relation ):
	def get_birth(self):
		print( "%s is born a baby..." % self.name )

m1 = Man("hero",18,2000000)
w1 = Woman("woman",18)
m1.make_friends(w1)
print( m1.friends )
# [<__main__.Woman object at 0x000000E0FD5B9EF0>]			#这样即使改了名字也会比较方便
w1.name = "WOMAN改"
print( m1.friends[0].name )