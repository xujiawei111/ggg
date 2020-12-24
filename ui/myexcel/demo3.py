# -*-coding:UTF-8 -*-
from xlwt import Workbook
wb=Workbook("utf-8")
sheet=wb.add_sheet("测试报告")
sheet.write(4,4,'客户无忧自动化测试报告')
wb.save(r'd:\自动测试.xls')