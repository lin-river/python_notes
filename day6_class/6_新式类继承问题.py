#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

class A:
	def __init__(self):
		print( "A")

class B(A):
	pass
	# def __init__(self):
	# 	print( "B")

class C(A):
	pass
	# def __init__(self):
	# 	print( "C")

class D(B,C):
	pass
	# def __init__(self):
	# 	print( "D")

obj = D()