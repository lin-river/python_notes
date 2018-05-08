#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws
#产品列表
product_list = [
    ("Iphone",5800),
    ("Mac Pro",9800),
    ("Bike",800),
    ("Watch",10600),
    ("book",88),
]
shopping_list = []      #购物车清单
salary = input("Input your salary:")        #工资
#判断工资输入是否正确
if salary.isdigit():        #如果是“1,2...”数字形式的则返回真，实际上还是字符串
    salary = int(salary)
else:
    print("invalid ！")

while True:
    """
    for item in product_list:
        print(product_list.index(item) + 1,item)
    break
"""
#打印商品
    for index,item in enumerate(product_list):
        #enumerate()返回序列号和值,直接打印enumerate（）会打印一串地址
        print(index,item)
    #判断编号输入是否正确
    user_choice = input("请选择要买的商品:>>>")
    if user_choice.isdigit():
        user_choice = int(user_choice)
        #判断输入的商品编码是否符合
        if user_choice < len(product_list) and user_choice >= 0:
            p_item = product_list[user_choice]
            #判断是否可以买下商品
            if p_item[1] <= salary:
                print("可以的，买下它！")
                #扣除工资并加入购物车
                shopping_list.append(p_item)
                salary -= p_item[1]
                print("Add %s into cart, your current balance is \033[100;1m%s\033[0m" %(p_item,salary))
                #\33[颜色编号；1m 内容 \033[0m     调整字体颜色，31是白底红字，41是红底黑字，32是白底绿字，42是绿地黑字
            else:
                print("\033[110;1m你的余额只剩[%s],没钱买个毛线啊...\033[0m" %(salary))
        else:
            print("product code [%s] is not exist!" %user_choice)
    elif  "q" == user_choice:
        print("exit...")
        print("---- shopping cart ----")
        for p in shopping_list:
            print(p)
        exit()
    else:
        print("invalid option...")

