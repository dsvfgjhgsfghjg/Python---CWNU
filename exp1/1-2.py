# -*-coding: utf-8 -*-
# !/usr/bin/python3

def daikuan():
    print("输入存款金额：")
    jine = float(input())
    print("存款年限")
    n = int(input())
    rate = 0.052
    profit = jine*(1.0+rate)*n
    print("收益：",profit)
daikuan()