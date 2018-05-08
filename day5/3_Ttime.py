#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws

import time

print("------------------时间戳--------------------")
print(time.time(),"(s) = nowtime - 1970.01.01 ")         #获取时间戳，单位为秒
#1970年1月1日到现在之后的秒，不同时刻的时间戳不一样
x = time.time()

#验证：
def time_swap(x):
    print( "转换成年：",x/3600/24/365)
    print("nowtime_year - 1970 = ",x/3600/24//365,"(years)")
    print("nowtime_day - 1970.01.o1 = ", x / 3600 // 24,"(days)")
    print("转化为小时：",x/3600)
time_swap(x)

# 将结构化的时间转化为时间戳
print( "将本地时间转为时间戳形式：",time.mktime(time.localtime()))

print( time.ctime())        #一个时间戳参数，将时间戳转化为Tue Nov 14 14:00:46 2017格式

print( "-----------------格式化时间--------------------")
#
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))      #两个参数，一个是自定义的格式，一个是结构化的时间


print( "-----------------结构化时间（元组）--------------------")
print(time.localtime())     #有一个参数为时间戳，若不传入时间戳，默认打印本地时间时间
# time.struct_time(tm_year=2017, tm_mon=11, tm_mday=9, tm_hour=18, tm_min=46, tm_sec=21, tm_wday=3(一周的第几天), tm_yday=313（一年的第几天）, tm_isdst=0（时区，是否为夏令时，0代表不是，1代表是）)

print(time.gmtime())        #有一个参数为时间戳，若不传入时间戳，默认打印（UTC）世界标准时间
# time.struct_time(tm_year=2017, tm_mon=11, tm_mday=9, tm_hour=11, tm_min=19, tm_sec=19, tm_wday=3, tm_yday=313, tm_isdst=0)

#strptime(string, format)
print(time.strptime("2017-11-09 19:53:41","%Y-%m-%d %H:%M:%S"))     #两个字符串参数，第一个是格式化时间，第二个是格式化时间的格式，将格式化的时间转化为结构化的时间
# strptime(string, format)

print( time.asctime() )      #一个元组参数，将元组结构时间转化为字符串，按%a %b %d %H %M %S %Y的格式转化

print( "-------------------time----------------------")
print(time.timezone)        #本地时区与世界标准时间的时间差
print("转化为小时：",time.timezone / 3600)
print(time.altzone)         #本地时间和夏令时的时间差
print("转化为小时：",time.altzone / 3600)
print( "你是否使用了夏令时，0为否，1为是,now:",time.daylight)
print( "睡几秒：",time.sleep(2),"zzzzzzz")      #先调用sleep（2），再返回none，再打印print



print( "-----------------从元组格式时间获取内容-------------------")
t = time.localtime()
print(t)
print( "年：",t.tm_year,t[1])     #
#随便拿到一个时间戳我们对其进行处理
t2 = time.localtime(1234567890)
print(t2)
print( "this is 1973 day : %d" %t2.tm_yday)

#help(time)

run_time = time.time()
time.sleep(2)
end_time = time.time()
print(  end_time - run_time  )