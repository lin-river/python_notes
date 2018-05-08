#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws

list_1 = [1,2,3,9,9,7,7,4,5]            #创建列表
list_2 = [122,3432,342,2,4,31,6,7]
list_1 = set(list_1)                    #将列表转化为集合
list_2 = set(list_2)

print(list_1,type(list_1))                  #集合是无序的，不支持索引，list_1[1]会报错
print("两个集合的交集:",list_1.intersection(list_2))          #求两个集合的交集   法一
a = list_2 & list_1                         #法二
print("两个集合的交集:",a)

print("两个集合的并集:",list_1.union(list_2))                 #求两个集合的并集   法一
b = list_1 | list_2                         #法二
print("两个集合的并集:",b)

print("两个集合的差集:",list_1.difference(list_2))            #求差集，list_1有list_2没有的
c = list_1 - list_2
print("两个集合的差集:",c)

list_3 = set([1,3,5])
print("判断list_3是不是list_1的子集:",list_3.issubset(list_1))              #判断list_3是不是list_1的子集

print("对称差集：",list_1.symmetric_difference(list_2))  #对称差集，不包含list_1和list_2交集的所有项
d = list_1 ^ list_2
print("对称差集：",d)

list_4 = set([2,4,6])
print(list_3.isdisjoint(list_4))        #若两个集合没有交集，返回True

#集合的增删改查（集合中没有插入，insert，只有添加add）
list_3.add(666)             #添加一项
list_4.update([666,777,888])  #添加多项
print(list_3,list_4)

list_4.remove(666)          #删除一项，若没有该项，则报错
list_4.discard(999)                 #删除一项，若不项存在，不做任何操作
print(list_4,"现长度为：",len(list_4))

print(list_4.pop())                #随机删除，并返回删除的项
print(list_4)