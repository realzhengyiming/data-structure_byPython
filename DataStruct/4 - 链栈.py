# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     4 - 链栈   
   Description :  
   Author :        zhengyimiing 
   date：          2019/9/2 
-------------------------------------------------
   Change Activity:
                   2019/9/2
        链栈的基本操作其实是单链表的基本操作的简化，
    只是把头指针改成了一直指向栈顶，并且链顺序倒过来
    输出即可。
-------------------------------------------------
"""

__author__ = 'zhengyimiing'


import unittest
from abc import ABC, abstractmethod

class Node:  # 节点类
    countNode = 0
    def __init__(self, val, next = None):  # 默认值头节点为0
        self.data = val
        self.next = next

    def __repr__(self):
        return f"data: { self.data }  {Node.countNode}"


class LinkStackImplement(ABC):
    @abstractmethod
    def __init__(self,**kwargs):  # 有参和无参都可以使用同一个
        '''please implements in subclass'''

    @abstractmethod
    def Push(self,val):
        '''please implements in subclass'''

    @abstractmethod
    def GetTop(self):  # 获得顶部的值，但是不删除值
        '''please implements in subclass'''

    @abstractmethod
    def Pop(self):  # 取出值
        '''please implements in subclass'''

    @abstractmethod
    def Empty(self):  # 测空
        '''please implements in subclass'''

    @abstractmethod
    def PrintList(self):  # 打印所有的值
        '''please implements in subclass'''


class LinkStack(LinkStackImplement):
    def __init__(self, **kwargs):
        self.top = None  # 头节点不存储数据
        super().__init__(**kwargs)  # 父类的继承
        if kwargs.get('dataList') != None:
            dataList = kwargs.get('dataList')
            # 头插法构建单链表
            for i in range(len(dataList)):
                if i == 0:
                    node = Node(val=dataList[i], next=None)  # python中的指针，就是一个东西的别名
                    self.top = node
                else:
                    node = Node(val=dataList[i], next=self.top)  # python中的指针，就是一个东西的别名
                    self.top = node

    def PrintList(self):
        templist = []
        top = self.top
        print()
        while top!= None:  # 到栈底了
            print(top.data)
            templist.append(top.data)
            top = top.next
        return templist

    def Push(self,val):
        assert val != None, "不能为空值"
        node  = Node(val = val,next = self.top)
        self.top = node

    def GetTop(self):
        if not self.Empty():
            return self.top.data
        else:
            return None

    def Pop(self):
        if not self.Empty():
            temp = self.top.data
            self.top  = self.top.next
            return temp
        else:
            return None

    def Empty(self):
        if self.top == None:
            return True
        else:
            return False


class seqListTestCase(unittest.TestCase):
    '''测试'''

    def test_Print(self):
        '''测试 Print函数'''
        linkStack = LinkStack(dataList=['a','b','c','d'])
        self.assertEqual(linkStack.PrintList(), ["d","c","b","a"])

    def test_Push(self):
        '''测试 push'''
        linkStack = LinkStack(dataList=['a','b','c','d'])
        linkStack.Push("😀")
        self.assertEqual(linkStack.PrintList(), ["😀","d","c","b","a"])

    def test_Pop(self):
        '''测试 pop'''
        linkStack = LinkStack(dataList=['a','b','c','😝'])
        print(linkStack.Pop())
        self.assertEqual(linkStack.PrintList(), ["c","b","a"])

    def test_Empty(self):
        '''测试 Empty'''
        linkStack = LinkStack()
        self.assertEqual(linkStack.Empty(), True)

if __name__ == '__main__':
    unittest.main()

