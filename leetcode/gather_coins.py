# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         gather_coins
# Description:  凑硬币问题，动态规划：最优子结构，边界，状态转移方程
# Author:       zhengyiming
# Date:         2020/10/10
# -------------------------------------------------------------------------------
import time


def g_coins(n, coins) -> int:
    '''
    :param n:  总共要凑的钱数量
    :param coins:  总共有的硬币的可选择的列表[1,3,5]
    :return: -1(凑不了); 0 (凑的钱为0，也不用凑）；m凑到的所需要的最少的硬币的数
    '''
    if n < 0:
        return -1
    elif n == 0:
        return 0  # 0也算是个数字，最少
    else:
        res_min = n  # 这个值是随便设置的吗。如果n是1呢
        for coin in coins:
            subproblem = g_coins(n - coin, coins)
            if subproblem == -1:
                continue  # 不能凑就跳过咯
            res_min = min(subproblem + 1, res_min)  # 每次都记录子问题都最少凑硬币的个数
        if res_min != -1:
            return res_min  # 这个就是这个问题规模内最少凑到的硬币的数量


temp_caching = {}  # 长度不知道啊，怎么用列表,用哈希表把


def g_coins_caching(n, coins) -> int:  # 加上了缓存
    '''
    :param n:  总共要凑的钱数量
    :param coins:  总共有的硬币的可选择的列表[1,3,5]
    :return: -1(凑不了); 0 (凑的钱为0，也不用凑）；m凑到的所需要的最少的硬币的数
    '''
    if n in temp_caching.keys():
        return temp_caching[n]
    else:
        if n < 0:
            return -1
        elif n == 0:
            return 0  # 0也算是个数字，最少
        else:
            res_min = n  # 这个值是随便设置的吗。如果n是1呢
            for coin in coins:
                subproblem = g_coins(n - coin, coins)
                if subproblem == -1:
                    continue  # 不能凑就跳过咯
                res_min = min(subproblem + 1, res_min)  # 每次都记录子问题都最少凑硬币的个数
            if res_min != -1:
                temp_caching[n] = res_min  # 把这个最小的值放回去
                return temp_caching[n]  # 这个就是这个问题规模内最少凑到的硬币的数量


# DP_table 使用这个的呢，就变成了自低向顶来进行操作，迭代，就叫做动态规划
# 正向的去处理那个表
def g_coins_recurrence(n, coins):  # 迭代,这个效果并不差的
    # dp = {}
    dp = [n+1]*(n+1)
    # PS：为啥 dp 数组初始化为 amount + 1 呢，
    # 因为凑成 amount ⾦额的硬 币数最多只可能等于 amount （全⽤ 1 元⾯值的硬币）
    # 所以初始化为 amount + 1 就相当于初始化为正⽆穷，便于后续取最⼩值。
    print(dp)
    dp[0] = 0

    # base case
    for i in range(1, n + 1):  # 迭代有一个问题就是我怎么确定这个迭代的问题规模是多少
        # 内层for在求所有子问题 + 1 的最小值
        dp[i] = n + 1  # 这个只是随便先设置一个默认值的意思
        for coin in coins:
            if i - coin < 0:  # 子问题无解，跳过
                continue
            dp[i] = min(dp[i], 1 + dp[i - coin])
    return -1 if dp[n] == n + 1 else dp[n]  # python的三目运算


def dynamic(amount, num):
    # num = [1, 3, 5]
    # 设置一个字典存储{钱数，硬币个数}
    dict = {0: 0}
    for i in range(1, amount + 1):
        # 硬币个数肯定不会大于钱数，我们设置为amount+1，如果后期没有匹配则值还为amount+1，比较好判断
        dict[i] = amount + 1
        for j in num:
            if j <= i:
                # 最优子结构 状态转移方程   边界
                dict[i] = min(dict[i], dict[i - j] + 1)
    if dict[amount] == amount + 1:
        return -1
    else:
        # print(dict)
        # print(dict[amount])
        return dict[amount]


if __name__ == '__main__':
    n = 30
    start = time.time()
    result = g_coins(n, [1, 3, 5])  # 这个值是暴力算法
    step = time.time()

    print(result)
    print(f"用时 {step - start} ")
    print()
    result2 = g_coins_caching(n, [1, 3, 5])  # caching 使用备忘录的
    print(result2)
    step2 = time.time()
    print(f"用时 {step2 - step} ")

    print()
    result3 = dynamic(n, [1, 3, 5])  # 迭代
    print(result3)
    step3 = time.time()
    print(f"用时 {step3 - step2} ")

    print()
    result4 = g_coins_recurrence(n, [1, 3, 5])  # 迭代
    print(result4)
    step4 = time.time()
    print(f"用时 {step4 - step3} ")
