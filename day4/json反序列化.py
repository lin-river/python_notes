#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws

f = open( "test.txt","r")
data = eval( f.read())      #将字符串转化为字典
f.close()
print( data["age"])

#以上并不规范，所以有如下就送规范
import json
f = open( "test.txt","r")
data = json.loads( f.read() )
print( data["age"])