#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws

#f = open("yesterday","r",encoding = "utf-8")       等于：
with open("yesterday","r",encoding = "utf-8") as f:
    print(f.readline())
    for line in f:
        print(line.strip())
#不需要f.close,因为with执行完后自动关闭文件

with open("yesterday","r",encoding = "utf-8") as f ,\
        open("yesterday2", "r", encoding = "utf-8") as f2:          #python官方建议一行不要超出80个字符
    print(f2.readline())
    for line in f:
        print(line.strip())