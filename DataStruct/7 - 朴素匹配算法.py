# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     7 - 朴素匹配算法   
   Description :  
   Author :        zhengyimiing 
   date：          2019/9/6 
-------------------------------------------------
   Change Activity:
                   2019/9/6
    字符串一般在C++ ，/C/Java等语言中是使用顺序存储的
    结构.主串中寻找字串T的过程称为模式匹配，T称为模式

    朴素的模式匹配算法是带回溯的。
-------------------------------------------------
"""

__author__ = 'zhengyimiing'

import unittest
from abc import ABC, abstractmethod


def BF(s, t):  # 这儿返回的匹配的开始位置是从1开始的，所以会有所不同
    i = j = 0
    while i != len(s) - 1 and j != len(t) - 1:  # 这里也是有一个问题，所以不是对值，是对下标
        if s[i] == t[j]:
            i += 1
            j += 1
        else:  # 否则就是i和j都回溯回去，这个才是比较麻烦的。
            i = i - j + 1
            j = 0
    # return i
    if j == len(t) - 1:
        return i - j + 1
    else:
        return 0  # 匹配失败返回0 ，不如返回-1


if __name__ == '__main__':
    s = "01234567"
    t = "345"
    print(BF(s, t))
