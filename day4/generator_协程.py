#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws

import time

def consumer(name):             #吃包子
    print("%s 准备吃包子啦！" %name)
    while True:
        baozi = yield               #单纯调用__next__()不会给传值，但是send()可以给send()传值
        print("包子[%s]来了，被[%s]吃掉了！" %(baozi,name))

print("----------send()和__next__()的区别------------")
#send()和__next__()的区别：
#__next__()只是单纯的调用yeild，不会给yeild传值
# send()调用yeild的同时给yeild传一个值
c = consumer("lin")
c.__next__()        #lin 准备吃包子啦！     因为运行到yeild生成器中断不运行，故接下来的print没执行
                    # 第一个next将函数变成生成器
c.__next__()        #包子[None]来了，被[lin]吃掉了！    因为__next__()不会给yeild传值,yeild 无值
taste = '韭菜馅'
c.send(taste)           #send发送
#包子[韭菜馅]来了，被[lin]吃掉了！    #taste被yeild接收到了，yeild又将值赋给baozhi

def producer(name):         #生产包子
    c1 = consumer("A")
    c2 = consumer("B")
    c1.__next__()
    c2.__next__()
    print("老子开始准备做包子了！")
    for i in range(10):
        time.sleep(1)
        print("做了1个包子，分了两半！")
        c1.send(i)
        c2.send(i)

print("\n----------协程(看似单线程并行，实际上还是在串行，以后异步io的雏形)，边做边吃------------")
producer("lin")
#协程是比线程更小的一个单位，寄生在线程中