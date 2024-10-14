# -*- coding: utf-8 -*-
# !/usr/bin/env python

def count_characters(s):
    char_count = {}

    for char in s:

        if 'a' <= char <= 'z':

            if char in char_count:
                char_count[char] += 1

            else:
                char_count[char] = 1

    for char, count in sorted(char_count.items()):
        print(f"{char}: {count}")


strvar = "the quick brown fox jumps over a lazy dog"
strvar_lower = strvar.lower()
count_characters(strvar_lower)