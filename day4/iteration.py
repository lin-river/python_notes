#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws

from collections import Iterable        #Iterable ： 可迭代的
print("--------判断是否为可迭代对象-----------")
print(isinstance(["list"],Iterable))   #使用isinstance()判断一个对象是否是Iterable对象
print(isinstance("str",Iterable))
print(isinstance(("tuple"),Iterable))
print(isinstance({"dict":1},Iterable))
print(isinstance(10,Iterable))          #单个数字无法迭代
#可迭代对象(iterable)和迭代器(iterator)不是一回事

iterable = [1,2,3]
print( dir( iterable ) )        #dir(a)可以返回调用a的所有方法
#可以看到a内无next()方法，所以不叫迭代器，只叫可迭代对象
#以上都只能叫可迭代对象而不叫迭代器
print("----------------判断列表生成式------------------")
print( isinstance( ( i for i in range(10) ), Iterable ) )       #生成式也是可迭代对象
#生成器一定是迭代器，因为有next()方法，但迭代器不一定是生成器

print("-------------将可迭代对象变成迭代器--------------")
iterator = iter( iterable )             #iter()内置函数，将可迭代对象变成迭代器
print( iterator )           #<list_iterator object at 0x0000007E37266898>
print( iterator.__next__() )
print( iterator.__next__() )
print( iterator.__next__() )
#print( iterator.__next__() )       #和生成器一样，当没有数据时，会报一个异常StopIteration错误
print("---------------------range()---------------------")
print( range(10) )      #在python3.x中实际上就是一个迭代器
# 若在python 2.X上直接返回一个0~9的列表，python 2.X通过xrange()将将可迭代对象变成迭代器
for i in range(5):
    print(i)

print("----#以上等价于如下：#----")

it = iter( [ 0,1,2,3,4 ] )
while True:
    try:
        x = next( it )
        print( x )
    except StopIteration:       #遇到StopInteration就退出循环
        break

print("----#文件操作中的for line in f: #----")
#文件操作中的for line in f:   其实就是一个迭代器
#若通过f.readline(),那将会把文件内所有内容提取到内存生成一个列表
#for line in f:print(line)      #每一次print()就是去迭代一次
#在python3.X中已经看不出迭代器的痕迹了
#而在python2.X上f有一个next()方法，但默认不能直接调用
#   必须通过for line in f.xreadline():才能使用并且只能使用next()方法，readline()已经没用了
f = open("Text_for_iterator.txt","r",encoding = "utf-8")
for line in f:
    print(line.strip())
