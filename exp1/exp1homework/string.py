# -*-coding: utf-8 -*-
# !/usr/bin/python3

def main():
    strs = ['11111', 'woshizuichangzifuchuan', '54188']
    longest_str = ''
    for item in strs:
        if len(item) > len(longest_str):
            longest_str = item

    print(longest_str)  # 这将打印出 'woshizuichangzifuchuan'


# 调用 main 函数
main()
