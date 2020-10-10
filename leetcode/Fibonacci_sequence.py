# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         Fibonacci_sequence
# Description:  斐波那契 相关的问题，斐波那契数列是个很牛逼，很有趣的东西，也叫做黄金数列，太有趣来
# Author:       zhengyiming
# Date:         2020/10/8
# -------------------------------------------------------------------------------

# 斐波那契最初是从 兔子繁殖衍生而来的有趣的东西，
# 自然界到处都是，黄金分割点，又自然，又哲学，类似与1生2，2生三，三生万物
# 1 1 2 3 5 8 13 21 ...
# An = A(n-1)+A(n-2)
# 其中n=1，n=2时，A1=1，A2=2

# 因为是递推公式，所以很容易直接通过递归写出斐波那契数列的输出函数

# 前面说到直接递归三个条件
# 1.递归结束条件（没有的话就变成无限递归，类似死循环）不行的
# 2.递归继续《调用自身，开始树形往下--》
# 3.数据操作，没有这个的话，那就是啥也不干的递归，递归的同时需要处理数据，
# 一般是通过将调用自己来结合运算 如 2*f(n-1) .. f(n-2)*f(n-1)

import time


def timer(fun):
    def wrap(n, *args, **kw):
        start = time.time()
        fun(n, **kw)
        print(f"{fun}总共用时{time.time() - start}")

    return wrap


# @timer
def Fibonacci_recursion(n) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 1  # 这儿是从1 1 2 这样的完整的斐波那契
    else:
        total = Fibonacci_recursion(n - 2) + Fibonacci_recursion(n - 1)
        return total


# 因为直接使用递归可能出现
# 缺点
# 1.效率低下
# 2.浪费资源
# 3.还有可能会栈溢出（某些值也会被一直重复计算）
# 优点
# 层次清晰，易于理解
# 优化的方式可以改用尾递归/迭代，后两种的效率会比直接递归效率好很多的。编程的技巧
# 尾递归是指向同一个栈地址，就不会太多的栈（增加参数）
# 但是python cpython没有对递归进行优化，但是其他语言可以有优化（pyhon中还是多用循环，实际工作中）
# 朴素的递归产生的栈的层次像二叉树一样，以指数级增长，
# 但是现在栈的层次却像是数组，变成线性增长了，减少了很多栈
# 总结起来也很简单，原本栈是先扩展开，然后边收拢边计算结果，现在却变成在调用自身的同时通过参数来计算。
def Fibonacci_tail_recursion(n, ret1=0, ret2=1):  # 从0，1开始
    if n == 0:
        return ret1  # 所以这个ret1是基本确定的0号是0
    # elif n == 1:
    #     return 1
    # elif n == 2:
    #     return 1
    else:
        return Fibonacci_tail_recursion(n - 1, ret2, ret2 + ret1)


# 循环的形式实现，循环逻辑是从底部往前的，
# 这儿的，不可以改成从顶部倒退 像递归那样（其实直接递归那样效率比较低的），
# 因为值从一开始才有，递归也是利用一开始的两个确定的值来推的，但是递归会开启过多的程序栈（树结构）并且可能存在反复计算（可以使用备忘录和动态规划优化）
# 这种相当于迭代法，效率比前面的直接递归效率高
# @timer
def Fibonacci_recurrence(n):
    a, b = 1, 1  # 最初的前两个数字
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(3, n + 1, 1):
            temp = a
            a = b
            b = temp + b
    return b


# 以上两个其实是跳台阶的问题，因为 1 1重复了，所以直接从1 2 3 5 开始
@timer
def F_list(n):
    f_lists = []
    for i in range(n):
        f_lists.append(Fibonacci_tail_recursion(i))  # 大量的反复计算这儿也可以看出来，并且开启堆栈太多容易溢出
    print(f_lists)


# 斐波那契问题变体 这儿是 1 2 3 5 8 ...
# 如果只有一阶台阶，只有一种跳法，一次跳一阶
# 如果只有2阶台阶，只有2种跳法，一次跳一阶，连续跳；一次跳两阶
# 如果大于2阶台阶，
# 一是第一次跳一级，此时跳法的数目等于后面剩下的n-1级台阶的跳法数目，
# 二是第一次跳二级，此时跳法的数目等于后面剩下的n-2级台阶的跳法数目，
# 因此n级台阶的不同跳法的总数为，不难看出就是斐波那契数列an = a(n-1)+a(n-2)


# 青蛙上台阶问题，n阶台阶，一次跳1阶或者2阶，
temp_list = {}  # 全局变量，增加备忘录，缓存思想


def fork_upstair(n):
    if n in temp_list.keys():
        return temp_list[n]
    if n == 0:
        temp_list[n] = 0
        return 0
    if n <= 2:
        temp_list[n] = 1
        return 1
    else:
        total = fork_upstair(n - 1) + fork_upstair(n - 2)
        temp_list[n] = total
        return total  # 直接算是备忘录，减少一定次数的反复计算


fork_temp_list = {}  # 备忘录（缓存）+ 尾递归 ，又优化了不少呢。


def fork_upstair_tail(n, et1=0, et2=1):  # 用参数来进行缓存
    if n in fork_temp_list.keys():
        return fork_temp_list[n]
    if n == 0:
        temp_list[n] = et1
        return et1
    else:
        total = fork_upstair_tail(n - 1, et2, et2 + et1)  # 节约内存
        fork_temp_list[n] = total
        return total  # 直接算是备忘录，减少一定次数的反复计算


# 直接递归效率很低


if __name__ == '__main__':
    n = 100
    start = time.time()
    print(Fibonacci_tail_recursion(n, ret1=0, ret2=1))  # 还真的会栈溢出呢，斐波那契数列,指数降成了线性
    step1 = time.time()
    print("Fibonacci_tail_recursion {}".format(step1 - start))
    print()

    print(Fibonacci_recurrence(n))  # python默认有一个调用栈限制，所以还是会栈溢出
    step2 = time.time()
    print(step2 - step1)
    print("Fibonacci_recurrence {}".format(step2 - step1))
    print()

    print(fork_upstair(n))  # 还真的会栈溢出呢，斐波那契数列
    step3 = time.time()
    print(step3 - step2)  # 增加备忘录的虽然也挺久，但是也快了很多，下面的更久
    print("fork_upstair {}".format(step3 - step2))
    print()

    print(fork_upstair_tail(n))  # 还真的会栈溢出呢，斐波那契数列
    step4 = time.time()
    print(step4 - step3)  # 增加备忘录的虽然也挺久，但是也快了很多，下面的更久
    print("fork_upstair {}".format(step4 - step3))
    print()

    #
    # print(Fibonacci_recursion(n))  # 还真的会栈溢出呢，斐波那契数列
    # step4 = time.time()
    # print("Fibonacci_recursion {}".format(step4 - step3))
    # print()
