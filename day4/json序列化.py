#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws

info = {
    "name":"linhaha",
    "age":20
}

f = open( "test.txt","w")
f.write( str( info ))       #f.write只能写入字符串，所以必须使用str()将字典转化为字符串

f.close()

#以上并不规范，所以有如下就送规范
import json
with open( "test.txt","w+") as f:
    print( json.dumps(info) ,type( json.dumps(info) ) )
    f.write( json.dumps(info) )


#以下会报错，因为json只能处理简单的字符串类型
#json是所有语言里面都通用的，所以以后在和其他语言进行交互的时候
#比如将Java的字典转化为python的字典
#但是因为Java的类和python的类完全不一样了，所以json只能进行简单的处理
"""
def sayhi():
    print("hello world!")

info1 = {
    "name":"linhaha",
    "age":20,
    "func":sayhi
}
with open( "test.txt","w+") as f:
    print( json.dumps(info1) ,type( json.dumps(info1) ) )
    f.write( json.dumps(info1) )
"""
