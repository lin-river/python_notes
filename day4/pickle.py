#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws

import pickle
print( "pickle 的用法和json完全一样,但pickle可以序列化所有的数据类型")
print( "而且pickle只能在python里用，在Java就不能用了，Java只认识json")
info = {
    "name":"linhaha",
    "age":20,
}
#序列化
with open( "test2.txt","wb") as f:
    f.write( pickle.dumps( info))       # = pickle(info ,f)

#反序列化
with open( "test2.txt","rb") as f:
    data = pickle.loads( f.read() )     #data = pickle.loads(f)