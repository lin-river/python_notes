#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import re

str1 = 'hero321lin123'

print( '----------- 从字符串头开始匹配: re.match() ------------')
print()

print( '---------- 从整个文本里搜索匹配: re.search() ----------')
print( re.search("l.+n",str1))
print()

print( '----------- 返回所有匹配结果: re.findall() ------------')
print( re.findall("[0-9]{1,3}","a1b23c456c"))		# 返回所有匹配结果
# ['1', '23', '456']
# re.findall("[0-9]{1,3}","a1b23c456c").group()		#findall()没有group()方法
# AttributeError: 'list' object has no attribute 'group'
print()

print( '------------- 获取匹配的内容: re.group() --------------')
res = re.match( "hero\d",str1)				#\d匹配一个数字
print( res.group() )
res = re.match( "hero\d+",str1)			#\d+匹配一个或多个数字
print( res.group() )
print()

print( '------- 以匹配到的字符当做列表分隔符:re.split() ---------')
print( re.split("[0-9]","a1b2c3d4c56ef7g") )
# ['a', 'b', 'c', 'd', 'c', '', 'ef', 'g']
print( re.split("[0-9]+","a1b2c3d4c56ef7g") )
# ['a', 'b', 'c', 'd', 'c', 'ef', 'g']
print()

print( '------------- 匹配字符并替换: re.sub() ---------------')
# sub(pattern, repl, string, count=0, flags=0)
print( re.sub("[0-9]+","999","a1b2c3d4c56ef7g" ))
# a999b999c999d999c999ef999g
print( re.sub("[0-9]+","|","a1b2c3d4c56ef7g",count=2 ))			#只换前俩个,不写默认替换全部
# a|b|c3d4c56ef7g
print()

print( '------------------ 匹配模式：flags -------------------')
print("re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）:")
print( re.search("[a-z]+","abcdEFg",flags=re.I))
# <_sre.SRE_Match object; span=(0, 7), match='abcdEFg'>

print( "\nre.M(MULTILINE): 多行模式，改变'^'和'$'的行为:")
print( "当本标志指定後， '^' 匹配字符串的开始和字符串中每行的开始。",
	   "同样的， $ 元字符匹配字符串结尾和字符串中每行的结尾（直接在每个换行之前）")
print( re.findall("[a-z]+t$","\nfirst\neight\n"))		#不加匹配模式
# ['eight']
print( re.findall("[a-z]+t$","\nfirst\neight\n",flags=re.M))
# ['first', 'eight']

print("\nre.S(DOTALL): 点任意匹配模式，改变'.'的行为")
print('使 "." 特殊字符完全匹配任何字符，包括换行；没有这个标志， "." 匹配除了换行外的任何字符。')
print( re.search(".+","\nabc	123"))						#不加匹配模式
# <_sre.SRE_Match object; span=(1, 8), match='abc\t123'>
print( re.search(".+","\nabc	123",flags=re.S))
# <_sre.SRE_Match object; span=(0, 8), match='\nabc\t123'>
print()

print( '------------- 匹配前一个字符1次或多次："+" -------------')
print( '------------- 匹配前一个字符1次或0次："？" -------------')
print( re.search("er?",str1))				#匹配到返回
# <_sre.SRE_Match object; span=(1, 3), match='er'>
print( re.search("a?",str1))				#匹配不到也会返回，默认为开头
# <_sre.SRE_Match object; span=(0, 0), match=''>
print("匹配前面一个字符1次或0次，所以：")
print( 'aaa?相当于匹配"aaa"或"aa",优先匹配"aaa":')
print( re.search('aaa?','aaalinaaaa'))
# <_sre.SRE_Match object; span=(0, 3), match='aaa'>
print( re.search('aaa?','aalinaaaa'))
# <_sre.SRE_Match object; span=(0, 2), match='aa'>
print( re.search('aaa?','alinaaaa'))
# <_sre.SRE_Match object; span=(4, 7), match='aaa'>
print()

print( '------------------匹配字符串开头："^"------------------')
print( re.match("^",str1) )					#匹配字符串开头
# 返回<_sre.SRE_Match object; span=(0, 0), match=''>
print( re.match( "^hero",str1 ) )
# <_sre.SRE_Match object; span=(0, 4), match='hero'>
print( re.match( "^123",str1 ) )			#若未匹配到则返回None
print()

print( '-----------默认匹配除\\n之外的任意一个字符："."----------')
print( re.match( ".",str1 ) )
#返回<_sre.SRE_Match object; span=(0, 1), match='h'>
print( re.match(".+\d",str1))				#".+"表示匹配任意长度字符串,所以\d没有用上
#返回<_sre.SRE_Match object; span=(0, 13), match='hero321lin123'>
print()

print( '------------------匹配字符串结尾："$"------------------')
print( re.search("l.+3$",str1))				#字符串str是否以$匹配的字符结尾，是的返回匹配内容，否则返回None
# 返回 <_sre.SRE_Match object; span=(7, 13), match='lin123'>
print()

print( '--------- [] :中括号表达式，要匹配 [，请使用 \[ ---------')
print( re.search("l[a-z]+n",str1 ) )		# [a-z]匹配小写字母
#只匹配最先遭到的第一个匹配串
print()

print( '---------------- {m} :匹配前一个字符m次 ----------------')
print( re.search("[0-9]{3}","12haha321he"))				# 匹配前一个字符3次
# <_sre.SRE_Match object; span=(6, 9), match='321'>
print("'{n,m}':匹配前一个字符n到m次")
print( re.search("[0-9]{2,3}","12haha321he"))				#匹配前一个字符1到3次
# <_sre.SRE_Match object; span=(0, 2), match='12'>
print( re.findall("[0-9]{1,3}","a1b23c456c"))				#返回所有匹配结果
# ['1', '23', '456']
print()

print("-------------- '|':匹配 | 左或 | 右的字符 --------------")
print( re.search("abc|ABC","1ABCabc23"))					#优先匹配字符串内先出现的匹配串
# <_sre.SRE_Match object; span=(1, 4), match='ABC'>
print()

print("------------------- (...)：分组匹配 -------------------")
print( re.search( "abc{2}","abcabcabcc"))					#没加括号相当于匹配c字符两次
# <_sre.SRE_Match object; span=(6, 10), match='abcc'>
print( re.search( "(abc){2}","abcabcabcc"))				#加括号后相当于匹配abc字符串两次
# <_sre.SRE_Match object; span=(0, 6), match='abcabc'>

print("------------------- |：匹配转义字符 -------------------")
print( re.search("\|{2}","|$||$|"))
# <_sre.SRE_Match object; span=(2, 4), match='||'>
print()

print("-------------------- 匹配转义字符 ---------------------")
print("'\A': 只从字符开头匹配,同'^' :")
print("'\Z': 匹配字符结尾，同'$':")
print( re.search( "\A[0-9]+a\Z","123a"))
# <_sre.SRE_Match object; span=(0, 4), match='123a'>

print("\n'\d': 匹配数字0-9")

print( "\n'\D': 匹配非数字:" )
print( re.search( "\D+","123\n$- aA\\"))
# <_sre.SRE_Match object; span=(3, 10), match='\n$- aA\\'>

print( "\n'\w': 匹配[A-Za-z0-9],即大小写和数字" )
print( re.search( "\w+","123\n" ) )
# <_sre.SRE_Match object; span=(0, 3), match='123'>
print( "\n'\w': 匹配非[A-Za-z0-9],即只匹配特殊字符" )
print( re.search("\W+","123\n$- aA\\"))
# <_sre.SRE_Match object; span=(3, 7), match='\n$- '>
print("\n'\s'：匹配空白字符、\\t、\\n、\\r")
print( re.search( "\s+","\r\n	"))
# <_sre.SRE_Match object; span=(0, 3), match='\r\n\t'>
print()

print("---------------- '(?P<name>...)' 分组匹配 -----------------")
print( re.search("(?P<id>[0-9]+)(?P<name>[a-zA-Z]+)","abc1234Defg@123").groupdict() )
# {'id': '1234', 'name': 'Defg'}
print( re.search("(?P<id>[0-9]+)(?P<name>[a-zA-Z]+)","abc1234Defg@123").group("id") )
# 1234

print("Eg:")
print( re.search("(?P<province>[0-9]{2})(?P<city>[0-9]{2})\d\d(?P<birthday>[0-9]{8})", "371481199306143242").groupdict())

# 匹配 * 号前的字符0次或多次，re.findall("ab*", "cabb3abcbbac")
# 结果为['abb', 'ab', 'a']

