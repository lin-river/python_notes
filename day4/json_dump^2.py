#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws

import json

info = {
    "name":"linhaha",
    "age":20
}
#序列化
with open( "test3.txt","w") as f:
    json.dump( info ,f)
    info["age"] = 19
    json.dump( info , f)


#反序列化
with open( "test3.txt","r") as f:
    json.load(f)       #dump可以dump好几次，load只能load一次