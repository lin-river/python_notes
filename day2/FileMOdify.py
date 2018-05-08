#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws

f = open("yesterday","r",encoding = "utf-8")
f_new = open("yesterday.bak","w",encoding = "utf-8")

for line in f:
    if "肆意的快乐等我享受" in line:
        line = line.replace("肆意的快乐等我享受","肆意的快乐等爸爸我去享受")
    f_new.write(line)
f.close()
f_new.close()

