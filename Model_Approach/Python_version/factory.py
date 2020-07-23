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
        if isinstance(value, int) or isinstance(value, str) or isinstance(value, float):
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
        if isinstance(value, int) or isinstance(value, str) or isinstance(value, float):
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


if __name__ == '__main__':
    print(phoneFactory("iphone_zhengyiming"))
    print(phoneFactory("android_zhengyiming"))