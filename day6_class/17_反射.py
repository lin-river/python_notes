#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

def bulk(self):
	print("%s is yelling..." % self.name)

class Dog(object):
	def __init__(self,name):
		self.name = name

	def eat(self,food):
		print( "%s is eating... " % self.name,food)

d = Dog( "wancai")
choice = input( ">>:(eat)").strip()
# 根据用户输入去调用类方法，如输入"eat"就去调用eat()
# d.choice							# 不能通过这样去调用
# AttributeError: 'Dog' object has no attribute 'choice'

print( "1.首先判断对象obj里是否有相应输入的字符串name_str的方法：hasattr(obj,name_str)")
#  用以下方法并不实际
# 	if choice == "eat":
# 		d.eat()
print( hasattr( d,choice ) )			#hasattr(实例名，查询的方法名)
# >>:eat
# True

print( "2.根据字符串去获取obj对象里的对应方法的内存地址：getattr(obj,name_str):")
print( getattr( d,choice ))				# 找到一串内存地址
# <bound method Dog.eat of <__main__.Dog object at 0x000000E671EE9A20>>

print( "3.调用：")
getattr(d,choice)("food")


print("\n-------------结合---------------")
choice = input( ">>:").strip()
if hasattr(d,choice):
	func = getattr(d,choice )
	func("baozi")
	#上面是方法，若是属性，则有：
	# setattr(d,choice,"新值")
elif choice == "talk":
	print("setattr()给一个对象添加新的属性")
	setattr(d,choice,bulk )				# 相当于动态将一个函数放到类里,
	d.talk(d)
else:
	setattr(d,choice,18 )				# 将一个属性动态传入类中，
	print( getattr(d,choice ) )
	# >>:age							# age为不存在的变量，故18赋值给age，如果是存在的变量者走第一条if
	# 18


print( "删除：")
#先判断存不存在：
if hasattr(d,choice):
	delattr(d,choice )
