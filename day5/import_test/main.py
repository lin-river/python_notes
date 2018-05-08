#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws

import sys,os
# import moduel_import        #在main.py的上级目录，import无法找到文件路径
print(sys.path)                 #环境路径
print(os.path.abspath(__file__) )      #__file__当前文件的绝对路径
#os.path.abspath获取当前文件的绝对路径
print(os.path.dirname(__file__))        #os.path.dirname获取目录名
print(os.path.dirname(os.path.dirname(__file__)))   #module_import的文件路径


sys.path.append(os.path.dirname(os.path.dirname(__file__))) #将module_import的文件路径添加到main.py环境变量中
print(sys.path)     #此时module_import的文件路径在环境变量中为最后一位
import module_import        #此时再去调用即不会报错

#sys.path.insert(os.path.dirname(os.path.dirname(__file__)))        #将module_import的文件路径添加到main.py环境变量第一位