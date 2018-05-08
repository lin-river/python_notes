#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

class Foo(object):
	def __init__(self, name):
		self.name = name

f = Foo("alex")
# 上述代码中，f 是通过 Foo 类实例化的对象，其实，不仅 f 是一个对象，Foo类本身也是一个对象
# 因为在Python中一切事物都是对象。
# 如果按照一切事物都是对象的理论：obj对象是通过执行Foo类的构造方法创建，那么Foo类对象应该也是通过执行某个类的 构造方法 创建。
print( "-----------------追随类的起源：------------------")
print(type(f))							# f 来自于 Foo
# <class '__main__.Foo'>
print( type( Foo ))						# Foo 来自于type
# <class 'type'>

print( "--------------创建类的两种方式：-----------------")
# a).普通方式
# class Foo(object):
# 	def func(self):
# 		print('hello world!')

# b).特殊方式
def func(self):
	print( "hello world!",self.name )

def __init__(self,name,age):			# 构造函数
	self.name = name
	self.age = age

Foo2 = type('Foo', (object,), {'printf': func,
							   "__init__":__init__})			# type 为类的类
# type第一个参数：类名
# type第二个参数：当前类的基类,继承谁.可以不写
# type第三个参数：类的成员.		"print"为key,随意.	func为value,是方法的内存地址

print( type( Foo2 ))
f = Foo2( "haha","18")
f.printf()