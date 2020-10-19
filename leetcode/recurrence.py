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
    total = n * recurrence_jieceng(n - 1)  # 迭代，但是只有迭代是没有的，相当于for
    return total
    # 还需要处理


# 其实平时说的分而治之的意思也就是递归的意思；
# 所以快速排序，和归并排序其实也就是递归的分而治之而已
# 按照思考的过程自己把过程还原回来，按框架走，这就是把知识联系起来，如果只是零散在一旁，总是会被忘记的
# 归并的递推方程可以写成（状态方程）：f(lists) = f(lists[mid:]) + f(lists[:mid])
# 就是这样，然后里面核心的后置遍历操作是合并两个相对有序的数组/列表，最小子问题
def merge(lists):
    # 1。停止条件
    if len(lists) <= 1:
        return lists

    mid = len(lists) // 2  # 整除，分两边
    # 2。开始两边递归 ，树是一样的
    left = merge(lists[:mid])
    right = merge(lists[mid:])  # 递归下去划分

    # 3。类似后续遍历，这儿是递归结束后操作的情况
    # 此处是合并相对有序的两个数组
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):  # 优化的话就是减少比对次数，相对有序的情况下
        # print(left)
        # print(right)
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]  # √  # 后面剩下的部分也直接添加进来,不能用append
    result += right[j:]
    return result  # 合并排好序的两个数组返回回去

    # 相当于后置遍历的二叉树了，又是递归的思想解决重复的子问题，还能优化吗


if __name__ == '__main__':
    # print()
    # print(sum_jieceng(3))
    # print()
    # print(recurrence_jieceng(3))

    # 归并排序
    result = merge([9, 8, 7, 6, 5, 4, 3, 2, 1, 1])
    print(result)
