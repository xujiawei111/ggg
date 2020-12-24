# -*-coding:UTF-8 -*-
from xlrd import open_workbook
class MyExcel():

    def __init__(self, workbook_name, sheet_name):
        self.workbook_name = workbook_name
        self.sheet_name = sheet_name

    def __sheet(self):
        bk=open_workbook(self.workbook_name) 
        sheet = bk.sheet_by_name(self.sheet_name)
        return sheet
    #��������
    def total_rows(self):
        return self.__sheet().nrows
    #��������
    def total_columns(self):
        return self.__sheet().ncols
    def cell_value(self):
        return self.sheet(12,6).cell_value
  

    
    #��ĳ��Ԫ��
    #cell_value = sheet.cell_value(12,6) #�±��0��ʼ
    #print(cell_value)

my = MyExcel(r'd:\emp.xls', 'empinfo')
print(my.total_rows())
print(my.total_columns())
print(my.cell_value())    