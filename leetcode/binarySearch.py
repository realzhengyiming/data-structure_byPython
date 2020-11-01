# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         binarySearch
# Description:  二分搜索相关
# Author:       zhengyiming
# Date:         2020/11/1
# -------------------------------------------------------------------------------

def binarySearch(lists, target):
    '''
    基本的框架步骤
    :param lists:  要搜索的列表（已经排好了顺序，这儿应该是不重复的列表）
    :param target: 目标的值
    :return:
    '''
    left = 0  # 1. 初始化最左边的坐标
    right = len(lists) - 1
    while left <= right:
        mid = left + (right - left) // 2  # 防止数字溢出

        if lists[mid] == target:
            return mid  # 找到就把下标放出来

        elif lists[mid] < target:
            left = mid + 1
        elif lists[mid] > target:
            right = mid -1

    return -1  # 如果没有找到


if __name__ == '__main__':
    print(binarySearch([1, 2, 3, 4, 5, 6], 5))
