#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

# 正常导入模块：
# form lib import a
modname = "a"
# 错误导入方法：
# from lib import modname
# ImportError: cannot import name 'modname'
# from lib import "a"
# SyntaxError: invalid syntax

print( "---------------以下为解释器自己内部用的:------------------")
# __import__('import_lib.metaclass') #这是解释器自己内部用的
# 以下为错误示范
# __import__('lib.a')
# obj = C()
# print( obj.name )

mod = __import__( "lib.a")				# mod相当于lib
print( mod )
# <module 'lib' (namespace)>			# namespace 相当于'C:\\Users\\Herolh\\Desktop\\news\\oldman\\day6_class\\lib\\__init__.py'
print( mod.a )
# <module 'lib.a' from 'C:\\Users\\Herolh\\Desktop\\news\\oldman\\day6_class\\lib\\a.py'>
print( mod.a.C )
# <class 'lib.a.C'>
instance = getattr(mod.a,"C")
print( instance )

print( "\n官方建议用以下这个：")
import importlib
# importlib.import_module('import_lib.metaclass') #与上面这句效果一样
a = importlib.import_module( "lib.a")
print( a )
# <module 'lib.a' from 'C:\\Users\\Herolh\\Desktop\\news\\oldman\\day6_class\\lib\\a.py'>
print( a.C().name )