#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

from lib.a import C

obj = C()
print(obj.__module__)  		# 输出 lib.aa，即：输出模块的绝对路径
print(obj.__class__ )     # 输出 lib.aa.C，即：输出类本身

class Dog(object):
	def __init__(self,name):
		# __init__()方法会在对象创建时完成初始化。每个对象都内置有一个__init__()方法。
		# 如果你在类定义中没有加入自己的__init__()方法，就会有这样一个内置方法接管，它的工作就是创建对象。
		self.name = name

	def talk(self):
		print( "%s is talking" % self.name )

	# --begin--:对象后面加括号，触发执行
	def __call__(self, *args, **kwargs):
		print( "runnig call",args,kwargs )
		# 如果没有这个方法会报以下错误
		# d()
		# TypeError: 'Dog' object is not callable
	# -- end --:对象后面加括号，触发执行

	# --begin--:
	def __str__(self):
		# 另一个特殊方法是__str__()，它会告诉Python打印（print）一个对象时具体显示什么内容。Python会默认以下内容。
		# 	1.实例在哪里定义
		# 	2.类名
		# 	3.存储实例的内存位置（0x00BB83A0部分）
		# 不过，如果你希望print为对象显示其他的内容，可以定义自己的__str__()，这会覆盖内置的__str__()方法。
		return "<obj : %s>" %self.name
		# 如果没有这个方法会有以下情况：
		# print(d)
		# <__main__.Dog object at 0x000000D2B2259E48>
	#-- end --：

d = Dog( "wancai")
d( 1,2,3,"call ",name = 4 )
Dog("123")(1,2,3)

print( "\n__dict__ 查看类或对象中的所有成员(属性，方法等):")
print( Dog.__dict__ )				# 通过类调用，打印类里的所有属性，不包括实例属性
# {'__module__': '__main__', '__init__': <function Dog.__init__ at 0x000000A5736AA8C8>, 'talk': <function Dog.talk at 0x000000A5736AA9D8>, '__call__': <function Dog.__call__ at 0x000000A5736AAA60>, '__dict__': <attribute '__dict__' of 'Dog' objects>, '__weakref__': <attribute '__weakref__' of 'Dog' objects>, '__doc__': None}
print( d.__dict__ )					# 通过实例调用，打印所有实例属性，不包括类属性
# {'name': 'wancai'}

print( "\n如果一个类中定义了__str__方法，那么在打印 对象 时，默认输出该方法的返回值")
print( d )

print( "\n__getitem__、__setitem__、__delitem__的用法：")
#将实例变成字典来操作

class Foo(object):
	def __init__(self):
		self.data = {}

	def __getitem__(self, key):
		print('__getitem__:', key)
		return self.data.get(key)

	def __setitem__(self, key, value):
		print('__setitem__:', key, value)
		self.data[key] = value

	def __delitem__(self, key):
		print('__delitem__：', key)

obj = Foo()
print( "__setitem__用法：")
obj["name"] = "hero"

print( "__getitem__用法：")
obj["name"]
# __getitem__: name
print(obj["name"])
# __getitem__: name
# hero

print( "__delitem__用法：")
del obj["name"]
# __delitem__： name
del obj["123"]				# 可以在def __delitem__(self, key):里加个判断即可
# __delitem__： 123

# result = obj['k1']  # 自动触发执行 __getitem__
# obj['k2'] = 'alex'  # 自动触发执行 __setitem__
# del obj['k1']