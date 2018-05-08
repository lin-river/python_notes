#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws


"""
data = open("yesterday",encoding = "utf-8").read()
print(data)
"""
#因为windows系统默认的编码格式为gbk，而之前我们设置python的默认编码格式为utf-8
#如果不用encoding指定编码格式，utf-8是处理不了gbk的

f = open("yesterday","r",encoding="utf-8")      #文件句柄（f包含文件的文件名，字符集，大小，硬盘上的起始位置）
#r = 只读模式，不写默认位r
print(f.readable())             #判断文件是否可读
print(f.writable())             #判断文件是否可写
first_read = f.read()
second_read = f.read()
print(first_read)
print("-------------second_reading---------------")
print(second_read)          #光标已在文件末，故读不出文字
f.close()               #文件关闭，程序借宿的时候也会自动关闭

#格式化读取
f = open("yesterday","r",encoding="utf-8")
print(f.readline())             #只读一行,适合读小文件，因为它将文件一次性的读到内存中
for i in range(5):              #读五行
    print(f.readline())

print(f.readlines())            #readlines将所有内容变成列表，每一行变成一个元素
f.close()
f = open("yesterday","r",encoding="utf-8")
for line in f.readlines():
    print(line.strip())         #strip去除每行后面的换行符，空格
print("-------------third_reading---------------")
f.close()
#遍历文件，不输出第十行
f = open("yesterday","r",encoding="utf-8")
for index,line in enumerate(f.readlines()):
    if index == 9:
        print("-----------------------------------------")
        continue
    print(line.strip())
f.close()
print("-------------fourth_reading---------------")

#可读取大文件的方法，高逼格
count = 0
f = open("yesterday","r",encoding="utf-8")
for line in f:                      #一行一行的读，内存里每次只存在一行，效率最高，因为此时f已变成一种迭代器
    count += 1
    if count == 10:
        print("--------------------------------------")
        continue
    print(line.strip())


#写文件
f1 = open("yesterday2","w",encoding="utf-8")        #W能写不能读
f1.write("ervery love story is beautiful\n")
f1.write("but ours is my favorite...\n")
f1.close()

#a = append 追加
f1 = open("yesterday2","a",encoding="utf-8")        #a不能读取
f1.write("每一个爱情故事都是是美丽的\n")
f1.write("但我们的故事是我最喜欢的...")
f1.close()

f = open("yesterday","r",encoding="utf-8")
print(f.tell())         #打印光标所在位置
print(f.read(7))        #只读7个字符
print(f.tell())
print(f.seekable())     #判断是否可读，是返回True，否则False
f.seek(0)               #光标重新定位指向（有些ttp终端文件无法重定向）1表示当前位置；2表示文件结尾。
print(f.tell())

print(f.fileno())       #	获得文件描述符，是一个数字
# 操作系统有一个专门的接口保存文件，python读文件并不是自己读的，而是去io列表内提取，该文件描述符为文件在列表内编号

print(f.isatty())       #如果文件是一个交互终端，则返回True，否则返回False。
print(f.name)           #打印文件名

print(f.flush())        #刷新缓存
#实时存进硬盘
f = open("yesterday2","r+",encoding="utf-8")
f.write("...........")
f.flush()

#运用flush打印进度条
import sys,time
for i in range(30):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.1)

print(f.closed)         #判断文件是否关闭
f.close()

f = open("yesterday2","r+",encoding="utf-8")
f.seek(20)
f.truncate(21)      # #把文件裁成规定的大小，默认的是从开头(seek没用)裁到当前文件操作标记的位置。
# 如果size比文件的大小还要大，依据系统的不同可能是不改变文件，
# 也可能是用0把文件补到相应的大小，也可能是以一些随机的内容加上去。

#二进制文件
f = open("yesterday2","wb")         #文本内还是字符，是以二进制编码的
f.write("hahahahahahaha".encode())
f.close()