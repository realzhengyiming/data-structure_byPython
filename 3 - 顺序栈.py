# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     3 - 顺序栈
   Description :  
   Author :        zhengyimiing 
   date：          2019/9/1 
-------------------------------------------------
   Change Activity:
                   2019/9/1
        线性结构，并且后入先出，也就需要一个指针一直放在栈顶，
    只在表尾进行插入和删除操作。
    顺序栈是顺序表的简化
    运用：
    1）比如安卓app开发中的各个界面的切换的生命周期。
    2）或者就是一个桶，装书......
-------------------------------------------------
"""
# todo 设置长度的，需要
__author__ = 'zhengyimiing'

import unittest
from abc import ABC, abstractmethod



class SepStackImplement(ABC):
    @abstractmethod
    def __init__(self,**kwargs):  # 有参和无参都可以使用同一个
        '''please implements in subclass'''

    @abstractmethod
    def Push(self,val):  
        '''please implements in subclass'''

    @abstractmethod  
    def GetTop(self):
        '''please implements in subclass'''

    @abstractmethod
    def Pop(self):  
        '''please implements in subclass'''

    @abstractmethod
    def Empty(self):  
        '''please implements in subclass'''

    @abstractmethod
    def PrintList(self):  # 打印所有的值
        '''please implements in subclass'''

maxLength=100  # 顺序表式定长的


class SepStack(SepStackImplement):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # 父类的继承
        self.dataList = ["*" for i in range(100)]  # 预先设置好初始长度为100的顺序线性表。
        self.top = -1
        if kwargs.get('dataList') != None :
            tempdataList = kwargs.get('dataList')
            for i in range(len(tempdataList)):
                self.dataList[i] = tempdataList[i]
            self.top = len(tempdataList)-1  # 栈顶，顺序栈也是从0开始的下标


    def PrintList(self):
        templist = []
        top = self.top
        while top!= -1:  # 到栈底了,有这个好像其他的不会受到影响的
            print(self.dataList[top])  # todo 我就说没那么容易嘛，固定长度的。
            templist.append(self.dataList[top])
            top -=1
        return templist

    def Push(self,val):  
        assert val != None, "不能为空值"
        self.dataList[self.top+1] = val
        self.top += 1

    def GetTop(self):
        if not self.Empty():
            return self.dataList[self.top]
        else:
            return None

    def Pop(self):  
        if not self.Empty():
            temp = self.dataList[self.top]
            self.top -= 1
            return temp
        else:
            return None

    def Empty(self): 
        if self.top == -1:
            return True
        else:
            return False




class seqListTestCase(unittest.TestCase):
    '''测试 book_function.py'''

    def test_Print(self):
        '''测试 Print函数'''
        seqStack = SepStack(dataList=['a','b','c','d'])
        seqStack.PrintList()


    def test_Push(self):
        '''测试 Push'''
        seqStack = SepStack(dataList=['a','b','c','d'])
        seqStack.Push("👍")
        self.assertEqual(seqStack.PrintList(), ["👍",'d','c','b','a'])

    def test_Pop(self):
        '''测试 Pop'''
        seqStack = SepStack(dataList=['a','b','c','d'])
        seqStack.Pop()
        self.assertEqual(seqStack.PrintList(), ['c','b','a'])

    def test_Empty(self):
        '''测试 Empty'''
        seqStack = SepStack()
        self.assertEqual(seqStack.Empty(), True)

    def test_GetTop(self):
        '''测试 Gettop'''
        seqStack = SepStack(dataList=['a','b','c','d'])
        self.assertEqual(seqStack.GetTop(), "d")



if __name__ == '__main__':
    unittest.main()

