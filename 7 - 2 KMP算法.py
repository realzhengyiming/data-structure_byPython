# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     7 - 2 KMP算法   
   Description :  
   Author :        zhengyimiing 
   date：          2019/9/9 
-------------------------------------------------
   Change Activity:
                   2019/9/9
        kmp算法是基于朴素匹配算法的改进，主要改变在于
    匹配失效后对于j的回滚操作，不再是暴力的j=0，而是基
    于类似“最长相同前缀后缀”来想出来的。
    此文件有三个版本的字符串匹配算法的对比，
    1）默认的朴素匹配算法
    2）使用“最长相同前缀后缀”--》得到next数组
    进行粗略改进的 KMP算法
    3）对2）中改进，对next数组使用迭代进行改进的
    KMP算法完整形态。

    思路实现详情，参考这个博主的博文:
    https://www.cnblogs.com/ZuoAndFutureGirl/p/9028287.html

    拓展的算法还有MB算法，
    还有sunday算法
-------------------------------------------------
"""
import datetime

__author__ = 'zhengyimiing'

def print_calc_time(func):
    def wrapper(*args, **kw):
        start_time = datetime.datetime.now()
        result = func(*args, **kw)
        end_time = datetime.datetime.now()
        ss = end_time - start_time
        print('Function <{}> run time is {}s.'.format(func.__name__, ss))
        return result
    return wrapper


# 1)BF 匹配算法
@print_calc_time
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


# 2) 使用“最长相同前缀后缀”改进得到next数组的kmp 1号
def GetNext(p):
    #  生成固定的长度的next用来存next数组
    next = [x for x in range(len(p))]
    pLen = len(p)
    next[0] = -1
    k = -1
    j = 0
    while j < pLen - 1:
        if k == -1 or p[j] == p[k]:
            k += 1
            j += 1
            next[j] = k
        else:
            k = next[k]
    return next   # 把next数组返回回去就可以了

@print_calc_time
def KMP_1(s, t):
    i = j = 0
    next = GetNext(t)
    while i != len(s) - 1 and j != len(t) - 1:  # 这里也是有一个问题，所以不是对值，是对下标
        if s[i] == t[j]:
            i += 1
            j += 1
        else:  # 否则就是i和j都回溯回去，这个才是比较麻烦的。
            i = i - j + 1
            j = next[j]
    # return i
    if j == len(t) - 1:
        return i - j + 1
    else:
        return 0  # 匹配失败返回0 ，不如返回-1


# 在2)基础上继续改进的，使j的回滚使用next迭代最为回滚结果的kmp算法
def GetNext2(p):
    #  生成固定的长度的next用来存next数组
    next = [x for x in range(len(p))]
    pLen = len(p)
    next[0] = -1
    k = -1
    j = 0
    while j < pLen - 1:
        if k == -1 or p[j] == p[k]:
            k += 1
            j += 1
            # 较之前next数组求法，改动在下面4行
            if p[j] != p[k]:
                next[j] = k  # 之前只有这一行
            else:
                # 因为不能出现
                p[j] = p[next[j]]
                # 所以当出现时需要继续递归，k = next[k] = next[next[k]]
                next[j] = next[k]
        else:
            k = next[k]
    return next   # 把next数组返回回去就可以了


@print_calc_time
def KMP_2(s, t):
    i = j = 0
    next = GetNext2(t)   # 使用改进过后的next数组
    while i != len(s) - 1 and j != len(t) - 1:  # 这里也是有一个问题，所以不是对值，是对下标
        if s[i] == t[j]:
            i += 1
            j += 1
        else:  # 否则就是i和j都回溯回去，这个才是比较麻烦的。
            i = i - j + 1
            j = next[j]
    # return i
    if j == len(t) - 1:
        return i - j + 1
    else:
        return 0  # 匹配失败返回0 ，不如返回-1


if __name__ == '__main__':
    s = "ababababaababaabababababababababaaaaababacacbacbasdfhwerxycvhwerabbababcabcabcabcabcdacdefgabcdefabcdefabcdefabcdefgabk"

    t = "abk"

    print(BF(s, t))
    print(KMP_1(s,t))
    print(KMP_2(s,t))