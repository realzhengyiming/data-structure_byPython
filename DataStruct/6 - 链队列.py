# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     6 - 链队列   
   Description :  
   Author :        zhengyimiing 
   date：          2019/9/6 
-------------------------------------------------
   Change Activity:
                   2019/9/6
        单链表的简化，复用单链表的类结构之类的。也采用有
    头节点的方式，然后再增加一个尾节点。方便入队的操作，
    指向尾部 。佛系投简历，有就去，没有就继续复习写
    代码😂
-------------------------------------------------
"""

__author__ = 'zhengyimiing'


import unittest
from abc import ABC, abstractmethod


class Node:  # 节点类

    def __init__(self, val, next = None):  # 默认值头节点为0
        self.data = val
        self.next = next

    # def __repr__(self):
    #     return f"data: { self.data }  {Node.countNode}"


class linkQueueImplement(ABC):
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
    def PrintList(self):  # 打印所有的值
        '''please implements in subclass'''


class linkQueue(linkQueueImplement):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # 父类的继承
        self.head = Node(val=None, next=None)  # 单链表头指针
        self.rear = self.head
        if kwargs.get('dataList') is not None:
            dataList = kwargs.get('dataList')
            # 头插法构建单链表
            p = self.head  # 头节点不存储数据
            for i in range(len(dataList)):
                node = Node(val=dataList[i], next=None)  # python中的指针，就是一个东西的别名
                p.next = node
                p = node  # 工作指针 ，最后一位的时候 p指向结尾的最后一个的节点
            self.rear = p

    def PrintList(self):
        p = self.head
        templist = []
        while 1:
            p = p.next
            templist.append(p.data)
            if p.next == None:
                break
        return templist

    def Enqueue(self, val):  # 指定尾部插入
        if self.rear is None:  # 空队列的话是None
            node = Node(val=val, next=None)
            self.head.next = node
            self.rear = node  # 改成指向最后一个元素
        else:
            node = Node(val=val, next=None)
            self.rear.next = node
            self.rear = node  # 改成指向最后一个元素

    def Dequeue(self):
        temp = self.head.next
        self.head = temp  # 头节点也后移，头节点上的数据不用，所以不影响
        return temp.data

    def Empty(self):
        if self.rear is self.head:
            return True
        return False

    def Getqueue(self):  # 只获得队头元素
        return self.head.next.data


class linkQueueTestCase(unittest.TestCase):
    '''测试 book_function.py'''

    def test_Print(self):
        '''测试 Print函数'''
        a = linkQueue(dataList = ["a", "b", "c", "d","1","2","3"])
        print(a.PrintList())
        self.assertEqual(a.PrintList(), ["a", "b", "c", "d","1","2","3"])

    def test_Enqueue(self):
        '''测试 Enqeue函数'''
        a = linkQueue(dataList = ["a", "b", "c", "d","1","2","3"])
        print(a.Enqueue("😀"))
        self.assertEqual(a.PrintList(), ["a", "b", "c", "d","1","2","3","😀"])

    def test_Dequeue(self):
        '''测试 Dequeue'''
        a = linkQueue(dataList = ["a", "b", "c", "d","1","2","3"])
        print(a.Dequeue())
        self.assertEqual(a.PrintList(), [ "b", "c", "d","1","2","3"])

    def test_Empty(self):
        '''测试 Empty'''
        a = linkQueue()
        self.assertEqual(a.Empty(), True)

    def test_GetQueue(self):
        '''测试 GetQueue'''
        a = linkQueue(dataList=["a", 'b'])
        self.assertEqual(a.Getqueue(), "a")


if __name__ == '__main__':
    unittest.main()