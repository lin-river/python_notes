#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __Author__: Hero lws

def change_name(name):
    print("before change ",name)
    name = "Lin"                    #局部变量，只在函数内(作用域)生效
    print("after change ",name)

name = "lin"                        #全局变量，在整个程序中都生效的
change_name(name)
print(name)

#局部变量上位成全局变量
age = 18
def change_age():
    global age                  #将局部变量上升到全局变量//不要在函数内改局部变量，会被开除
    age = 19
    print("函数调用之后：")
print(age)                      #因为函数还没调用，所以还是全局变量的值
change_age()
print(age)

print("--------开除示范---------")
def change_sex():
    global sex                  #外面没有全局变量，在函数内定义全局变量，作死，出bug不好调试，直接开除
    sex = "man"
    print("函数调用之后：")
#print(sex)                      #因为函数还没调用，没有全局变量所以会报错
change_sex()
print(sex)

#全局只有字符串和单独的整数在函数内是无法修改的
# 列表，字典，集合在函数内修改全局也会修改
names = ["zao","qian","sun","li"]
def namelist():
    names[0] = "lin"
namelist()
print(names)

print("-----局部变量和全局变量的访问顺序-------")
x = 0
def grandpa():
    x = 1
    def dad():
        x = 2
        def son():
            x = 3
            print("The son is :",x)
        print("The dad is :",x)
        son()
    print("The granda is :",x)
    dad()       #如果没有这一步的调用，son()函数内的内容也不会执行

grandpa()