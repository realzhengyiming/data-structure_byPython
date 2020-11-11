# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         binarySearch
# Description:  二分搜索相关
# Author:       zhengyiming
# Date:         2020/11/1
# -------------------------------------------------------------------------------

def binarySearch(lists, target):
    '''
    基本的框架步骤,常规的二分查找，算法理解一样要能够想象出完整的数据的 变化，移动，对比，交换等的顺序，
    切不可死记硬背，这样才有效果。二分法衍生问题找到最左边的，找到最右边的。

    主要和选定的起始左边和右边有关，然后是搜索区间的不同，注意一定不要漏掉区间

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

# 排序数组中查找元素的第一个和最后一个元素的位置
# 统一使用【左边，右边】闭区间这样，
def left_index_binarySearch(lists, target):
    pass


if __name__ == '__main__':
    print(binarySearch([1, 2, 3, 4, 5, 6], 5))
