#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = Hero lws

# xml是实现不同语言或程序之间进行数据交换的协议，跟json差不多，但json使用起来更简单，
# 不过，古时候，在json还没诞生的黑暗年代，大家只能选择用xml呀，至今很多传统公司如金融行业的很多系统的接口还主要是xml。
# xml的格式如下，就是通过<>节点来区别数据结构的:

# <?xml version="1.0"?>			#版本号
# <data>			#data下包含三组数据，data可随意更改，如写成<lin></lin>
#     <country name="Liechtenstein">
#         <rank updated="yes">2</rank>
#         <year>2008</year>
#         <gdppc>141100</gdppc>
#         <neighbor name="Austria" direction="E"/>
#         <neighbor name="Switzerland" direction="W"/>
#     </country>
#     <country name="Singapore">
#         <rank updated="yes">5</rank>
#         <year>2011</year>
#         <gdppc>59900</gdppc>
#         <neighbor name="Malaysia" direction="N"/>
#     </country>
#     <country name="Panama">
#         <rank updated="yes">69</rank>
#         <year>2011</year>
#         <gdppc>13600</gdppc>
#         <neighbor name="Costa Rica" direction="W"/>
#         <neighbor name="Colombia" direction="E"/>
#     </country>
# </data>
import xml.etree.ElementTree as ET


tree = ET.parse("XMLtest.xml")		# 处理哪个文件
root = tree.getroot()
print( "root为一串内存地址：",root)			#整个XML文档的入口地址
print(root.tag)			#根的标签名

print( "------------------遍历xml文档----------------------")
for child in root:					#遍历根标签内容(此为三个子标签)
	print(child.tag, child.attrib)		#child.tag：子标签名(此为country)，child.attrib：子标签属性(此为name)
	for i in child:					#遍历子标签内容
		print(i.tag,i.attrib, i.text)			#i.tag : 子子标签名（此为rank等），i.text：标签内容（此为2,2008等）
										#还可以添加i.attrib获取子子标签的属性（此为updated等）
	print('\n')


print("------------------只遍历year 节点----------------------")
for node in root.iter('year'):		# 通过iter方法取出year
	print(node.tag, node.text)

print("------------------ 修改XML文档 ----------------------")
for node in root.iter("year"):
	new_year = int(node.text )
	node.text = str( new_year + 1 )		#将每个year加1
	node.set("updated_by","lin")			#增加属性
tree.write("XMLtest.xml")		#写回源文件

print("------------------ 删除 ----------------------")
for country in root.findall('country'):		#root.findall()将子标签中的找出啦
	rank = int( country.find("rank").text )
	if rank > 50:
		root.remove(country)
tree.write( "XMLdelete.xml")		#写入一个新的XML文档


print("------------------ 自己创建XML文档 ----------------------")
new_xml = ET.Element("lin_data")		#根节点
#SubElement : 子标签，必须多于两个参数
PersonInfo1 = ET.SubElement(new_xml,"PersonInfo",attrib = {"enrolled":"yes"} )		#创建new_xml的子节点
#下面为子标签内容
name =  ET.SubElement(PersonInfo1,"name",attrib={ "checked":"no" })			#创建PersonInfo的子节点
age =  ET.SubElement(PersonInfo1,"age",attrib={ "checked":"no" })				#attrib : 必须为字典
sex = ET.SubElement(PersonInfo1,"sex")
name.text = "Lin"
age.text = "18"
sex.text = "man"

PersonInfo2 = ET.SubElement(new_xml,"PersonInfo",attrib = { "enrolled":"no"})
name =  ET.SubElement(PersonInfo2,"name",attrib={ "checked":"no" })
age = ET.SubElement( PersonInfo2,"age",attrib = { "checked":"no"})
sex = ET.SubElement( PersonInfo2,"sex")
name.text = "He"
age.text = "16"
sex.text = "woman"

XMLcreate = ET.ElementTree(new_xml)		#生成xml文档对象
XMLcreate.write("XMLcreate.xml",encoding = "utf-8",xml_declaration = True)		#写入文件
#xml_declaration : 声明这是一个xml格式的,即在头加上<?xml version='1.0' encoding='utf-8'?>
ET.dump(new_xml)		#打印生成的格式