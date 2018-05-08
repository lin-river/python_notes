#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws
name = "\thello world!"
print(name.capitalize())        #首字母大写
print(name.count("l"))          #统计选定字符串出现的次数
print(name.center(50,"-"))      #打印50个字符，不够用选定字符串补上，把name放在中间
print(name.ljust(50,"*"))       #保证宽度，当宽度不够数时，在左侧填充name，右侧填充字符串
print(name.rjust(50,"*"))       #保证宽度，当宽度不够数时，在右侧填充name
print(name.endswith("!"))       #判断是否以选定字符串结尾，是返回TRue（可打印），否则返回false，switch：快速地
print(name.expandtabs(tabsize = 30))    #将字符串中的tab宽度转换成指定宽度 expend：扩展地
print(name.find("l"))
print(name.find("world"))       #查找字符串并返回首字母序列，若有多个则返回第一个字符串首字母的序列值
print(name[name.find("world"):12])      #字符串也可以用来切片
print("hello world".rfind("l"))           #从右往左找到字符串并打印序列值
names = "my name is {name} and I am {age} years old"
print(names.format(name = "lin",age = "18"))          #format：格式
print(names.format_map( {"name" : "lin","age": 12 } ))
print("ab123\t".isalnum())      #当字符串包含特殊字符时返回False,只有当字符串只包含26个字母和阿拉伯数字时返回True
print("abA".isalpha())          #但字符串只有字母时返回True
print("1A".isdecimal())         #检查是否由十进制字符组成，是返回True       #decimal 小数的；十进位的
print("1.23".isdigit())         #检查是否是一个整数,digit : 数字，手指
print("a中文1A".isidentifier())      #判断是否是一个合法的变量名     #identifier ：标识符
print("33".isnumeric())         #检测变量是否为数字或数字字符串,是返回True，小数或其他进制数也会返回False
print("     A".isspace())       #检测是否全为空格，是则返回True
print("This Is A Title".istitle())      #检测每个单词首字母是否大写，是返回True
print(name.isprintable())        #判断是否为可打印字符串(不包含转义字符)，是则返回True，
                                 # 只有在tty文件（设备终端，驱动文件等）这类的文件不能打印的
                                 # 字符串根本不需要考虑这个问题
print("Th\t".isupper())         #判断所有字符（不包含转义字符）是否全为大写，是返回True
print("".join( ["1","2","3","4"]),
      "+".join( ["1","2","3","4"]))
                                #将join项目中的项目转化为字符串，并用str里的字符将将其连接起来
print("我\tLOWER".lower())     #将所有字母变成小写,有其他字符不变
print("upper".upper())         #将所有字母变成大写
print("\n\t\n  \\my name is\\ \n\t\n".strip())      #去掉字符串两头的\n,\t,空格
print("\n\n  \t\\name\n".lstrip())     #去掉左侧的换行符,tab和空格
print("name\\\n\t    \n".rstrip())     #去掉右侧的换行符,tab和空格
p = name.maketrans("abcdefg","1234567")
print(name.translate(p))        #str.maketrans(intab, outtab)用于创建字符映射的转换表
    # 对于接受两个参数的最简单的调用方式，第一个参数intab是字符串，表示需要转换的字符
    # 第二个参数outtab也是字符串表示转换的目标。
    #注意两个字符串的长度必须相同，为一一对应的关系。
print("hello world!".replace("l","L",2))         #用L替换l，替换两次
str1 = "this is string example....wow!!!"
str2 = "is"
print(str1.rindex(str2))           #返回子字符串 str 在字符串中最后出现的位置
            # 如果没有匹配的字符串会报异常，你可以指定可选参数[beg:end]设置查找的区间。
print(str1.index(str2))             #检测字符串中是否包含子字符串 strd
            # 如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内
            #该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
print("1+2+3+4".split("+"))         #将字符串以“+”为分隔组成列表，默认以空格为分隔
print("1+2+3+\n+4".splitlines())    #将字符串以换行为分隔组成列表，linux和win的换行是不一样的，自动识别
print("Hello World".swapcase())     #大小写互相切换
print("hello world".zfill(15))      #返回指定长度的字符串，原字符串右对齐，前面填充0
                                      # 当指定长度小于原字符串时，直接打印原字符串