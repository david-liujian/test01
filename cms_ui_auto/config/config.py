#coding=utf-8
''''''
'''
这个模块是用来存放项目和各个包的路径，
为了后面引用路径使用
'''
import os
# path=r"C:\Users\liujian\PycharmProjects\cms_ui_auto"
# newpath=os.path.join(path,"config")
# print(newpath)

base_path=os.path.dirname(os.path.dirname(__file__)) #os.path.dirname获取到当前文件的上级路径
# print(base_path)
data_path=os.path.join(base_path,"data")       #data包的路径
# print(data_path)
public_path=os.path.join(base_path,"public")   #public包的路径
# print(public_path)
pages_path=os.path.join(public_path,"pages")     #public/pages的路径
# print(pages_path)
utils_path=os.path.join(public_path,"utils")    #public/utils的路径
# print(utils_path)
reprot_path=os.path.join(base_path,"reprot")   #report包的路径
# print(reprot_path)
runcase_path=os.path.join(base_path,"run_case")  #run_case包的路径
# print(runcase_path)
testcase_path=os.path.join(base_path,"testcase")   #test_case包的路径
# print(testcase_path)









