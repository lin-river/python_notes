#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = Hero lws

import configparser		#在python3.X为configparser，在python2.X为ConfigParser
# 用于生成和修改常见配置文档
print( "-------------------生成配置文件--------------------")
config = configparser.ConfigParser()		#生成一个configparser对象
config["DEFAULT"] = {"ServerAliveInterval":"45",
					 "Compression":"yes",
					 "CompressionLevel":"9",
					 "ForwardX11":"yes"}

config["bitbucket.org"] = {}		#可以先写为空，下面再填
config["bitbucket.org"]["User"] = 'hg'

config["topsecret.server.com"] = {}
topsecret = config["topsecret.server.com"]		#相当于取了一个别名
topsecret["Host Port"] = "50022"
topsecret["ForwardX11"] = 'no'

with open("Tconfigparser.ini","w") as configfile:
	config.write( configfile )

print( "-------------------读取配置文件--------------------")
conf = configparser.ConfigParser()		#生成一个configparser对象
conf.read("Tconfigparser.ini")		#将配置文件写入对象

print( conf.defaults() )	#打印["DEFAULT"]内容
print( conf.sections() )	#打印除["DEFAULT"]外所有节点，不包含内容（列表）

#打印节点内容：
print( conf["bitbucket.org"]["User"] )


print( "-------------------修改配置文件--------------------")
# sec = conf.remove_section('bitbucket.org')		#删除节点
# conf.write(open('Tconfigparser.change', "w"))		#修改完记得写回去

# sec = config.has_section('bitbucket.org')				#判断是否存在节点
# print( sec )

# sec = conf.add_section('bitbucket.org')			#写入节点
# conf.write(open('Tconfigparser.change', "w"))

# conf.set('bitbucket.org','conf',"1")				#添加节点下配置
# conf.write(open('Tconfigparser.change', "w"))

conf.remove_option('bitbucket.org','conf')		#删除节点下配置
conf.write(open('Tconfigparser.change', "w"))
