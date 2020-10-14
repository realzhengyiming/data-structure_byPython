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
# 不重复的东西,树的节点，又是和二叉树相关，只要涉及到 递归，
import copy

track = []  # 默认设置为,可选择列表 1，2，3 默认
res = []  # 已做的选择列表  ,显示还是隐式的进行相关的操作都是可以的
nums = 3
result = []


# 1.全排列的解决
def template(input):
    result = []  # 这里用列表来处理这个东西

    # 函数的函数
    def trace(path, choices):
        # 结束条件
        if len(path) == len(input):
            result.append([path.copy()])  # 一条路径回溯到底才添加进来，这样又涉及到深拷贝浅拷贝了。这种情况如果使用[]那就是浅拷贝，后面的pop会清空；list则返回一个新的
            # result.append(list(path))  # 一条路径回溯到底才添加进来，这样又涉及到深拷贝浅拷贝了。这种情况如果使用[]那就是浅拷贝，后面的pop会清空；list则返回一个新的
            return

            # 做选择
        for item in choices:
            if item in path:  # 排除不合法的，做选择
                continue
            path.append(item)  # 前面没选过这个的话那就添加进来
            trace(path, choices)  # 路径迭代
            path.pop()  # 撤销选择的操作（回溯）核心名词在这里

    trace([], input)  # 运行函数，默认的path是空的，没做任何选择
    return result


# 2.N 皇后
res = []


def N_queen(n):
    def check(board, row, col):
        '''
        是否可以在board row（index），col上放置皇后；因为这儿的board是list
        :param board: 是一个list ，里面的index 代表row， value代表 col；其实算是二维数据了
        :param row:  行
        :param col:  列
        :return: True/False
        '''

        # print(board)
        # print(row)
        # print(col)
        # print()
        for i_row in range(row):  #
            列重合 = abs(board[i_row] - col)  # 发生重合就不行
            左斜线或者右斜线的距离 = abs(i_row - row)
            if abs(board[i_row] - col) == 0:  # 列不能重复
                return False
            if abs(board[i_row] - col) == abs(i_row - row):  # 相等时候距离为斜线距离内
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
            # print(row)
            # print(temp)
            res.append(copy.deepcopy(board))  # 要做一个深拷贝,不然就只保留了最后一下的结果了
            for i, col in enumerate(board):  # 这个方法是返回下标+col列
                print('□ ' * col + '■ ' + '□ ' * (len(board) - 1 - col))  # 这种是
            print("")
        # 2.遍历选择，做选择
        for col in range(border):  # 这儿是按列来遍历，每次递归进来列都是0，开始
            if check(board, row, col):  # 3.判断是有有效，无效就取消这个选择。重新做选择，那这个就叫回溯
                board[row] = col
                eightqueen(board, row + 1)  # 4.递归
                # 这儿没有显示回溯，其实是有回溯的，只是因为这儿的board直接是用index 当成row，value当成col，所以不用再使用"*"填充了
                # 这儿是一纬数组，用二维数组的board[row][col]应该更好的理解，那样就可以默认先填充"*"，然后再填充"Q"

    board = [0 for i in range(n)]  # n条边的情况
    eightqueen(board, 0)  # 默认从0行开始，不知道怎么看就一步一步来运行。《变量要知道代表什么，然后就可以操作了》
    print("res 是什么")
    print(res)


def N_queen2(n):
    # 创建一个二维数组board =
    board = [["*" for col in range(n)] for row in range(n)]
    # print(board)
    res = []

    def put_queen(board, row):  # 从row 0 开始遍历
        # 1.停止条件
        if row >= len(board):
            res.append(copy.deepcopy(board))  # 把这个结果放进去  ，果然是python神拷贝，浅拷贝的问题
            # return 这儿不返回，是因为不是迭代的返回，回滚不通过这样的操作，结果还可能很多呢
        for col in range(len(board)):  # 每一行的每一列来进行开始操作
            if not check_position(board, row, col):  # 排除不合法的选择
                continue  # 继续循环
            # 2.做选择
            board[row][col] = "Q"  # 放置皇后
            # 3.进入下一步决策
            put_queen(board, row + 1)
            # 4. 撤销选择
            board[row][col] = "*"
            # 因为这儿有一个撤销的操作，所以必须要深拷贝，
            # 也可以不要这个的。不过为了保持那个结构好理解
            # 还是带上好

    def check_position(board, row, col):  # 检查这个位置可不可以再放置皇后；竖直下来，还有斜着的,这儿不是
        for row_ in range(len(board[:row + 1])):
            for col_ in range(len(board)):
                if board[row_][col_] == "Q":  # 列放置列Q那就不行
                    if col - col_ == 0:
                        return False
                    if abs(col - col_) == abs(row - row_):
                        return False  # 没绝对值的就分成两个式子
        return True

    put_queen(board, row=0)
    for u in res:
        print(u)
        print()
    # return res

# todo 随机生成一个迷宫，然后再使用回溯算法，探索出迷宫的路，生成路
# todo 水满寻路算法，叫什么给忘记了，可以多线程，多方向进行寻路的吧。

if __name__ == '__main__':
    # nums = 3
    # backtrack(3)

    # 这个是全排列的
    # result = template([1, 2, 3])
    # print(result)

    # 这个是n皇后
    # N_queen(4)

    # 这个是N皇后，使用二维数组的，更加清晰一点
    N_queen2(4)
