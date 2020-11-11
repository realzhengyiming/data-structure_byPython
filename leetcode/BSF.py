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
#     队列存储选择
#     集合，存储已经做过的选择
#     起点加入队列
#     步数为0
#     while 队列不为空：
#       队列长度
#       for(i in 队列长度）：
#         出队一个，
#        1.结束条件：是否到了终点
#           返回结果集
#       把这个选择附近节点的选择（没做过的，没走过的，加入队列中去）
#       步数+1

# labuladong的不回溯，改用非递归的方法，就是迭代/while/for这种，这种就需要转一转，从递归层的直逻辑绕一绕就过去了

# 1.leetcode 111 判断一颗二叉树的最小高度
from queue import Queue


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def TemplateShortTreeDepth():  # 二叉树最短路径
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
            depth += 1  # 然后这样深度就加一了，一圈一圈往外扫，每一个外层算是一步，记录最短路径。

    result = BSF(root)
    print(result)


def Leetcode752():
    '''
    又一个需要多思考的就是，如何抽象，能够把实际现实中的东西抽象成代码层面
    1.无论如何，数据结构，算法题；就是操作数据，存储数据，所以实际的东西要抽象成数据
    2.BSF中的这儿，做选择，就是一个例子；比如这道题目里面的转密码锁，转懂改变值就是做选择
    这些就是解构出来的数据，对这些数据进行处理.
    # n 位密码的bsf解答，解答问题可以先从一位开始，从简单到复杂，可以更好的理解算法
    '''

    def plus(s, i):
        temp = list(s)
        num = int(temp[i])
        if num == 9:
            num = 0
        else:
            num += 1
        temp[i] = str(num)
        return "".join(temp)

    def sub(s, i):
        temp = list(s)
        num = int(temp[i])
        if num == 0:
            num = 9
        else:
            num -= 1
        temp[i] = str(num)
        return "".join(temp)

    start = "000"
    target = "126"

    def bsf(start, target):
        q = Queue()
        visited = set()
        depth = 0
        # try_time = 0

        q.put(start)
        visited.add(start)

        while not q.empty():
            qz = q.qsize()

            for i in range(qz):  # 队列中每个已经做过的选择取出来，再把这些选择附近还可以做的选择加入队列--
                val = q.get()
                if val == target:
                    return depth
                # try_time += 1
                ## 如果要每一种可能当成一次探索
                for i in range(len(val)):  # 这个是按位数来，其实是有四种选择，需要都表示出来，增加数字减少数字那个只是其中的操作
                    # todo 字符串如何拼接回去
                    n_s_int = plus(val, i)  # 做选择后的结果，
                    if n_s_int not in visited:  # 看看有没有访问过，集合内
                        q.put(n_s_int)  # 入队
                        visited.add(n_s_int)  # 设置访问过。

                    n_s_int2 = sub(val, i)
                    if n_s_int2 not in visited:
                        q.put(n_s_int2)
                        visited.add(n_s_int2)
            depth += 1
        if depth == 0:
            return -1  # 没找到的情况
        return depth

    result = bsf(start, target)
    return result


if __name__ == '__main__':
    # 这个就是二叉树的
    # TemplateShortTreeDepth()

    # 这个是转密码锁的那道题目
    # Leetcode752()

    # 一位数的看看什么情况
    # test_0_9()

    # fun-2位
    result = Leetcode752()
    print(result)
