#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

class Dog:										#定义狗类

	def __init__(self,name):					#传入参数
		# 在创建对象时设置属性。这称为初始化对象。
		self.name = name
		# self这个名字在Python中没有任何特殊的含义。只不过所有人都使用这个实例引用名。这也是让代码更易读的一个约定。
		# 也可以把这个实例变量命名为你想要的任何名字，不过强烈建议你遵循这个约定，因为使用self 能减少混乱。

	def call(self):								#定义了一个类方法
		print( "%s: 汪！" % self.name )

dog1 = Dog("旺财")
dog1.call()										#调用类方法


# 新增一些属性
dog1.newProperty = "Property"
print( dog1.newProperty )