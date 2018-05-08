#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws
print("--------------高阶函数---------------")
import time
def time1():
    time.sleep(1)
    print("in the time1")

def time2():
    time.sleep(1)
    print("in the time2")

def deco(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    print("The func run time is %s" %(stop_time-start_time))

deco(time1)     #改变了函数的调用方式

print("----------高阶函数+嵌套函数-----------")
def timer(func):
    def deco():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("The func run time is %s" % (stop_time - start_time))
    return deco

time1 = timer(time1)   # = @timer <==> time1 = timer(time1) = deco
time1()

print("-----以下装饰器可满足日常90%的需求------")

def timer2(func):
    def deco(*args,**kwargs):       #非固定参数，加上之后这个装饰器才能算是通用的
        start_time = time.time()
        func(*args,**kwargs)                      #原函数有参数，若装饰器未考虑道参数问题则会报错
        stop_time = time.time()
        print("The func run time is %s" % (stop_time - start_time))
    return deco

@timer2                  #time3 = timer(time3) = deco
def time3(name):                        #原函数带参数
    print("%s in the time3" %name)

time3("decorator")                       #有参无参调用没问题

print("-----以下装饰器可满足其他10%的需求------")
use,passwd = "lin","abc123"
def auth(auth_type):
    print("auth func is:",auth_type)
    def out_wrapper(func):
        def wrapper(*args, **kwargs):
            print("wrapper func args: ",*args,**kwargs)
            if auth_type == "local":
                username = input("Username  :  ").strip()  # 去掉字符串两头的空格换行等
                password = input("Password  :  ").strip()
                if use == username and passwd == password:
                    print("\033[32;1mUser has passed authentication\33[0m")
                    res = func(*args, **kwargs)  # 虽然home有返回值，但是在装饰器离并没有保存下来,所以给一个res保存lin
                    return res
                else:
                    exit("\033[31;1mInvalid username or password\33[0m")
            elif auth_type == "remote":
                print("搞毛线remote，不会，任性，你咋滴")
        return wrapper
    return out_wrapper

def index():
    print("Welcome to index page!")

@auth(auth_type="local")
def home():
    print("Welcome to home page!")
    return "I have a return"

@auth(auth_type = "remote")
def bbs():
    print("Welcome to bbs page!")

index()
print(home())          #调用home()相当于调用wrapper(),,home有返回值，而wrapper没有返回值，故此处调用无返回一个none
bbs()
