#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws

#不能写绝对路径，只能写相对路径，因为这样可移植性才高
#调用只能调用同级或者下级，不能向上调用
print(__file__)     #返回当前目录的相对路径，只是因为在pycharm里所以打印出绝对路径，用命令行试一试
#我们要将程序的绝对路径获取到，动态的加到系统的环境变量中，所以就有

import os
print( os.path.abspath( __file__ ) )        #绝对路径
print( os.path.dirname( os.path.abspath(__file__) ) )   #y要路径名不要文件名
#C:\Users\herolh\Desktop\oldman\day4\ATM_dir\bin
print( os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ) )    #再往上走一级就到了根目录
#C:\Users\herolh\Desktop\oldman\day4\ATM_dir


#添加环境变量
import sys
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
sys.path.append(BASE_DIR)

import conf,core       #此时调用其他不同级模块，此处标红是因为这是动态添加，pycharm启动之前根本不知道这个环境变量
#调用如下：
from conf import settings
from core import main

main.login()
