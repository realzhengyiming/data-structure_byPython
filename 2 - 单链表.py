# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     2 - 单链表   
   Description :   单链表
   Author :        zhengyimiing 
   date：          2019/8/31 
-------------------------------------------------
   Change Activity:
                   2019/9/1
        单链表的特点就是 LinkList 里面属性只有一个头节点，
    所以求长度，遍历都是从头节点开始，头节点不存储数据。
        单链表是为了克服 1 - 顺序表.py 存储结构静态存储分配
    造成的缺点，而改进儿来的动态存储分配的线性表。

    差不多的还有双链表，还有循环链表
-------------------------------------------------
"""
import unittest

__author__ = 'zhengyimiing'

from abc import ABC, abstractmethod


class Node:  # 节点类
    countNode = 0
    def __init__(self, val, next = None):  # 默认值头节点为0
        self.data = val
        self.next = next
        Node.countNode += 1

    def __repr__(self):
        return f"data: { self.data }  {Node.countNode}"

class LinkListImplement(ABC):
    @abstractmethod
    def __init__(self,**kwargs):  # 有参和无参都可以使用同一个
        '''please implements in subclass'''

    @abstractmethod
    def Length(self):  # 按位查找
        '''please implements in subclass'''

    @abstractmethod  # 返回线性表的长度
    def Get(self, index):
        '''please implements in subclass'''

    @abstractmethod
    def Locate(self, _data):  # 按值查找位
        '''please implements in subclass'''

    @abstractmethod
    def Insert(self, index, val):  # 在某个位中插入
        '''please implements in subclass'''

    @abstractmethod
    def Delete(self, index):  # 删除某个位置的值
        '''please implements in subclass'''

    @abstractmethod
    def DeleteAll(self, _data):  # 删除某个位置的值
        '''please implements in subclass'''

    @abstractmethod
    def PrintList(self):  # 打印所有的值
        '''please implements in subclass'''


class LinkList(LinkListImplement):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # 父类的继承
        self.head = Node(val = None,next=None)  # 单链表头指针
        if kwargs.get('dataList') != None :
            dataList = kwargs.get('dataList')
            # 头插法构建单链表
            p = self.head   # 头节点不存储数据
            for i in range(len(dataList)):
                node = Node(val = dataList[i],next=None)  # python中的指针，就是一个东西的别名
                p.next = node
                p = node   # 工作指针


    def PrintList(self):
        p = self.head
        templist = []
        while 1:
            p = p.next
            templist.append(p.data)
            if p.next == None:
                break
        return templist

    def Length(self):  # 按位查找
        p = self.head
        count = 0
        while p.next != None:
            p = p.next
            count += 1
        return count

    def Get(self, index):
        p = self.head
        count = 0
        while p.next != None:
            p = p.next
            count += 1
            if index == count:
                return p.data
        return None  # 没有找到

    def Locate(self, _data):  # 按值查找位
        p = self.head
        tempList = []
        count = 0
        while p.next != None:
            p = p.next
            count += 1
            if p.data == _data:
                tempList.append(count)
        return tempList  # 返回位的序号的列表

    def Insert(self, index, val):  # 在某个位中插入
        p = self.head
        count = 0
        while p.next != None:
            p = p.next
            count += 1
            if index == count:
                node = Node(val = val,next = p.next)
                p.next =node
                break

    def Delete(self, index):  # 删除某个位置的值
        # python 有自动的垃圾回收，所以当一个对象的引用计数为0个时就不用管了，资源自动回收
        p = self.head
        count = 0
        while p.next != None:
            p = p.next
            count += 1
            if index == count+1:
                p.next = p.next.next # 改链接就可以了,这儿改链接
                break

    def DeleteAll(self, _data):  # 按值删除
        p = self.head
        while p.next != None:  # 最后一位的时候，怎么处理 todo
            preNode = p
            print(preNode)
            p = p.next  # 移动到当前位置。
            if _data == p.data:
                preNode.next = p.next  # 改链接就可以了
                p = preNode
                # 工作指针这时候应该移动回前一个去，
                # 因为后面的那个还需要继续判断是不是需要删除的


class seqListTestCase(unittest.TestCase):
    '''测试 book_function.py'''

    def test_Print(self):
        '''测试 Print函数'''
        seqlist = LinkList(dataList = ["a", "b", "c", "d","1","2","3"])
        print(seqlist.PrintList())
        self.assertEqual(seqlist.PrintList(), ["a", "b", "c", "d","1","2","3"])

    def test_Insert(self):
        '''测试 Insert函数'''
        linkList = LinkList(dataList = ["a", "b", "c", "d"])
        # 添加一个插入的
        linkList.Insert(2,"😁")
        print(linkList.PrintList())
        self.assertEqual(linkList.PrintList(), ["a", "b","😁","c", "d"])

    def test_Length(self):
        '''测试读取长度'''
        linkList = LinkList(dataList = ["a", "b", "c", "d"])
        self.assertEqual(linkList.Length(), 4)

    def test_Get(self):
        '''按位查找，从1开始'''
        linkList = LinkList(dataList=["a", "b", "c", "d"])
        self.assertEqual(linkList.Get(2), "b")

    def test_Location(self):
        '''按值查找，从1开始'''
        linkList = LinkList(dataList=["a", "b", "c", "d","d"])
        self.assertEqual(linkList.Locate("d"), [4,5])

    def test_Delete(self):
        '''按位删除'''
        linkList = LinkList(dataList=["a", "b", "c", "d","d"])
        linkList.Delete(2)
        self.assertEqual(linkList.PrintList(), ["a", "c", "d","d"])

    def test_DeleteAll(self):
        '''按位删除'''
        linkList = LinkList(dataList=["a", "b", "c", "d","d",'d'])
        linkList.DeleteAll("d")
        print(linkList.PrintList())
        self.assertEqual(linkList.PrintList(), ["a", "b", "c"])


if __name__ == '__main__':
    unittest.main()


