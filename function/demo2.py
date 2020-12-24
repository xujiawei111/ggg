# -*-coding:UTF-8 -*-
from xlwt.Workbook import Workbook 

wb=Workbook("utf-8")
sheet=wb.add_sheet("测试报告")
sheet.write(1,1,'客户无忧自动化测试报告')
wb.save(r'd:\自动化测试.xls')    