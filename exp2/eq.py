# -*-coding:utf-8-*-
# !/user/bin/env python3
import math
def eq():
    print('输入参数a：')
    a=float(input())
    print('输入参数b：')
    b=float(input())
    print('输入参数c：')
    c=float(input())
    p=b*b - 4*a*c
    if p>0 :
        x1=(-b+math.sqrt(p))/(2*a)
        x2=(-b-math.sqrt(p))/(2*a)
    else:
        print("没有实数根！")

eq()