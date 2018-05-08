#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws

import sys,os
print(sys.path)
print(os.path.abspath(__file__))    #当前文件的绝对路径
print(os.path.dirname(__file__))    #当前文件的绝对路径目录
print(os.path.split(__file__))      #将当前文件的绝对路径目录和文件名以元组的形式返回

