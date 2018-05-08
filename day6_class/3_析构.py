#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

class Role(object):
	n = 123									#类变量，存在类的内存里，不用实例化就可以调用
	name = "类name"
	def __init__(self, name, role, weapon, life_value=100, money=15000):		#加括号自动弹出一个self
		# 构造函数
		# 作用: 在实例化时做一些类的初始化工作
		self.name = name					#实例变量(静态属性)，作用域为实例本身
		self.role = role
		self.weapon = weapon
		self.__life_value = life_value
		self.money = money


	def __del__(self):				# 析构函数：实例释放，销毁的时候自动执行的，通常做一些收尾工作
		print("%s 彻底死了。。。" %self.name )


	# --begin--:这些方法永远存在类里，而不是一个实例copy一份
	def show_status(self):
		print( "name: %s weapon: %s life_value:%s" % ( self.name,self.weapon,self.__life_value ) )

	def shot(self):  # 类的方法，功能(动态属性)
		print("shooting...")

	def got_shot(self):
		self.__life_value -= 50
		print("ah...,I got shot...")

	def buy_gun(self, gun_name):
		print("%s just bought %s" % (self.name, gun_name))

	# --end--:这些方法永远存在类里，而不是一个实例copy一份

print("--------------析构函数执行情况-------------------")
# print("第一种：")
# r1 = Role( "hero","pelice","AK47" )
# # hero 彻底死了。。。

# print("第二种：")
# r1 = Role( "hero","pelice","AK47" )
# r1.buy_gun("AK47")
# r1.got_shot()
# # hero just bought AK47
# # ah...,I got shot...
# # hero 彻底死了。。。

# print('第三种：')
# r1 = Role('hero', 'police', 'AK47')
# r1.buy_gun("AK47")
# r1.got_shot()
#
# r2 = Role('Jack', 'terrorist', 'B22')
# r2.got_shot()
# # hero just bought AK47
# # ah...,I got shot...
# # ah...,I got shot...
# # hero 彻底死了。。。							#程序退出的时候自动销毁
# # Jack 彻底死了。。。

# print('第四种：')
# r1 = Role('hero', 'police', 'AK47')
# r1.buy_gun("AK47")
# r1.got_shot()
# del r1										#手动销毁
# r2 = Role('Jack', 'terrorist', 'B22')
# r2.got_shot()
# # hero just bought AK47
# # ah...,I got shot...
# # hero 彻底死了。。。
# # ah...,I got shot...
# # Jack 彻底死了。。。

print( "---------------------- 私有属性 ----------------------")
r1 = Role('hero', 'police', 'AK47')
# print( r1.__life_value )					# 私有属性对类外部是属于隐藏状态
# AttributeError: 'Role' object has no attribute '__life_value'
print( "若要访问私有属性，只能类内部访问，即在类内设置方法调用")
r1.got_shot()
r1.show_status()
