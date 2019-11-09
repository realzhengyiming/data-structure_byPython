# coding =utf-8
# 使用基于装饰器的单例模式的例子  切面思想  可以用这个来代替调试时候的print 记录程序运行日志
import os
import sys



def Singleton(cls):  # 传进来的是一个类
    instances = {}  # 这儿用字典来存这个对象
    def getInstance(*args,**kw):
        if 'cls' not in instances:
            instances['cls'] = cls(*args,**kw)
            # 如果为创建过，那就创建一个对象放进去
        return instances['cls']
    return getInstance

@Singleton
class Logger:
    def __init__(self,dir_root,filename):
        self.filename = filename
        self.dir_root = dir_root # 输出日志的文件夹的位置
        path2=os.path.abspath('.')  # 表示当前所处的文件夹上一级文件夹的绝对路径
        print(path2)

        self.location = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), dir_root, self.filename) 

        # 这样就可以稳定的以这个文件夹为基准来进行文件的读写操作
        if  not os.path.exists(self.location):#如果路径不存在
            os.makedirs(self.location)
        print(f"Set the {self.location}")


    def _write_log(self, level, msg):
        '''write a log to the file and '''
        with open(self.location, "a") as log_file:
            log_file.write("[{0}]  {1}\n".format(level, msg))


    def critical(self, msg):
        self._write_log('CRITICAL', msg)


    def error(self, msg):
        self._write_log('ERROR', msg)


    def warn(self, msg):
        self._write_log('WARN', msg)


    def info(self, msg):
        self._write_log('INFO', msg)


    def debug(self, msg):
        self._write_log('DEBUG', msg)

    def getlocation(self):
        print("logger_的目录输出")
        print(os.getcwd())
        print(os.path.abspath(sys.argv[0]))
        print(os.path.dirname(os.path.realpath(__file__)))

        print()

if __name__ == '__main__':
    logger = Logger("None","logger.txt")
    logger.info("hello")
    logger.getlocation()



