#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import queue

# class queue.PriorityQueue(maxsize=0) #存储数据时可设置优先级的队列
# 排序越小按优先级越高
q = queue.PriorityQueue()

q.put( (-1,"zao") )
q.put( (3,"qian") )
q.put( (10,"shun") )
q.put( (6,"li") )

print( q.get() )
print( q.get() )
print( q.get() )