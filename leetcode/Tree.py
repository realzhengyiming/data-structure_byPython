# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         Tree
# Description:  根据前序遍历和中序遍历恢复一棵树，根据后序遍历和中序遍历恢复一棵树，
# leetcode 105 和 106题目解答，这道题目其实本质就是二叉树的前序遍历（先处理后递归的操作）
# 难度medium
# Author:       zhengyiming
# Date:         2020/10/8
# -------------------------------------------------------------------------------

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def restructTree(pre_order, inorder):
    if len(pre_order) == 0:
        return None
    elif len(pre_order) == 1:
        return TreeNode(pre_order[0])
    else:
        root_val = pre_order[0]
        pivot = inorder.index(root_val)  # 假设元素不重复
        root = TreeNode(root_val)
        root.left = restructTree(pre_order[1:pivot + 1], inorder[:pivot + 1])
        root.right = restructTree(pre_order[pivot + 1:], inorder[pivot + 1:])
        return root


def pre_print(root):
    if root is None:
        return
    else:
        print(root.val)
        pre_print(root.left)
        pre_print(root.right)


def post_print(root):
    if root is None:
        return
    else:
        pre_print(root.left)
        pre_print(root.right)
        print(root.val)


# ----- 根据后续遍历和中序遍历恢复一棵树
def restructTree2(postorder, inorder):
    if len(pre_order) == 0:
        return None
    elif len(pre_order) == 1:
        return TreeNode(postorder[-1])
    else:
        root_val = postorder[-1]
        pivot = inorder.index(root_val)  # 假设元素不重复
        root = TreeNode(root_val)  # 主要是这个的不同
        root.left = restructTree(postorder[:pivot], inorder[:pivot + 1])
        root.right = restructTree(postorder[pivot:-1], inorder[pivot + 1:])  # 这儿取的时候要把末尾的根结点去掉，找对对应的左右子节点的序列
        return root


if __name__ == '__main__':
    pre_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G']  # 前序
    in_order = ['C', 'B', 'D', 'A', 'E', 'G', 'F']  # 中序
    post_order = ["B", "C", "D", "E", "F", "G", "A"]  # 后序
    root = restructTree(pre_order, in_order)
    root2 = restructTree2(post_order, in_order)
    pre_print(root)
    print()
    pre_print(root2)

