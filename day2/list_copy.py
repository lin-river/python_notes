#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws
names = ["zao","qian","sun",[1,2],"li","hahaha"]
names2 = names.copy()   #只能进行浅层复制

names[3][0] = 0         #第二层的相当于只是一个链接放在第一层的列表内，
                        # 所以当names改了之后，copy后的names2也能随之改变
                        #这时候当你再去改names2的第二层列表时，names的第二层也随之改变

names[2] = "Sun"
print(names,"\n",names2)
names2[3][0] = 1
print(names,"\n",names2)

