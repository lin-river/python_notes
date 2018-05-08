#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"


class MyType(type):
    def __init__(self,*args,**kwargs):
        print("Mytype __init__",*args,**kwargs)

    def __call__(self, *args, **kwargs):					# __call__用来创建__new__
        print("Mytype __call__", *args, **kwargs)
		#若没有以下以下两句，Foo类将不会执行，即没有以下两句结果：
			# Foo __new__ <class '__main__.Foo'>
			# Foo __init__
        obj = self.__new__(self)							# 相当于开辟了一块内存空间，调用Foo的__new__
        # print("obj ",obj,*args, **kwargs)
        # print(self)
        self.__init__(obj,*args, **kwargs)					# 调用Foo里的__init__
        return obj

    def __new__(cls, *args, **kwargs):
        print("Mytype __new__",*args,**kwargs)
        return type.__new__(cls, *args, **kwargs)


class Foo(object,metaclass = MyType):
	# metaclass = MyType					# 放在这里也是可以的
    def __init__(self,name):
        self.name = name
        print("Foo __init__")

	# --begin--: __new__ 是用来创建实例化的
    def __new__(cls, *args, **kwargs):
		# 通过__new__来实例化的，通过new来调用的__init__()
        print("Foo __new__",cls, *args, **kwargs)					# cls 为Foo
        return object.__new__(cls)									# 去继承父亲的__new__方法
		# 若没有以上这句话，将不会执行__init__
		#实例化时先调用的__new__再通过"return object.__new__(cls)"调用的__init__
		#Foo __new__ <class '__main__.Foo'> hello
		# Foo __init__
	# -- end --: __new__ 是用来创建实例化的

f = Foo("hello")

# print("f",f)
# print("fname",f.name)

# 作用：自定义一个类

# 执行顺序：
# MyType.__new__() --> MyType.__init__() --> MyType.__call__() --> Foo.__new__() -->Foo.__init__()