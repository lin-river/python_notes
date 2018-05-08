#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws

calc = lambda n:n*n         #匿名函数就是不需要显式的指定函数
print(calc(10))

#以下是一个最简单的函数调用
def sayhi(n):
    print(n)
sayhi("hahahahahaha")

#将以上的函数改为匿名函数如下：

( lambda n:print( n ) )("hehehehehehehehe")
#lambda n:print( n ) --> 返回一个内存地址，加个括号即为可调用函数
#("hehehehehehehehe")   --> 后面的括号内是传进去的参数

#便于理解的语句如下：
c = lambda n:print( n )
c("heiheiheiheiheihei...")

print( "lambda 处理不了类似for语句这样复杂的语句，判断语句也不能写，顶多写个三元运算")

d = lambda n: 3 if n < 4 else  n
print( "d(4):",d(4) )
print( "d(2):",d(2) )

#单独用lambda其实用的不多，因为你会发现其实代码没少多少，lambda要和其他结合起来使用
print( "-------------- filter ---------------------")
print( "将range()里的数提取出来放到lambda的n中，过滤出来符合条件的形成一个新的迭代器，并返回这个迭代器")
res = filter(lambda n : n>5 ,range(10) )        #
for i in res:
    print(i)
print( "-------------- map ---------------------")
print( "将range()里的数提取出来放到lambda的n中，每一个值都用func内的方式进行处理，并形成一个新的迭代器，并返回这个迭代器")
res2 = map( lambda n : n*n,range(10) )      #将range()里的数提取出来放到lambda的n中，
for i in res2:
    print(i)

#以上的代码相当于如下：
res3 = [ lambda n : n*n for i in range(10) ]
for i in res3:
    print(i)

print( "-------------- reduce ---------------------")
import functools
res = functools.reduce( lambda x,y:x+y,range(10) )
print( res )
#reduce的作用：
# x = range(0),y = range(1)
# x = x + y,y = range(2)
#......

res = functools.reduce( lambda x,y:x*y,range(1,10) )
print( res )
# x = range(1),y = range(2)
# x = x * y,y = range(3)
#......