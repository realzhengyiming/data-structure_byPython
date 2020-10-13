# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         backtrace
# Description:
# Author:       zhengyiming
# Date:         2020/10/10
# -------------------------------------------------------------------------------

# from labuladong
# 回溯算法的框架
# 都长得一个样的回溯算法

# result = []
# def backtrack(路径, 选择列表):
#     if 满⾜结束条件: result.add(路径) （1）结束条件
#         return
#     for 选择 in 选择列表: （2）做选择
#         做选择
#         backtrack(路径, 选择列表) （3） 递归
#         撤销选择  （4）撤销选择

# for循环内的递归，递归之前做选择，递归之后 撤销选择。
# 不重复的东西,树的节点


track = []  # 默认设置为,可选择列表 1，2，3 默认
res = []  # 已做的选择列表  ,显示还是隐式的进行相关的操作都是可以的
nums = 3
result = []


# 1.全排列的解决
def template(input):  # 输入一个正整数n，用来做什么的呢
    result = []

    # 函数的函数
    def trace(path, choices):
        # 结束条件
        if len(path) == len(input):
            # print("到底部了")
            # print(path)
            result.append([path.copy()])  # 一条路径回溯到底才添加进来，这样又涉及到深拷贝浅拷贝了。这种情况如果使用[]那就是浅拷贝，后面的pop会清空；list则返回一个新的
            # result.append(list(path))  # 一条路径回溯到底才添加进来，这样又涉及到深拷贝浅拷贝了。这种情况如果使用[]那就是浅拷贝，后面的pop会清空；list则返回一个新的
            return

            # 做选择
        for item in choices:
            if item in path:
                continue  # 简直操作
            path.append(item)  # 前面没选过这个的话那就添加进来
            trace(path, choices)  # 路径回溯
            path.pop()  # 递归出来后回溯

    trace([], input)  # 运行函数，默认的path是空的，没做任何选择
    return result


# 2.N 皇后
def N_queen(n):
    def check(board, row, col):  # 这个检查当前放置位置放置皇后行不行
        i = 0
        for i in range(row):
            if abs(board[i] - col) == 0 or abs(board[i] - col) == abs(i - row):
                return False
        return True

    def eightqueen(board, row):  # 8皇后，当然这儿可不一定要8皇后
        '''
        :param board: 这个是设置的棋盘的长宽n*n
        :param row: 当前放置第几行的皇后
        :return:
        '''
        border = len(board)
        if row >= border:  # 1.结束条件
            temp = board
            print(temp)
            for i, col in enumerate(board):  # 这个方法是返回下标+col列
                print('□ ' * col + '■ ' + '□ ' * (len(board) - 1 - col))  # 这种是
            print("")
            return temp
        col = 0
        while col < border:  # 2.遍历选择，做选择
            for col in range(border):
                if check(board, row, col):  # 3.判断是有有效，无效就取消这个选择。重新做选择，那这个就叫回溯
                    board[row] = col
                    eightqueen(board, row + 1)  # 4.递归
            col += 1

    board = [0 for i in range(n)]  # n条边的情况
    result = eightqueen(board, 0)
    return result

# todo 水满寻路算法，叫什么给忘记了，可以多线程，多方向进行寻路的吧。

if __name__ == '__main__':
    # nums = 3
    # backtrack(3)

    # 这个是全排列的
    # result = template([1, 2, 3])
    # print(result)

    # 这个是n皇后
    N_queen(4)
