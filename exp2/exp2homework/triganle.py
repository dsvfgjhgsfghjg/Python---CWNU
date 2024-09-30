# -*-coding:utf-8-*-
# !/user/bin/python3

import math

def triangle() :
    print("输入第一条边：")
    l1= float(input())
    print("输入第二条边：")
    l2= float(input())
    print("输入第三条边：")
    l3= float(input())
    p=(l1+l2+l3)/2
    s=math.sqrt(p*(p-l1)*(p-l2)*(p-l3))
    print("面积为："+str(s))
triangle()