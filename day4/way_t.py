#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws
import sys,os
print(os.path.dirname(os.path.dirname(__file__)))
# import pachage_T          #找不到package_T，因为package_T所在的环境路径为C:/Users/herolh/Desktop/oldman/day5
                            # 添加的环境路径为C:/Users/herolh/Desktop/oldman
# 这个时候想找到package_T，就需要用到如下
from day5 import package_T
print(sys.path)

#sys.path.append(os.path.dirname(os.path.dirname(__file__)))