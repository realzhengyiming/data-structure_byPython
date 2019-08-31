# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     1 - 顺序表
   Description :  
   Author :        zhengyimiing 
   date：          2019/8/30 
-------------------------------------------------
   Change Activity:
                   2019/8/30
    # 此程序使用python实现顺序表的数据结构，然后使用unittest来对各功能进行检验
    
    顺序表的缺点：
    （1）插入和删除需要移动大量的元素
    （2）表的容量难以确定，长度需要事先确定
    （3）造成存储空间的碎片
-------------------------------------------------
"""
import unittest

__author__ = 'zhengyimiing'




from abc import ABC, abstractmethod


class seqListImplement(ABC):  # 接口类确定接口
    @abstractmethod
    def __init__(self):
        '''please implements in subclass'''

    @abstractmethod
    def __init__(self, alist, n):  # 含参构造函数
        '''please implements in subclass'''

    @abstractmethod
    def Length(self):   
        '''please implements in subclass 获得长度'''

    @abstractmethod  # 按为查找
    def Get(self, index):
        '''please implements in subclass'''

    @abstractmethod
    def Locate(self, _data):  # 按值查找位
        '''please implements in subclass'''

    @abstractmethod
    def Insert(self, location, index):  # 在某个位中插入
        '''please implements in subclass'''

    @abstractmethod
    def Delete(self, index):  # 删除某个位置的值
        '''please implements in subclass'''

    @abstractmethod
    def DeleteAll(self, _data):  # 删除某个位置的值
        '''please implements in subclass'''

    @abstractmethod
    def Print(self):  # 打印所有的值
        '''please implements in subclass'''


class seqList(seqListImplement):

    def __init__(self):
        self.length = 0
        self.data = []

    def __init__(self, alist, n):
        self.length = n
        self.data = ["*" for i in range(100)]  # 预先设置好初始长度为100的线性表。
        for i in range(0, n):
            # print(alist[i])
            self.data[i] = alist[i]

    def Length(self):
        # return len(self.data)  # 这儿不用这种方法
        return self.length  # 直接返回就好了

    def Get(self, index):  # 按下标查找
        for i in range(self.length):
            if i == index:
                return self.data[i]

    def Locate(self, _data):  # 按值查找位
        assert _data  in self.data ,"查找的值不在顺序表中"
        result  = []
        for i in range(self.length):
            if _data == self.data[i]:
                result.append(self.data.index(_data))
        return result

    def Insert(self, index, _data):  # 在某个位中插入
        assert index < self.length-1, "插入的下标越上界"  # 下标是长度-1
        assert index >= 0, "插入的下标越下界"
        tempLength = self.length-1
        for i in range(tempLength,index-1,-1):  # 使用 range生成逆序注意range(4,2,-1) ->> 4,3 所以末尾要再减小一点
            self.data[i+1] = self.data[i]  # 从最后面一个开始移动
        self.data[index] = _data
        self.length += 1
        print(f"插入成功，插入下标为： {index} 的地方插入值： {_data}")

    def Delete(self, index):  # 按下标删除
        assert index < len(self.data) ,"输入的位置越界，序号从0开始"
        assert index >= 0, "输入的位置越界，序号从0开始"
        for i in range(index,self.length):  # 起始下标，末尾下标
            self.data[i] = self.data[i+1]
        self.length -= 1
        print(f"删除成功")


    def DeleteAll(self, _data):  # 删除这个值的数据
        '''please implements in subclass'''
        assert _data in self.data ,"输入的值不在顺序表内"
        for i in range(self.length): # 找到一个就可以了
            if self.data[i] == _data:
                # 获得下标
                for jj in range(i,self.length):
                    self.data[jj] = self.data[jj+1]
                self.length -= 1
                try :
                    self.DeleteAll(_data) # 递归
                except Exception as e:
                    print("结束迭代")
                    break
                break
                # self.Delete(i)




    def Print(self):
        tempdata = []
        for i in self.data:
            if i != "*":
                print(i)
                tempdata.append(i)
            else:
                break
        return tempdata


class seqListTestCase(unittest.TestCase):
    '''测试 seqlist function.py'''

    def test_seqListPrint(self):
        '''测试 Print函数'''
        print("1.初始化顺序表")
        seqlist = seqList(["a", "b", "c", "d"], 4)
        # result = to_read('现代艺术150年 : 一个未完成的故事')
        # self.assertEqual(result, '我想读《现代艺术150年 : 一个未完成的故事》咯')
        self.assertEqual(seqlist.Print(), ["a", "b", "c", "d"])

    def test_seqListInsert(self):
        '''测试 Insert'''
        seqlist = seqList(["a", "b", "c", "d"], 4)
        seqlist.Insert(2, "😀")
        self.assertEqual(seqlist.Print(), ["a", "b","😀", "c", "d"])

    def test_seqListDelete(self):
        '''测试 Delete'''
        seqlist = seqList(["a", "b", "c", "d"], 4)
        seqlist.Delete(2)
        self.assertEqual(seqlist.Print(), ["a", "b",  "d"])

    def test_seqlistGet(self):
        '''测试Get函数'''
        seqlist = seqList(["a", "b", "c", "d"], 4)
        self.assertEqual(seqlist.Get(2),"c")

    def test_seqlistLocation(self):
        '''测试Location函数'''
        seqlist = seqList(["a", "b", "c", "d"], 4)
        self.assertEqual(seqlist.Locate("d"),[3])

    def test_seqlistLength(self):
        '''测试Location函数'''
        seqlist = seqList(["a", "b", "c", "d"], 4)
        self.assertEqual(seqlist.Length(),4)

    def test_seqlistDeleteAll(self):
        '''测试Location函数'''
        seqlist = seqList(["a", "a", "a", "d","a","a"], 6)
        seqlist.DeleteAll("a")
        self.assertEqual(seqlist.Print(),["d"])
        self.assertEqual(seqlist.Length(),1)


if __name__ == '__main__':
    unittest.main()
    # list.insert()