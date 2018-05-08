#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws
names = ["lin","zao","qian","sun","li"]

"""
print(names[1:3])
print(names[-0])
print(names[-3:-1])       #不包含-1
print(names[:3])          #如果是从头开始取，0可以忽略，跟上句效果一样
print(names[3:])          #如果想取到最后一个，就不能写-1，只能这么写
print(names[-2:])
print(names[::2])        #后面的2是代表每隔一个元素，就取一个
"""

names.append("jian")        #列表后追加一个值
names.insert(1,"he")        #列表中插入一个值
names[6] = "ren"            #修改列表中一个值
#delete(有以下三种方法)
names.remove("ren")         #直接写值
del names[0]
names.pop()                 #没有参数默认删除列表最后一个值，names.pop(0) = del names[0]

print(names.index("he"))    #查找值在哪个位置
print(names[names.index("he")])

names.reverse()              #列表翻转
#names.clear()               #清空整个列表
names.sort()                 #列表排序(此处按首字母ASCII码排序）
print(names)
names2 = [1,2,3,4]
names = [4,5,6,7]
names2.extend(names)
names[3] = [6.1,6.2,6.3]
names[3][2] = 7              #二层修改
print(names2,names)