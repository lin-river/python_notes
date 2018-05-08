#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws

print( "in the 'package\\__init__.py'")

from . import Tt1       #从当前目录下导入Tt1文件, . 相当于绝对目录
#相当于将Tt1.py中的内容在__init__.py文件解释了一遍,如下
"""
print( "in the package_T\\Tt1.py")
"""