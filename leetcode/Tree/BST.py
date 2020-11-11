# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         BST树
# Description:
# Author:       zhengyiming
# Date:         2020/11/4
# -------------------------------------------------------------------------------

# 1.创建一颗BST树
class Tree_node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


def BST_insert(root, val):
    '''

    :param root: 待插入的树
    :param val:  待插入树中的值
    :return: 返回这棵新树
    '''
    if root is None:  # 1. 子递归结束条件
        return Tree_node(val)  # 创建一个新的返回回去

    # 2.子问题开始按照要求执行递归和操作
    if val > root.val:
        return BST_insert(root.right, val)
    if val < root.val:
        return BST_insert(root.left, val)

    return root



# 2.bst树的操作有 插入；查找；删除，这种数据结构，修改呢？那就是先删除再插入，都是增删查改

# 2.验证一颗BST树
