#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws

name = input("name:");print(type(name))
age = int(input("age:"));print(type(age))               #进行强制类型转换，str——>int
job = input("job:");print(type(job))
salary = input("salary:");print(type(salary))
#type()检测变量类型，结果显示如果不进行强制类型转换，四个变量全为字符型

information = """
-- Personal information --
name:%s  
age:%d
job:%s
salary:%s
""" % (name,age,job,salary)                             #也可以在调用的时候进行类型转换

information2 = """
-- Personal information2 --
name:{_name}
age:{_age}
job:{_job}
salary:{_salary}
""".format(_name = name,
           _age = age,
           _job = job,
           _salary = salary)

information3 = """
-- Personal information3 --
name:{0}
age:{1}
job:{2}
salary:{3}
""".format(name,age,job,salary)

print(information)
print(information2)
print(information3)