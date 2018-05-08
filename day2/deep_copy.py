#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"
import copy
names = ["zao","qian","sun",[1,2],"li","hahaha"]
names2 = copy.copy(names)               #这样还是浅层copy
names2 = copy.deepcopy(names)           #这样才是深层copy
names[3][0] = 0
print(names,"\n",names2)
#三种浅copy的方法：
person = ["name",["a",100]]
p1 = copy.copy(person)
p2 = person[:]
p3 = list(person)
print(person,p1,p2,p3)