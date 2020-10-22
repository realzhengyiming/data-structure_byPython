# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         BSF
# Description:  BSF和前面的DSF，回溯算法其实很类似的
#               leetcode 111 题  easy 类型
#               BSF一般是用来求图start到end最短路径，很枯燥；走迷宫也是一样
# Author:       zhengyiming
# Date:         2020/10/14
# -------------------------------------------------------------------------------


# BSF解题框架，又是二叉树的遍历。各种高遍历的方法。
#
# def BSF():
#     1.结束条件
#         返回结果集
#
#     if 做过了选择：
#         先回溯
#     for 选择 in 选择集：
#         if 不合法的选择：
#             cotinue
#         做选择

# labuladong的不回溯，改用非递归的方法，就是迭代/while/for这种，这种就需要转一转，从递归层的直逻辑绕一绕就过去了

# 1.leetcode 111 判断一颗二叉树的最小高度
from queue import Queue


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def TemplateShortTreeDepth():
    q = Queue()  # 初始化一个队列

    # 初始化一颗二叉树，找最小高度
    ['A', "B", "C", None, None, "D", "E"]
    root = TreeNode("A", TreeNode("B", None, None), TreeNode("C", TreeNode("D", None, None), TreeNode("E", None, None)))

    def BSF(start):
        q.put(start)  # 1.起点入队
        # visited 原本是图的话需要有一个访问的集合，不过树，链表，只能单向，那就可以不用
        depth = 1  # root 默认算一层
        while not q.empty():  # 队列不空，就继续
            node = q.get()  # 取出刚才的
            if node.left is None and node.right is None:  # 2.判断到终点了没(这儿是叶子节点，终端节点）
                return depth  # 到了就结束
            # for 原本是用for的代表把能走的都走了，而这儿只有两个分之，直接了
            if node.left is not None:  # 还需要判断非空，才添加进去，有时候有一个可以走的
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)
            depth += 1  # 然后这样深度就加一了

    result = BSF(root)
    print(result)


def Leetcode752():  # 密码锁问题,不单单用来解答迷宫；还好可以用来解答密码
    pass
    print("")


if __name__ == '__main__':
    # 这个就是二叉树的
    TemplateShortTreeDepth()
