#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws
"""
模块就是某个东西的一部分。如果一个东西可以分为几部分，或者你可以很容易地把它分解成多个不同部分，我们就说这个东西是模块化的。
乐高（LEGO）积木可能就是模块化最好的例子。可以拿一堆不同的积木，用它们搭建不同的东西。

为什么要那么麻烦地把程序分解为较小的部分呢？要知道我们需要所有这些部分才能让程序正常工作。为什么不直接把所有内容都放在一个大文件中呢？
原因有几个:
    1.这样做文件会更小，因而就能更容易地查找代码。
    2.一旦创建模块，这个模块就能在很多程序中使用。这样下一次需要相同的功能时就不必再从头开始了。
    3.并不是所有模块都要使用。模块化意味着你可以使用各部分的不同组合来完成不同的任务，就像利用同样的一组乐高积木可以搭建不同的东西一样。
"""



print( "-------------- 第一个导入方法：import one -----------------\n")
#import module_import             #导入一个模块
#print( module_import.name )
# module_import.say_hello()

print( "-------------- 第two个导入方法 : import more ----------------- \n")
# import module_import1 , module_import1

print( "-------------- 第 there 个导入方法 : from module import * -----------------\n")
from module_import import *             #导入module_import的所有方法，但不建议这么使用，慎用
#module_import.say_hello()               #报错：NameError: name 'module_import' is not defined
#因为上面的from import导入的是moduel_import内全部方法，而不是module_iport本身

eat()           #使用module_import的话直接调用方法名即可
#in the module_import : eat

def eat():                              #覆盖了1module_import导入的eat()代码
    print( "in the main")

eat()
#因为Python是一个解释性语言，当进行到from module_import import * 时，eat()被导入到main.p
# 当再进行到def eat()时，eat被重新定义，已不再是module_import的内的那个eat()

print( "-------------- 第 four 个导入方法 : from module import method as 别名-----------------\n")
from module_import import eat as work
work()

from module_import import eat,drink,play as work1       #以最后一个为准
work1()