#coding=utf-8
import unittest
import  os
from config.config import *
from public.pages.HTMLTestRunner3_New import HTMLTestRunner
import time


def run():
    start_dir=testcase_path
    discover=unittest.defaultTestLoader.discover(start_dir,pattern="test*.py")
    now=time.strftime("%Y_%m_%d_%H_%M_%S")
    file_path=reprot_path+"\\"+str(now)+"cms_ui_auto.html"
    f=open(file_path,"wb")
    runnner=HTMLTestRunner(stream=f,
                           title="cms_ui_auto",
                           description="用例执行情况如下：",
                           tester="小刘"
    )
    runnner.run(discover)
if __name__ == '__main__':
    run()









