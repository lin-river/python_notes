#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws

import time

def timmer_decorator(func):                 #装饰器本身就是一个函数
    def warpper(*args,**keargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print("The func run time is %s" %(stop_time-start_time))
    return warpper

@timmer_decorator                           #不修改原函数的源代码和调用方式
def function1():
    print("----------decorator1-----------")
    time.sleep(1)
    print("----------decorator1-----------")

function1()

print("-------------分割线1--------------")
def foo():
    print("in the foo()")
    bar()
# foo()             #报错，bar()在此时未定义
def bar():
    print("in the bar()")

foo()