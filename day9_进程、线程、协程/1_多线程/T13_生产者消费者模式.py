#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import queue,threading,time

q = queue.Queue(maxsize=10)


# 供大于求：
# def Producer():
# 	count = 1
# 	while True:
# 		q.put("骨头 %s" % count)
# 		print("生产了骨头 %s" % count)
# 		count += 1
#
# def Consumer(name ):
# 	while True:
# 		print( "[%s] 取到了 %s" % ( name,q.get() ) )
# 		time.sleep(1)
#
# P1 = threading.Thread( target= Producer )
# C1 = threading.Thread( target= Consumer, args=("消费者1",) )
#
# P1.start()
# C1.start()



# 求大于供：
def Producer():
	count = 1
	while True:
		q.put("骨头 %s" % count)
		print("生产了骨头 %s" % count)
		count += 1
		time.sleep(2)

def Consumer(name ):
	while True:
		print( "[%s] 取到了 %s" % ( name,q.get() ) )
		time.sleep(1)

P1 = threading.Thread( target= Producer )
C1 = threading.Thread( target= Consumer, args=("消费者1",) )
C2 = threading.Thread( target=Consumer, args=("消费者2",) )

P1.start()
C1.start()
C2.start()