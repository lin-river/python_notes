#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws

b = """{
            'bakend': 'www.oldboy.org',
            'record':{
                'server': '100.1.7.9',
                'weight': 20,
                'maxconn': 30
            }
        }"""

b = eval(b)         #内置函数，将字符串转化为字典
print(b)
print(b["record"])