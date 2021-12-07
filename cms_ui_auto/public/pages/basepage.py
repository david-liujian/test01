#coding=utf-8
'''
这个模块中封装的是，用例的基类和元素定位的方法
页面点击，页面输入，页面滑动条等操作
'''
# 单例模式：每次都使用同一个driver
#需要联系100次投篮：
#我有100个篮球每次都去投不一样的
#我只有一个篮球，但是我投过去，又把篮球捡回来，继续投
import unittest
from selenium import webdriver

class Basepage(unittest.TestCase):             #因为我们封装的方法，待会儿会用来组织我们的用例
    @classmethod
    def set_driver(cls,driver):                    #设置一个driver给类属性
        cls.driver=driver
    @classmethod
    def  get_driver(cls):                          #把类属性返回给函数调用出，因为我们待会用例会引用这个driver
       return cls.driver
    # baidu_input=("id","kw")
    @classmethod
    def  find_element(cls,elem):                  #封装查找元素的方法，只需要传入一个元组  元组的[0]作为定位方式
          type=elem[0]                           #元组的[1]作为元素的 值
          value=elem[1]
          if type=="id":
                elem=cls.driver.find_element_by_id(value)
          elif type=="name":
                elem=cls.driver.find_element_by_name(value)
          elif type=="xpath":
                elem=cls.driver.find_element_by_xpath(value)
          elif type=="class":
                elem=cls.driver.find_element_by_class_name(value)
          elif type=="css":
                elem=cls.driver.find_element_by_css_selector(value)
          elif type=="link_text":
                elem=cls.driver.find_element_by_link_text(value)
          else:
                raise ValueError("please  input  account  value")
          return  elem
    @classmethod
    def  sendkeys(cls,elem,text):                   #封装输入值的方法，需要输入元素定位，就是 上面函数find_element()的返回值
        return  elem.send_keys(text)               #还需要给出一个要输入的值

    @classmethod                              #封装click点击函数
    def click(cls,elem):
        return elem.click()

    @classmethod
    def wait(cls,sec):
        return  cls.driver.implicitly_wait(sec)

    @classmethod
    def  get_text(cls,elem):
        return  Basepage.find_element(elem).text



# if __name__ == '__main__':
    # driver=webdriver.Chrome()
    # driver.get("http://www.baidu.com")
    # baidu_input = ("id", "kw")
    # element=Basepage.find_element(baidu_input)           #类调用类方法来定位元素
    # Basepage.sendkeys(element,"python")                 #类调用类方法来给指定元素填写进内容
    #






