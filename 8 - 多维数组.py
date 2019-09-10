# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     8 - 多维数组   
   Description :  
   Author :        zhengyimiing 
   date：          2019/9/8 
-------------------------------------------------
   Change Activity:
                   2019/9/8
        多维到一维的映射(内存上的顺序存储结构)，矩阵可以
    存储多维的信息数据，如果知道了如何把矩阵这种结构映射
    到顺序结构中存储，那么就非常厉害了，因为矩阵是个好工
    具。
    1）按行优先就是把二维数组中的值，存入类似顺序表的一维数组中
    2）按行优先存储，同上。
-------------------------------------------------
"""

__author__ = 'zhengyimiing'

testList = range(50 * 50)
# 例如下面的二维数组，也可以理解成矩阵
# 初始位置 aij ，行宽度为h1，列宽度为h2
# 每一位的表示方法为 ai0j0(地址）+ i ( i0<=i<=h2 ,i 为行坐标，在第几个的位置上，行)
# 第n行， ai0j0(地址）+ (n-1)*h2+i ( i0<=i<=h2， i 为行坐标，在第几个的位置上，行;n 为列，第几列的意思，这样就完成了映射)
# 按行列来查找
# 1 2 3
# 4 5 6
# 7 8

# 例如把上面的矩阵存储到 顺序表中（因为内存都是顺序排列的）
#  行优先，先把行填满，后换行填，这儿就是把
arrayList = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, "*"]
]  # 假定上面的就是 二维数组 矩阵，把他们映射到一维数组中,暂时用"*"代表空值

import unittest
from abc import ABC, abstractmethod


class multi_arrayImpl(ABC):
    @abstractmethod
    def __init__(self, **kwargs):  # 有参和无参都可以使用同一个
        '''please implements in subclass'''

    @abstractmethod
    def Update(self, val, i, j):  # 这个是写操作，就是修改
        '''please implements in subclass'''

    @abstractmethod
    def Getdate(self, i, j):  # 输入第几行 i，第几列 j
        pass

    @abstractmethod
    def PrintList(self):  # 这个是读操作，读取全部
        '''please implements in subclass'''


class multi_array(multi_arrayImpl):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # 父类的继承
        if kwargs.get('array') is not None:  # 这个对格式要求很严格...大家只理解存储映射的意思就好
            arrayList = kwargs.get('array')  # 二维数组

            # 这儿的长度，宽度都是从1开始，1-2-3-4...-n
            self.h1 = len(arrayList[0])  # 行宽度，就是列数
            self.h2 = len(arrayList)  # 列宽度，合起来可以是一个矩形,
            # 这个是行数，就是列宽度
            self.seqlist = ["*"] * self.h1 * self.h2
            for i in range(0, len(arrayList)):
                for j in range(0, len(arrayList[i])):
                    self.seqlist[0 + (i) * self.h1 + j] = arrayList[i][j]  # 这个就是映射的下标，这儿也是从0开始的下标

    def PrintList(self):
        templist = []
        for i in range(self.h1):
            temp = []
            for j in range(self.h2):
                temp.append(self.seqlist[i * self.h1 + j])
            templist.append(temp)
        from pprint import pprint
        pprint(templist)
        pprint(self.seqlist)
        return templist

    def Update(self, val, i, j):  # 行优先的检索修改是这样就可以。核心映射方法
        assert i <= self.h1 - 1, "横坐标越界，此二维数组下标从0 开始"
        assert j <= self.h2 - 1, '纵坐标越界，此二维数组下标从 0 开始i'
        self.seqlist[i * self.h1 + j] = val

    def Getdate(self, i, j):
        assert i <= self.h1 - 1, "横坐标越界，此二维数组下标从0 开始"
        assert j <= self.h2 - 1, '纵坐标越界，此二维数组下标从 0 开始'
        return self.seqlist[i * self.h1 + j]


class linkQueueTestCase(unittest.TestCase):
    """测试 """

    def test_Print(self):
        """测试 Print函数"""
        a = multi_array(array=[
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', "*"]
        ])
        self.assertEqual(a.PrintList(), [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', "*"]
        ])

    def test_Get(self):
        """ 测试 获得某个位置的数据，函数 """
        a = multi_array(array=[
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', "*"]
        ])
        self.assertEqual(a.Getdate(2, 2), "*") # 输入的下标是从0开始的，

    def test_Update(self):
        """ 测试 更新某个位置的数据函数 """
        a = multi_array(array=[
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', "*"]
        ])
        a.Update(val="9",i=2,j=2)
        self.assertEqual(a.Getdate(2, 2), "9") # 输入的下标是从0开始的，


if __name__ == '__main__':
    unittest.main()
