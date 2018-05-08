#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

from gevent import monkey						# 如果没有这个补丁，以下内容执行起来还是串行(因为有些模块，gevent无法识别是否为IO)
import gevent
from  urllib.request import urlopen

monkey.patch_all()								# 把当前程序的所有IO操作给我单独做上标记

def f(url):
	print('GET: %s' % url)
	resp = urlopen(url)
	data = resp.read()
	print('%d bytes received from %s.' % (len(data), url))


gevent.joinall([
	gevent.spawn(f, 'https://www.python.org/'),
	gevent.spawn(f, 'https://www.yahoo.com/'),
	gevent.spawn(f, 'https://github.com/'),
])