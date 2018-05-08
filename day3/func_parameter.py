#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws

def parameter_test1(x,y):     #形参
    print(x)
    print(y)
#位置参数和关键字参数
parameter_test1(2,1)          #实参，位置参数调用
parameter_test1(y = 2,x = 1)    #关键字参数调用，这样不用按照函数定义的文字填参数
#parameter_test1(x = 2,3)        #报错，相当于赋予x多个值，关键参数不能写在位置参数之前的

#默认参数:
print( "-------默认参数---------")
def parameter(x,y = 2):
    print("x = %s" %x)
    print("y = %s" %y)

parameter(1)
parameter(1,3 )

#函数的非固定参数
print( "-------函数的非固定参数---------")
def parameter3(*args):         #接收n个位置参数，转化成元组的方式
    print(args)

parameter3(1,2,3,4,5)
parameter3(*[1,2,3,4,5])        #args = tuple（[1,2,3,4,5]）

def parameter4(x,*excess):
    print("x = %s" % x)
    print(excess)

parameter4(1,2,3,4,5)           #可传超越形参个数的实参

#接收字典作为参数
print( "-------字典作为参数---------")
def parameter5(**kwargs):          #把n个关键字参数，转化为字典的方式
    print(kwargs)
    print(kwargs["name"])
    print(kwargs["age"])
parameter5(name = "lin",age = "20",sex = "man")
parameter5(**{"name" :"lin","age" : "20","sex" : "man"})

#混合字典参数
print( "-------混合字典参数---------")
def parameter6(name,**kwargs):
    print(name)
    print(kwargs)

parameter6("lin")           #不传默认为空字典
#parameter6("lin","xxxx")    #字典参数只接受关键字参数，否则报错
parameter6("lin",age = 18,sex = "m")

def parameter7(name,*args,**kwargs):
    print(name)
    print(args)
    print(kwargs)
parameter7("lin",age = 18,sex = "m")        #没有位置参数，所以args打印出来的为空元组