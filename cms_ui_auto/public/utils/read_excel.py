#coding=utf-8
'''
这里封装一个用来读取xlsx的方法的类
读取excel文档需要导入xlrd模块
如果没有的同学，在dos窗口：pip  install xlrd
'''
import xlrd                    #这个xlrd 这个模块是用来读取excel表格的
from config.config import *
import os
class  Read_excel(object):
    def __init__(self,filename,sheetname):
        self.open_book=xlrd.open_workbook(filename)          #打开一个excel文件 ,将这个动作赋值给一个实例变量
        self.choice_sheet=self.open_book.sheet_by_name(sheetname)   #用刚才打开文件的实例变量来选中文档中的 Sheet

    def  get_excel_data(self,row,col):
        value=self.choice_sheet.cell(row,col)      #用刚才选择了的Sheet文件，来获取 某一行，某一列的数据
        return value

if __name__ == '__main__':
    file = os.path.join(data_path, "data1.xls")
    r=Read_excel(file,"Sheet1")      #创建一个读取文件和选择sheet的对象
    print(r.get_excel_data(1,1))       #用这个对象来调读取文档的列和行的索引位对应的数据

















