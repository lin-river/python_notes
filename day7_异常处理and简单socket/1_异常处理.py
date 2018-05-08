#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

data = {}
name = ["zao","qian","sun","li"]

try :									# 尝试执行下列这段代码
	# name[4]								# 第一个出错后就不往下进行了
	# data["name"]
	# open( "t.txt")
	print(name[0] )
except KeyError as info:				# 除了报KeyError这个类型的错，否则不执行下列代码，Info 为错误日志
	print( "没有 %s 这个Key" % info )
except IndexError as info:
	print( "列表操作异常：%s" % info )
except FileNotFoundError as E:
	print( "出错了：",E )
#还能对多个(2个)错误进行处理，但处理结果只有一种
# except (KeyError,IndexError) as info:
# 	print("Error!")

# 相当于最后的else：
except Exception as E:					# 处理所有错误类型，但是是哪种错误类型只能自己揣测
	print( "未知错误！" )
else:
	print( "一切正常的情况下执行这一条！")
finally:
	print( "不管有没有错都会执行")


# 常用异常

# AttributeError 试图访问一个对象没有的树形			比如foo.x，但是foo没有属性x
# IOError 输入/输出异常；基本上是无法打开文件				--》现在叫FileNotFoundError
# ImportError 无法引入模块或包；基本上是路径问题或名称错误
# IndentationError 语法错误（的子类） ；代码没有正确对齐
# IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
# KeyError 试图访问字典里不存在的键
# KeyboardInterrupt Ctrl+C被按下
# NameError 使用一个还未被赋予对象的变量
# SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
# TypeError 传入对象类型与要求的不符合
# UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它
# ValueError 传入一个调用者不期望的值，即使值的类型是正确的

