#coding=utf-8
from public.pages.basepage import Basepage
from selenium import  webdriver
from time import sleep
from public.utils.read_ini import Read_Ini
import  os
from config.config import *
import unittest
from public.pages.pages_element import Pages_element as P
file=os.path.join(data_path,"data.ini")
r=Read_Ini(file)
url=r.read_data_ini("test_data","url")
username=r.read_data_ini("test_data","username")
pwd=r.read_data_ini("test_data","pwd")


class  Test_login(Basepage):

    @classmethod
    def setUpClass(cls):
        driver=webdriver.Chrome()
        Basepage.set_driver(driver)
    @classmethod
    def tearDownClass(cls):
        sleep(2)

    def  test_login01(self):
        driver=Basepage.get_driver()
        driver.get(url)
        driver.maximize_window()
        # 1.定位元素
        location=Basepage.find_element(P.elem)
        #2.输入账号
        Basepage.sendkeys(location,username)
        # 3输入密码
        location2=Basepage.find_element(P.elem2)
        Basepage.sendkeys(location2,pwd)
        #4.点击登录
        location3=Basepage.find_element(P.elem3)
        Basepage.click(location3)
        #5.断言
        sleep(1)
        value=Basepage.get_text(P.elem4)
        assert  value=="我的桌面"

if __name__ == '__main__':
    unittest.main()

'''
数据和脚本分离的做法叫做：PO
优点：
1.方便后期维护
2.用明确的分层思想来管理我们的用例
3.如果数据发生改变，只需要修改配置文件，或者数据文件
缺点：
写上去太复杂了

1.为了后期方便管理和维护我们的代码，我们一般使用po模式（数据与脚本分离）来进行编写脚本
2.介绍，我们的模式一共分了6个层了来装我们的代码，分别是
config==》装配置文件
data==》用来装数据
public==》装公共的方法和基类
report==》装报告
run_case==》运行我们的用例
testcase==》用来转用例
我们在执行用例的时候，一般会结合unittest框架，介绍unittest框架的特性：
执行test开头的方法（执行顺序0~9，A~Z,a~z）
setup  和teardown   :每执行一次用例就会执行一次  执行用例之前，和执行用例之后
setupclass  和 treadownclass   ：我只会执行一次，在最开始和最后的时候   +三种执行框架的方式
'''













