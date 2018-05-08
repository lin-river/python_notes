#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

x = input()
n = len(x)
y = []
sum = 0
for i in range(0,n):
    y.append(x[n - 1 - i])
for i in range(1,n+1):
    sum += int(y[i-1])*(pow(10,n-i))
y = int(x)+sum
print(y)