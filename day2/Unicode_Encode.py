#!/usr/bin/env python
# -*- coding:utf-8 -*-          改的只是文件编码
# Author: Hero lws

import sys
print(sys.getdefaultencoding())         #打印系统默认编码,pyhon3.X中没有decode

s = "你好"                #s默认编码类型为unicode，所以没有s.decode
print("gbk：",s.encode("gbk"),type(s.encode("gbk")))      #python3改变编码的同时也转化为bytes类型
print("utf-8:",s.encode("utf-8"),type(s.encode("utf-8")))
print("gb2312:",s.encode("utf-8").decode("utf-8").encode("gb2312"))     #因为gbk向下兼容gb2312

s_gbk = s.encode("gbk")
gbk_to_utf8 = s_gbk.decode("gbk").encode("utf_8")
print("utf-8:",gbk_to_utf8)