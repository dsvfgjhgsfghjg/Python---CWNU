# -*-coding: utf-8 -*-
# !/usr/bin/python3

import math

def daishu():
    num1 = 1+1-10*8%10/5
    print(num1)
# +-*%就是代数运算

def zhishu():
    base = 2
    exponent = 3
    zhishures = math.pow(base,exponent)
    print("指数：",zhishures)

def duishu():
    duishurse = math.log10(100)
    print("10的对数：",duishurse)
    # 任意对数为
    # math.lag(2,3)

def sanjiaohanshu():
    radians = math.radians(45)
    sin = math.sin(radians)
    cos = math.cos(radians)
    tan = math.tan(radians)
    cot = math.cos(tan)
    print("正弦",sin)
    print("余弦",cos)
    print("正切", tan)
    print("余切", cot)

daishu()
zhishu()
sanjiaohanshu()
duishu()