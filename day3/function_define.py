#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws

#定义函数
def func1():                #函数名要能反映其意义
    "test1"
    print("in the func1")
    return 0

#定义过程
def func2():
    "test2"
    print("in the func2")

x = func1()
y = func2()

print("from func1 return is %s" %x)
print("from func2 return is %s" %y)

#日志函数
import time
def logger():
    time_format = "%Y-%m-%d %X"
    time_current = time.strftime(time_format)           #引用上面time_foemat的显示格式
    with open("a.txt","a+",encoding="utf-8") as f:
        f.write("---------%s-----------\n"%time_current)

def test1():
    print("in the test1")
    logger()
def test2():
    print("in the test2")
    logger()
def test3():
    print("in the test3")
    logger()

test1()
test2()
test3()

#返回值
def return_test1():
    print("return_test1")
    return 0
    print("hahahahaha")         #renturn之后的语句不会执行，但也不会报错

def return_test2():
    print("return_test2")
    #没有return，函数隐式返回None

def return_test3():
    print("return_test3")
    return 0,"hello",["haha","hehe"],{"1":"lin"}        #将一堆东西变成元组返回

def return_test4():
    print("return_test4")
    return return_test1()           #f返回一个函数(高阶函数)

x = return_test1()
y = return_test2()
z = return_test3()

print("from return_test1 return is %s" %type(x),x)
print("from return_test2 return is %s" %type(y),y)
print("from return_test3 return is %s" %type(z),z)
print(return_test4())