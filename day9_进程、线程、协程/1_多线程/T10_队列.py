#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"



import  queue
# 在python2.X里为import Queue

q = queue.Queue()
# class queue.Queue(maxsize=0) #先入先出

# Queue.put(item, block=True, timeout=None)			block = True 默认取不到值就阻塞卡住，timeout = 阻塞等待时间
q.put("connect1")
q.put("connect2")
q.put("connect3")
print( q.qsize() )

# Queue.get(block=True, timeout=None)
print( q.get() )
print( q.get() )
print( q.get() )

print( q.get_nowait() )		# 马上取出来，如果队列为空就会抛出queue.Empty异常
# print( q.get() )			# 没有内容就卡在那了，等待新的内容进入队列q
