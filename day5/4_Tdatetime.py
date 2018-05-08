#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws
import time
import datetime                 #时间加减
datetime.datetime.now()   #在DOS界面显示：datetime.datetime(2017, 11, 14, 14, 12, 54, 116465)
print(datetime.datetime.now()) #获取当前时间，返回 2016-08-19 12:47:03.941925
print(datetime.date.fromtimestamp(time.time()) )  # 时间戳直接转成日期格式 2016-08-19
print(datetime.datetime.now() )

print("--------------------timedelta(无法单独存在，必须和datetime.now()连用)-----------------------")
print(datetime.datetime.now() + datetime.timedelta(3)) #当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(-3)) #当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(hours=3)) #当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(minutes=30)) #当前时间+30分


#
# c_time  = datetime.datetime.now()
# print(c_time.replace(minute=3,hour=2)) #时间替换