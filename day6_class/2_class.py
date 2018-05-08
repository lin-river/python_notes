#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

class Role(object):
	n = 123									#类变量，存在类的内存里，不用实例化就可以调用
	n_list = []
	name = "类name"
	def __init__(self, name, role, weapon, life_value=100, money=15000):		#加括号自动弹出一个self
		# 构造函数
		# 作用: 在实例化时做一些类的初始化工作
		self.name = name					#实例变量(静态属性)，作用域为实例本身
		self.role = role
		self.weapon = weapon
		self.life_value = life_value
		self.money = money

# --begin--:这些方法永远存在类里，而不是一个实例copy一份
	def shot(self):							# 类的方法，功能(动态属性)
		print("shooting...")

	def got_shot(self):
		print("ah...,I got shot...")

	def buy_gun(self, gun_name):
		print("%s just bought %s" % (self.name,gun_name) )
# --end--:这些方法永远存在类里，而不是一个实例copy一份


r1 = Role('hero', 'police', 'AK47') 					#把一个类变成一个具体对象的过程：实例化（初始化一个类，造了一个对象）
# 上面相当于Role(r1,'hero', 'police', 'AK47'),r1也被当作参数传进去，然后执行r1.name = "hero"...

r2 = Role('Jack', 'terrorist', 'B22')  				#生成一个角色，又称为Role的实例

r1.got_shot()											# Role.got_shot()
r1.buy_gun("AK47")

print( "--------------------------变量作用域-----------------------------")
print( "类变量不用实例化就可以调用:n =",Role.n )
print(r1.n,r1.name )							#先找实例本身，如果实例里没有，再去类里找

print( "\n--------------------给实例修改/添加属性：------------------------")
r2.name = "rose"
r2.bullet_prove = True					#添加新属性，只在r2里
print( r2.name,r2.bullet_prove )

print("实例中不能修改类变量：")
r1.n = "从r1改变的类变量"
print( Role.n,r1.n ,r2.n )						#在实例中改变类变量相当于在r1中生成一个变量名为n的实例变量
# 从r1改变的类变量 123
Role.n = 321							#影响的范围只有类和r2
print( Role.n,r1.n ,r2.n )
print( "列表：用的是同一个内存地址，所以不管是实例还是类调用，结果都一样")
r1.n_list.append("from r1")
r2.n_list.append( "from r2")
Role.n_list.append(" from Role")
print( r1.n_list,r2.n_list,Role.n_list )
# ['from r1', 'from r2', ' from Role'] ['from r1', 'from r2', ' from Role'] ['from r1', 'from r2', ' from Role']

print( "-------------------------- 删除属性 -----------------------------")
del r2.bullet_prove
