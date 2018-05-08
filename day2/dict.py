#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"
dict = {
    "stu1":"zao",
    "stu2":"qian",
    "stu3":"sun",
    "stu4":"li",
    1:2
}
print(dict)    #在python3.6以前，字典的输出是无序的，Python3.6里字典的key终于有序了，先设置的key先输出
               #{'stu1': 'zao', 'stu2': 'qian', 'stu3': 'sun', 'stu4': 'li', 1: 2}
#删除
#del dict        #删除整个字典
del dict["stu1"]        #通过键名删除
dict.popitem()           #任意删一个
dict.pop("stu2")        #通过键删除，不给键报错
dict["stu1"] = "赵"      #通过键名添加键值
#查找
print(dict.get("stu2"))     #通过键名查找，有返回值，没有返回"None"   None
#判断一个键是否存在与字典
print("stu2" in dict)       #=pyrhon 2.X 中的 dict.has_key("stu5"),存在返回True，不存在返回False
print(dict)         #{'stu3': 'sun', 'stu4': 'li', 'stu1': '赵'}

#多级字典嵌套及操作

menu_catalog = {
    "chinese":{
        "shicuan":["麻婆豆腐","以麻辣为主的菜肴"],
        "dongbei":["dacong","rice","精干豪放"],
        "guandong":["......","eat ervertthing..."]
    },
    "Europe":{
        "English":["chips","hamburger","cookies"]
    }
}
menu_catalog.setdefault("japan",{"food":[1,2,3]})       #添加内容key,value
menu_catalog.setdefault("japan",{"food":[3,2,1]})       #如果字典内已有键，则不做修改，没有则添加进字典
print(menu_catalog)
print(menu_catalog["chinese"]["guandong"][1])       #通过多级键名索引 eat ervertthing...

dict2 = {
    1:1,2:2,3:3
}
dict2.update(dict)      #从另一个字典更新成员（不存在的就创建，存在的就覆盖）
print(dict2)        #{1: 1, 2: 2, 3: 3, 'stu3': 'sun', 'stu4': 'li', 'stu1': '赵'}
d = dict.fromkeys([6,7,8],"text")       #以所给的键创建一个字典，默认值是None
d[7] = "hehe"       #一层情况下，修改一个键，其余键变
print(d)        #{6: 'text', 7: 'hehe', 8: 'text'}
d = dict.fromkeys([6,7,8],[1,{"name":"haha"}])      #三个键共享一个后面的默认值地址，
                            # 所以在多层情况下修改任一键后的的值，其他键的值跟着变
print(d)        #{6: [1, {'name': 'haha'}], 7: [1, {'name': 'haha'}], 8: [1, {'name': 'haha'}]}
d[7][1]["name"] = "hehe"
print(d)        #{6: [1, {'name': 'hehe'}], 7: [1, {'name': 'hehe'}], 8: [1, {'name': 'hehe'}]}
print(dict2.items())        #将字典转化为列表

for i in dict:              #效率更高
    print(i,dict[i])        #stu3 sunstu3 sun\nstu4 li\nstu1 赵
for k,v in dict.items():    #x先变成列表再取值
    print(k,v)              #stu3 sunstu3 sun\nstu4 li\nstu1 赵

"""
av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}

av_catalog["大陆"]["1024"][1] = ",可以用爬虫爬下来"
print(av_catalog)
#ouput ['全部免费,真好,好人一生平安', '服务器在国外,慢,可以用爬虫爬下来']
"""