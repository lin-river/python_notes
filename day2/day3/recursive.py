#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws

def calc(n):            #递归最多叠加999层，保护机制，防止内存被耗光
    print(n)
    if n//2 == 0:       #整除
        return 0
    return calc(n//2)
    print("->",n)       #无法执行到

calc(10)                 #递归效率不高

def calc2(n):
    print(n)
    if int(n/2) > 2:
        return calc( int(n/2) )

calc2(10)

print("---------二分查找法-----------")
data = [1,3,2,4,24,5,23,245,214,575,7,88,545,45,78,66]
def binary_search(dataset,find_num):
    dataset.sort()              #将列表中的数按从大到小排序
    print(dataset)

    if len(dataset) >1:
        mid = int(len(dataset)/2)
        if dataset[mid] == find_num:        # 找的数在mid左面
            print("we finding the num:",dataset.index(dataset[mid]))
        elif dataset[mid] > find_num:
            print("\033[31;1m The number to be found is on the [%s] left\033[0m" %dataset[mid])
            return binary_search(dataset[0:mid],find_num)
        else:                               # 找的数在mid右面
            print("\033[31;1m The number to be found is on the [%s] right\033[0m" %dataset[mid])
            return binary_search(dataset[mid+1:],find_num)
    else:
        if dataset[0] == find_num:
            print("we finding the num:",dataset[0])
        else:
            print("The number you are looking for is not in the list!")

binary_search(data,66)