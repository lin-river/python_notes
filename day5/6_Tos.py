#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = Hero lws
import os

print( "---------------------------------查看路径和文件--------------------------------")
print( os.getcwd() )		#绝对路径：获取当前工作目录，即当前python脚本工作的目录路径
#在命令行结果为'C:\\Users\\Herolh\\Desktop\\news\\oldman\\day5'
#注意为双斜杠

print( '--os.chdir("dirname")	:	改变当前脚本工作目录；相当于shell下cd')
os.chdir("C:\\")		#双斜杠，否则报错
print( os.getcwd() )
os.chdir( r'C:\Users\Herolh\Desktop\news\oldman\day5')		#原始字符串
print( os.getcwd() )

print( "--# os.curdir  返回当前目录: ('.')  是一个属性不是一个方法" )
print( os.curdir )

print( "--# os.pardir  上一级目录，获取当前目录的父目录字符串名：('..')" )
print( os.pardir )

print( "--# os.listdir('dirname')    列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印")
print( os.listdir(r"C:\Users\Herolh\Desktop\news\oldman") )
print( os.listdir( os.curdir ) )		#打印当前路径所有文件和子目录  = print( os.listdir( '.' ) )
print( os.listdir( os.pardir ) )		#打印上一目录的所有文件和子目录 = print( os.listdir( '..' ) )

print( "--# os.stat('path/filename')  获取文件/目录信息")
print( os.stat( r"C:\Users\Herolh\Desktop\news\oldman\test" ) )			#返回文件夹信息
print( os.stat( r"C:\Users\Herolh\Desktop\news\oldman\day5\Tos.py" ) )	#返回文件信息

print( "--# os.environ  获取系统环境变量 ")
print( os.environ )

print("------------------------------创建和删除目录和文件-------------------------------")

print( "--# os.makedirs('dirname1/dirname2')    可生成多层递归目录,即使目录不存在，也会给你递归的创建出来")
# os.makedirs(r"C:\Users\Herolh\Desktop\news\oldman\test\a\b\c\d")

print( "--# os.removedirs('dirname1')    若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推")
# os.removedirs( r"C:\Users\Herolh\Desktop\news\oldman\test\a\b\c\d")

print( "--# os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname")
# #os.mkdir( r"C:\Users\Herolh\Desktop\news\oldman\test\a\" )	#报错，因为创建的是一个多级目录
# os.mkdir( r"C:\Users\Herolh\Desktop\news\oldman\test" )
# os.mkdir( r"C:\Users\Herolh\Desktop\news\oldman\test\a" )

print( "--# os.rmdir('dirname')    删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname")
# os.rmdir( r"C:\Users\Herolh\Desktop\news\oldman\test")		#报错，因为test不为空
# os.rmdir( r"C:\Users\Herolh\Desktop\news\oldman\test\a")

print( "--# os.remove()  删除一个文件")
# os.remove( r"C:\Users\Herolh\Desktop\news\oldman\test\1.txt" )	#不能删除文件夹

print("---------------------------------修改目录和文件----------------------------------")
print( '--# os.rename("oldname_path","newname_path")  重命名文件/目录')
# os.rename(r"C:\Users\Herolh\Desktop\news\oldman\test\old.txt",r"C:\Users\Herolh\Desktop\news\oldman\test\new.txt")

print("---------------------------------不同平台兼容性----------------------------------")
print( '--# os.sep    输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"')
print( os.sep )		#在Ddos界面显示为\\

print( r'--# os.linesep    输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"')
print( os.linesep )

print( "--# os.pathsep    输出用于分割文件路径的字符串")
print( os.pathsep )			#windows系统的分隔符为顿号";"，linux系统的分隔符为冒号":"

print( "--# os.name    输出字符串指示当前使用平台。win->'nt'; Linux->'posix'")
print( os.name )

print("---------------------------------执行shell命令----------------------------------")
# print( '--# os.system("bash command")  运行shell命令，直接显示，无法保存为字符串')
# os.system( "dir")

print( '--# os.popen("bash command")  运行shell命令，不直接显示，可以保存为字符串')
str1 = os.popen( "dir").read()
print( str1)		#linux的话可以直接print( os.popen("bash command") )


print( "----------------------------------os.path-----------------------------------")
print("--# os.path.abspath(path)  返回path规范化的绝对路径")
print( os.path.abspath(__file__) )		#当前文件的绝对路径

print("--# os.path.split(path)  将path分割成目录和文件名,以元组返回，路径本身可以不存在")
print( os.path.split( r"w:\test\a\b\t.txt") )
print( os.path.split(r"C:\Users\Herolh\Desktop\news\oldman\day5\Tos.py"))
print( os.path.split(__file__) )	#两个返回不一样，在于文件分割符

print( "--# os.path.dirname(path)  返回path的目录。其实就是os.path.split(path)的第一个元素")
print( os.path.dirname( r"w:\test\a\b\t.txt") )		#路径本身可以不存在
print( os.path.dirname(__file__) )

print( '--# os.path.basename(path)  返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素')
print( os.path.basename(r"w:\test\a\b\t.txt") )
print( os.path.basename(__file__) )

print("--------------存在与否-----------------")
print( '--# os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False')
print( os.path.exists(__file__) )
print( os.path.exists( r"w:\test\a\b\t.txt"))

print( '--# os.path.isabs(path)  如果path是绝对路径，返回True,无法检验路径是否正确')
print( os.path.isabs(__file__))
print( os.path.isabs(r"w:\test\a\b\t.txt") )
print( os.path.isabs(r"\test\a\b") )		#linux是以/为根目录，故可行
print( os.path.isabs(r"test\a\b") )

print( "--# os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False")
print( os.path.isdir( r"w:\test\a\b" ))
print( os.path.isdir(__file__))		#w文件名不行
print( os.path.isdir( r"C:\Users\Herolh\Desktop\news\oldman\day5\Tos.py"))
print( os.path.isdir( r"C:\Users\Herolh\Desktop\news\oldman\day5"))

print('--# os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False')
print( os.path.isfile(__file__) )
print( os.path.exists( r"w:\test\a\b\t.txt"))
print( os.path.exists( r"C:\Users\Herolh\Desktop\news\oldman\day5\Tos.py"))

print( "--# os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略")
print( os.path.join(r'C:',r"\a") )
print( os.path.join(r'C:',r'/a',r"/b") )		#linux下是可行的，会输出C:/a/b

print( "--# os.path.getatime(path)  返回path所指向的文件或者目录的最后存取时间,返回时间戳")
print(	os.path.getatime(__file__))
import time
print( time.ctime( os.path.getatime(__file__) ) )

print( "--# os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间")
print(	os.path.getmtime(__file__))
print( time.ctime( os.path.getmtime(__file__) ) )