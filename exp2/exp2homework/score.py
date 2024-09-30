# -*-coding:utf-8-*-
# !/usr/bin/python3

def score():
    print("输入第一科成绩：")
    score1 = float(input())
    print("输入第二科成绩：")
    score2 = float(input())
    print("输入第三科成绩：")
    score3 = float(input())
    condition = (score1<=100 and score2<=100 and score3<=100 and score1>=0 and score2>=0 and score3>=0)
    if condition:
        sum = score1+score2+score3
        average = sum/3
    print("总分")
    print(sum)
    print("平均成绩")
    print(average)

score()