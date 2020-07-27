'''
author: zhengyiming
date: 2020-07-23
factory 工厂模式
Django中的表单就是使用工厂模式类中的字段约束
'''

class iphone:
    def __init__(self):
        self._name = ""

    @property
    def phone_name(self):
        return self._name
    
    @phone_name.setter
    def phone_name(self,name):
        if isinstance(name, int) or isinstance(name, str) or isinstance(name, float):
            raise ValueError('Name must be type of "str" or "float" or "int"')
        elif len(name)==0:
            raise ValueError('Name cant be "" ')
        self._name=name

    def __str__(self):
        return "your iphone name is {}".format(self._name)


class android:
    def __init__(self):
        self._name = ""

    @property
    def phone_name(self):
        return self._name
    
    @phone_name.setter
    def phone_name(self,name):
        if isinstance(name, int) or isinstance(name, str) or isinstance(name, float):
            raise ValueError('Name must be type of "str" or "float" or "int"')
        elif len(name)==0:
            raise ValueError('Name cant be "" ')
        self._name=name

    def __str__(self):
        return "your android name is {}".format(self._name)


def phoneFactory(phone_code):  # phone_code like "iphone_zhengyiming"
    if phone_code.split("_")[0] == "iphone":
        phone_maker = iphone  # 直接指向了类，未生成对象
    elif phone_code.split("_")[0] == "android":
        phone_maker = android
    else:
        print("we dont know your phone")
    your_phone = phone_maker()
    your_phone._name = phone_code.split("_")[-1]
    return your_phone

# 抽象的工厂方法
# 比如适配不同的操作系统的东西等，就非常的实在的例子,可以这样写两个独立的类，然后使用工厂模式来隐藏细节，
# 抽象工厂设计模式是一种一般化的工厂方法
# 总的来说，一个抽象工厂是一些工厂方法的
# （逻辑）集合，其中每一个工厂方法负责生成
# 种不同的对象

import sys
class Linux_python:
    def __init__(self):
        self._system_name = "Welcome you download this on linux_system"

    def __str__(self):
        return self._system_name

class Win_python:
    def __init__(self):
        self._system_name = "Welcome you download this on Window_system"

    def __str__(self):
        return self._system_name

# 抽象工厂类
class System_environment:
    def __init__(self,factory):
        self.environment = factory()
    
    def hello(self):
        print(self.environment)


# 主函数调用
def abstract_main():
    factory = Win_python if str(sys.platform).find("win") != -1 else Linux_python
    system_hello = System_environment(factory)
    # print(system_hello)
    system_hello.hello()


        



if __name__ == '__main__':
    print("工厂方法")
    print(phoneFactory("iphone_zhengyiming"))
    print(phoneFactory("android_zhengyiming"))
    print("抽象工厂方法")
    abstract_main()