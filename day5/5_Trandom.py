#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws
import random
print(random.random())		#随机[0,1)内的浮点值，不能再指定区间
print( random.uniform(1,3) )	#可指定区间，随机浮点值
print(random.randint(1,3))		#[1,3]内随机整数（包含1和3）
print(random.randrange(1,3))	#[1,3)内随机整数（不包含3）

print('----------choice----------')
print( random.choice("hello!") )	#随机抽取序列值
print( random.choice([1,2,3,4,5]))

print( random.sample('hello!',2))		#S随机抽取num个值，以列表形式打印


print('----------洗牌功能----------')
l = [1,2,3,4,5,6,7];print('原：',l)
random.shuffle(l)
print(l)

print('----------简单四位数字验证码-------------')
checkcode = ''
for i in range(4):
	current = random.randint(1,9)
	checkcode += str(current)
print(checkcode)


print( '----------------随机字母数字四位验证码---------------------')
checkcode2 = ''
for i in range(4):
	current2 = random.randrange(0,4)
	# 字母
	if current2 == i:
		change1 = random.randint(1,2)
		if change1 == 1:
			tmp = chr( random.randint(65,90) )		#大写字母
		else:
			tmp = chr( random.randint(97,122) )		#小写字母
	#数字
	else:
		tmp = random.randint(0,9)					#数字

	checkcode2 += str(tmp)
print( checkcode2 )