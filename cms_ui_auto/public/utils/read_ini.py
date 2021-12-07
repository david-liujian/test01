#coding=utf-8
from configparser import ConfigParser
from config.config import *
import os
# 如果没有的同学需要安装下载，在dos窗口输入：pip install configparser

class  Read_Ini(ConfigParser):

    def __init__(self,filename):
        super(Read_Ini, self).__init__()            #输入一个super ，默认会继承父类的构造函数
        self.read(filename)                        #configparser里面自带的read方法，读取这个文件

    def  read_data_ini(self,section,option):       #定义一个方法，来获取文件中的值，需要传入两个参数 section和option
        value=self.get(section,option)           #configparser里面自带的  get方法，来获取文件的内容
        return value                         #反馈到函数的调用出

if __name__ == '__main__':
    file=os.path.join(data_path,"data.ini")
    print(file)
    r=Read_Ini(file)
    print(r.read_data_ini("test_data","username"))















