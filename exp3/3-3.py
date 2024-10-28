# 要求：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13，…，计算该序列的前 20 项之和。

def sum_order():
    sum = 0
    i = 0
    num = 2
    dom = 1
    temp =0
    while i<20:
        sum = sum + num/dom
        temp = num
        num = num + dom
        dom = temp
        i+=1
    print(sum)
sum_order()