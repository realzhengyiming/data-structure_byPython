# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     5 - 顺序队列   
   Description :  
   Author :        zhengyimiing 
   date：          2019/9/3 
-------------------------------------------------
   Change Activity:
                   2019/9/3
        队列的顺序存储结构，循环队列（这样才不会一直后移
    然后内存不够。循环，队列内的空间一定。
    类似scrapy 的分布式使用的redis队列，就是队列的结构.
    循环队列中这儿入队时候采用队尾下标加1 ，从尾部进来，
    而队头front下标不变，只有出队front+1
-------------------------------------------------
"""

__author__ = 'zhengyimiing'

# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     3 - 顺序栈
   Description :  
   Author :        zhengyimiing 
   date：          2019/9/5
-------------------------------------------------
   Change Activity:
                   2019/9/5
-------------------------------------------------
"""
__author__ = 'zhengyimiing'

import unittest
from abc import ABC, abstractmethod


class cirQueueImplement(ABC):
    @abstractmethod
    def __init__(self, **kwargs):  # 有参和无参都可以使用同一个
        '''please implements in subclass'''

    @abstractmethod
    def Enqueue(self, val):
        '''please implements in subclass'''

    @abstractmethod
    def Dequeue(self):
        '''please implements in subclass'''

    @abstractmethod
    def Getqueue(self):
        '''please implements in subclass'''

    @abstractmethod
    def Empty(self):
        '''please implements in subclass'''

    @abstractmethod
    def Full(self):
        '''please implements in subclass'''

    @abstractmethod
    def PrintList(self):  # 打印所有的值
        '''please implements in subclass'''




class cirQueue(cirQueueImplement):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # 父类的继承
        if kwargs.get("maxLength") is not None or kwargs.get("maxLength") == 0:
            self.maxLength = kwargs.get("maxLength")
        self.dataList = ["*" for i in range(self.maxLength)]  # 预先设置好初始长度为100的顺序线性表。
        self.front = self.rear = self.maxLength - 1  # 这儿是初始化一个长度为100的顺序结构的循环丢列
        if kwargs.get('dataList') is not None:  # 这个就是入队的操作嘛
            tempdataList = kwargs.get('dataList')
            for i in tempdataList:
                print(i)
                self.Enqueue(i)

    def PrintList(self):
        templist = []
        tempfront = self.front  # 因为是循环队列，所以这儿需要使用指针来进行下标的移动。
        while tempfront != self.rear:  # 如果队列空了，那就退出
            tempfront = (tempfront+1) % self.maxLength
            templist.append(self.dataList[tempfront])
        return templist

    def Enqueue(self, val):   # 从尾部入队
        assert val!=None, "入队的不能为空值"
        assert (self.rear+1)%self.maxLength != self.front ,"队列已经满了，不能入队"
        self.rear = (self.rear+1) % self.maxLength
        self.dataList[self.rear] = val

    def Dequeue(self):  # 先入先出。
        assert (self.rear != self.front),"队列为空，不能出队"
        self.front = (self.front + 1) % self.maxLength
        return self.dataList[self.front % self.maxLength]
        # 因为每次都是读取front下一位的，所以这样是没问题的，front 和 raar 差1

    def Empty(self):  # 在某个位中插入
        if self.rear == self.front:
            return True
        else:
            return False

    def Full(self):
        print(f"front:{self.front},rear:{self.rear},除法结果:{(self.rear+1) % self.maxLength}")
        if (self.rear+1) % self.maxLength:
            return True
        else:
            return False

    def Getqueue(self):
        assert (self.rear!=self.front),"队列为空，不能出队"
        temp_front =  self.front + 1
        return self.dataList[temp_front % self.maxLength]



class cirQueueTestCase(unittest.TestCase):
    '''测试 book_function.py'''

    def test_Print(self):
        '''测试 Print函数'''
        a = cirQueue(dataList=['a', 'b', 'c', 'd'], maxLength=5)
        self.assertEqual(a.PrintList(), ['a', 'b', 'c', 'd'])

    def test_Enqueue(self):
        '''测试 Enqueue函数'''
        a = cirQueue(dataList=['a', 'b', 'c', 'd'], maxLength=6)
        a.Enqueue("😁")
        a.PrintList()
        self.assertEqual(a.PrintList(), ['a', 'b', 'c', 'd', "😁"])   # 这儿因为front 和 rear 是隔开1个位置的，有一个位置是不能使用的。

    def test_Dequeue(self):
        '''测试 Dequeue'''
        a = cirQueue(dataList=['a', 'b', 'c', 'd'], maxLength=5)
        a.Dequeue()
        self.assertEqual(a.PrintList(), ['b', 'c', 'd'])

    def test_Full(self):
        '''测试 Full'''
        a = cirQueue(dataList=['a', 'b', 'c', 'd'], maxLength=6)  # 这边也是一样的道理，存4个就需要5个存储空间的位置，1个用来做固定距离
        from pprint import pprint
        a.Enqueue("x")
        pprint(a.PrintList())
        self.assertEqual(a.Full(), True) # todo full 和Empty判断错误。插入的报错也没有说出来

    def test_Empty(self):
        '''测试 Empty'''
        a = cirQueue(maxLength=4)
        self.assertEqual(a.Empty(), True)


if __name__ == '__main__':
    unittest.main()
