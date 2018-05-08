#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws
"""import sys

print(sys.path)         #打印环境变量
print(sys.argv)         #打印相对路径地址，但是因为pycharm调用的时候写的这个脚本的名字就是绝对路径，
                        # 所以在pycharm里会打印绝对路径，若用的命令行则会打印相对路径"""
import os
#os.system("dir")        #调用系统命令，直接输出，不能保存结果
cmd_res = os.popen("dir")
cmd_read = os.popen("dir").read()

print(cmd_res)
print("-->",cmd_read)

os.mkdir("new_dir")     #在当前路径下创建一个新的目录名为"new_dir"
""""""
