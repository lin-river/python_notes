#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

class Animal(object):
	def __init__(self, name):  # Constructor of the class
		self.name = name

	def talk(self):  # Abstract method, defined by convention only
		# raise NotImplementedError("Subclass must implement abstract method")
		pass

	# --begin--: 将多态的思想的放入父类
	@staticmethod
	def animal_talk(obj):
		obj.talk()
	# -- end --: 将多态的思想的放入父类

class Cat(Animal):
	def talk(self):
		print('%s: 喵喵喵!' % self.name)


class Dog(Animal):
	def talk(self):
		print('%s: 汪！汪！汪！' % self.name)

c1 = Cat('小晴')
d1 = Dog('李磊')

# def func(obj):  # 一个接口，多种形态
# 	obj.talk()
# func(c1)
# func(d1)

Animal.animal_talk(c1)
Animal.animal_talk(d1)