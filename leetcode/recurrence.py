# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         递归
# Description:
# Author:       zhengyiming
# Date:         2020/10/8
# -------------------------------------------------------------------------------

def sum_jieceng(n):
    total = 1
    for i in range(n, 0, -1):
        print(i)
        total *= i
    return total

# 递归三个条件
# 1.递归结束条件（没有的话就变成无限递归，类似死循环）
# 2.递归继续《调用自身，开始树形往下--》
# 3.数据操作，没有这个的话，那就是啥也不干的递归，递归的同时需要处理数据，
def recurrence_jieceng(n):
    if n <= 1:
        return 1
    print(n)
    total = n*recurrence_jieceng(n - 1)  # 迭代，但是只有迭代是没有的，相当于for
    return total
    # 还需要处理


if __name__ == '__main__':
    print()
    print(sum_jieceng(3))
    print()
    print(recurrence_jieceng(3))
