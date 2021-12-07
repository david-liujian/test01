#coding=utf-8
'''
需求：点击cms用户中心，用户管理
'''


from public.pages.basepage import Basepage

class Test_usercenter(Basepage):

    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls)  -> None:
        pass

    def test_usercenter01(self):
        elem5=("xpath",'//*[@id="menu-user"]/dt/text()')
        location4=Basepage.find_element(elem5)
        Basepage.click(location4)













