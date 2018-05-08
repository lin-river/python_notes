#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import queue

q = queue.LifoQueue()

q.put("connect1")
q.put("connect2")
q.put("connect3")
print( q.qsize() )

print( q.get() )
print( q.get() )
print( q.get() )