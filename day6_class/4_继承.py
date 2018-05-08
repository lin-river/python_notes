#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

class People:

	def __init__(self,name,age):
		self.name = name
		self.age = age

	def eat(self):
		print( "%s is eating..." % self.name )

	def talk(self):
		print( "%s is talking..." % self.name )

	def sleep(self):
		print( "%s is sleeping..." % self.name )


class Man( People ):					# 继承People类的方法
	def sex(self):						#若没有这一句相当于覆盖父类方法
		print( "%s is sexing ...... done " % self.name )

	def sleep(self):					# 修改父类方法
		People.sleep(self)
		print( "man is sleeping...")

class Woman( People ):
	def get_birth(self):
		print( "%s is born a baby..." % self.name )

m1 = Man("hero",18)
m1.eat()
m1.sex()
print( "继承People类的方法:")
m1.sleep()
print( "woman类:")
w1 = Woman( "woman",18)
w1.get_birth()