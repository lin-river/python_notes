#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws

def add(x,y,f):
    return f(x)+f(y)

print(add(3,-6,abs))        #abs()内置函数，求绝对值

print("--------把一个函数名当作实参传给另一个函数---------")
import time
def bar():
    time.sleep(1)
    print("in the bar")

def func1(func):            #作用相当于bar()的装饰函数
    print(func)         #打印函数地址
    start_time = time.time()
    func()
    stop_time = time.time()
    print("the func run time is %s" %(stop_time-start_time))

func1(bar)

print("--------返回值中包含函数名---------")
def func2(func):
    print(func)
    return  func

print(func2(bar))       #返回bar的内存地址
bar = func2(bar)        #再次调用func2，将func2的返回值传给bar
bar()                   #给bar函数增加了新功能，没有改变其调用方式

print("--------------嵌套函数--------------")
def foo():
    print("in the foo")
    def bar2():                 #在函数内再用def去声明一个函数，这才叫做嵌套
        print("in the bar2")
    bar2()
foo()
# bar2()          #报错，因为bar2()现在是一个局部函数，无法直接在全局调用

# def test1():
#     test2()     #注意，这不叫函数的嵌套，这叫函数地1调用