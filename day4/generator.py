#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws

# 注意到yield是个表达式而不仅仅是个语句，所以可以使用x = yield r 这样的语法。

print("-------------列表生成式-------------")
a = [ i*2 for i in range(10)]           #i*2不仅可以是表达式，也可以是函数如func(i)
print(a)
#以上代码相当于如下，列表生成式的作用：使代码更简洁
a = []
for i in range(10):
    a.append(i*2)
print(a)

#在python3.X中，range(10)后
#3python2.X中，range(10)后得到的是[0,1,2,3,4,5,6,7,8,9],这些数据是直接占内存的

print("-------------列表生成器--------------")
generator1 = ( i*2 for i in range(10) )      #这就是一个列表生成器
print(generator1)           #根本没生成，只生成了一段地址，只是给你准备一个算法i*2,只有在调用的时候生成值

#print(generator1[5])        #'generator' object is not subscriptable,还未调用到generator[5],没有这个数据，所以会报错
for i in generator1:
    print(i)

print("-------------列表生成器特色----------------")
generator2 = ( i*2 for i in range(10) )
print(generator2.__next__())        #通过__next__()方法去取生成器中的内容
print(generator2.__next__())
print(generator2.__next__())
#注意：这些已经生成的数据调用后就已经被kill了，无法接着在调用
#生成器只能按部就班的一步一步走，不能返回，不能跳步
#一般用循环调用，不会这样一个一个__next__()，但进行超过生成器生成个数时，会报异常

print("-------------函数做列表生成器----------------")
#斐波那契数列(fibonacci)，用列表表达式写不出来，但是用函数把它打印出来却很容易：
def fib(max):                   #函数，一步执行到底
    x1,x2,x3 = 0,0,1
    while x1 < max:
        print(x3)
        x2,x3 = x3,x2+x3        #相当于t = (x3,x2+x3),t是一个tuple，x2 = t[0],x3 = t[1]
        x1 = x1+1
    return 'done'
fib(10)
print("------------以上是一个打印斐波那契数列的函数，接下来要转化为生成器-------------")
def fib1(max):               #
    x1,x2,x3 = 0,0,1
    while x1 < max:
        yield x3               #此处做了修改，有yeild的存在，变成一个生成器了，返回当前状态的值
        x2,x3 = x3,x2+x3
        x1 = x1+1
    return 'done'             #变成生成器之后在出错的时候返回，StopIteration done
print(fib1(10))              #<generator object fib at 0x0000000925E601A8>发现函数变成生成器了
fib1_generator = fib1(10)
print(fib1_generator.__next__())         #变成生成器之后，函数进行一步之后暂停
print("--------其他操作----------")          #中间可进行其他操作，等到下面的for循环继续进行
for i in fib1_generator:
    print(i)

print("-------------列表生成器底线报错设置----------------")
def fib2(max):
    x1,x2,x3 = 0,0,1
    while x1 < max:
        yield x3
        x2,x3 = x3,x2+x3
        x1 = x1+1

fib2_generator = fib2(6)
#抓代码
while True:
    try:
        x = next(fib2_generator)             #next()内置函数，和__next__()一样，回到上一次函数中断的位置
        print("fib2_generator : ",x)
    except StopIteration as e:              #若出的是这个错，执行下列操作，e是自己给异常起的名字
        print("Generator return value : ", e.value)
        break