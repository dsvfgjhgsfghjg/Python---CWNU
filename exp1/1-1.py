# -*-coding: utf-8 -*-
# !/usr/bin/python3

import math

def cone():
    volume = 0
    print("输入半径")
    r = input()
    print("输入高")
    h = input()
    expression = f"(1/3) * math.pi * float({r}) * float({h})"
    volume=(eval(expression))
    print(volume)

cone()