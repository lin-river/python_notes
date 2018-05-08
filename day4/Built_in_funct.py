#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws
print("------------------# 内置函数 #-------------------")
#python程序一启动，就能调用的函数
print( "abs(-12)",abs(-12) )             #abs()取绝对值
print( "all([-1,0,2,3]):",all([-1,0,2,3]) )    #若参数全为真(非零即为真)，返回True，否则返回False
print( "all()当数据为空时，没有一个假，即为真：",all([]) )
print( "any([0,0,1,-1]):",any( [0,0,1,-1] ) )     #只要有一个数据为真则返回True，否则返回False
print( "any([])当数据为空时，没有一个真，返回假:",any( [] ) )
ascii = ascii( [1,2,"将整个列表转化为可打印的字符串形式"])
print("ascii():",type(ascii),"\n",[ascii] )        #注意[ascii]的引号

print("------------------ b -------------------")
print("bin()的作用是将数值变为二进制:",bin(1),bin(8),bin(255))          #字符串不行
print("bool()的作用是判断真假：",bool(0),bool([]),bool([2]),bool("True"))
byte = bytes( "abcde",encoding = "utf-8" )
print( "byte()生成字节格式：",byte.capitalize(),byte )
#byte[0] = "A" #和字符串一样，字节格式也不能修改    b'Abcde' b'abcde'
byte2 = bytearray("abcde",encoding = "utf-8" )
#byte2[0] = "A"                 #TypeError: an integer is required 不能直接赋值字符串
byte2[0] = 65                  #需要将其转化为数值形式才可
print(byte2[0],byte2)           #65 bytearray

print("------------------ c -------------------")
def func():pass
print( "callable()判断是否可调用：",callable([]),callable(func()),callable(func) )
#判断是否可调用，如函数，类（带括号的即为可调用）

print( "chr()的作用：将数字对应的ascii码打印出来，chr(97) = ",chr(97))  #chr()内必须为数字
print( "ord()的作用：将字符在ascii码表对应的数字打印出来，ord('a') = ",ord('a'))  #chr()内必须为数字

#classmethod : 类方法      内置函数，以后单独讲

#complie ： 编译，汇编
code = "for i in range(10):print(i)"        #code如今是一个字符串
print( compile(code,"","exec") )         #exec : 执行以string类型存储的python代码
#以上将字符串转化为一个pyobject对象
c = compile(code,"","exec")
exec( c )     #执行被编译的代码


code = "1+3/2*6"        #code是一句表达式
print( compile(code , "", "eval") )
c = compile(code , "", "eval")      #eval()将字符串变成字典,将字符串str内的简单数据类型或简单运算当成有效的表达式来求值并返回计算结果,
print( eval(c) )    # 执行被编译的代码

compile( code,"","exec")       #""内应该是一个文件名，当发生错误的时候，将错误打到“file_name”中
                                # 但这个实际应用情况并不太好用，所以放空即可
#相当于import的功能，但compile可以实现一种动态导入的功能


print("------------------ d -------------------")
print( "dict() :生成一个为空的字典 ",dict() )
print( " dir() : 查看可以调用的方法 ： ",dir({}))
#两个下划线的为内部方法我们不能用
print( "divmod() :输入的两个参数相除，返回商和余数",divmod(5,2),divmod(5,1))

print("------------------ e -------------------")
exec( "print('helloworld')")    #exec : 执行以string类型存储的python代码

print("------------------ f -------------------")
#filter(func，值) : 在一组数据中过滤出你想要的来
res = filter(lambda n : n>5 ,range(10) )
for i in res:
    print(i)
print( "将range()里的数提取出来放到lambda的n中，过滤出来符合条件的形成一个新的迭代器，并返回这个迭代器")

#frozenset 将可修改的集合变为不可修改
a = set([1,12,3,4,5,1,23,4])
print( a )      #{1, 3, 4, 5, 12, 23}
a = frozenset([1,12,3,4,5,1,23,4])
print( a )      #frozenset({1, 3, 4, 5, 12, 23})

print( "-------------- g ---------------------")
print( globals() )
#返回当前程序文件内所有的变量，将其深层为一个字典，其变量名为键，变量值为值

print( "-------------- h ---------------------")
#hash() : 建立映射关系
print( "hash(1) : 输入一个数字，该值永远唯一，故不变",hash(1))
print( "hash( 'hahahahaha...') : 生成映射标识且永远不变 ：",hash( 'hahahahaha...') )

#help()

#hex()
print( "hex() : 把一个数字转成十六进制 " ,hex(16) )

print( "-------------- i ---------------------")
print( "id() : 打印内存地址", id( [] ))

print( "-------------- i ---------------------")
#local()
def localtest():
    local_var = 1234
    print( locals() )   #打印该函数内的变量及变量值（局部变量）
    print( globals().get( local_var))   #即使在函数内部使用globals()也不能查找到局部变量

print(globals())            #打印所有变量，但是没有local_var，因为它为局部变量
print( globals().get("local_var"))      #直接在globals()里get获取local_var，没有返回None

localtest()

print( "-------------- m ---------------------")
#将range()里的数提取出来放到lambda的n中，每一个值都用func内的方式进行处理，并形成一个新的迭代器，并返回这个迭代器
res2 = map( lambda n : n*n,range(10) )      #将range()里的数提取出来放到lambda的n中，
for i in res2:
    print(i)
print( "将range()里的数提取出来放到lambda的n中，每一个值都用func内的方式进行处理，并形成一个新的迭代器，并返回这个迭代器")

print( "-------------- o ---------------------")
print( "oct() : 将十进制转化为八进制 ", oct(8))

print( "-------------- p ---------------------")
print( "pow(2,3) : 2的3次幂", pow(2,3))

print( "-------------- r ---------------------")
c = int(12345)
print( "repr() : 转化为字符串对象 ",repr(c),type( repr(c) ) )

#round()保留几位小数,默认保留一位小数
print( round(1,2345) , round(1.2345,2) )

print( "-------------- s ---------------------")
#slice()切片
a = range(20)
a[ slice(2,5)]
print( a)
print( a[ slice(2,5)])

#sorted()会给字典的key排序
a = { 2:8,4:3,7:8,2:6,5:5}
print( a )
print( sorted(a))   #[2, 4, 5, 7, 9]
print( sorted( a.items() ) )     #[(2, 1), (4, 3), (5, 5), (7, 6), (9, 8)]
#若想以value来排序，则又要用到lambda
print( sorted( a.items() ,key = lambda x:x[1] ) )
#先进行a.items()获取到每一个元素：[(2, 6), (4, 3), (5, 5), (7, 8)]
#lambda x:x[1] 的x = a.items()中的每个元素

print( "-------------- z ---------------------")
a = [1,2,3,4]
b = ["a","b","c","d"]
for i in zip(a,b):      #zip：拉链  将两列表内的数据一一对应，并生成一个迭代器
    print(i)
#如果两个列表不一样长，那么将会按照最短的列表来进行组合

print( "-------------- __hahaha__ ---------------------")
import math     #原本应该是像这样包含一个变量名的
__import__('math')      #用这个可以包含一个字符串
