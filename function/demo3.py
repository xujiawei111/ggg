# -*-coding:UTF-8 -*-
from xlwt.Workbook import Workbook

wb = Workbook('utf-8')
sheet = wb.add_sheet('测试报告')
title = ['编号', '姓名', '职业', '上级', '入职日期']

for i in range(len(title)):
    sheet.write(4, i + 4, title[i],)
    
content = [[1, 'SMITH', '测试', '蔡昶', '2020-10-10'], [2, '凤姐', '开发', '蔡昶', '2020-10-11']]    
for i in range(len(content)):
    for j in range(len(content[i])):
        sheet.write(5 + i, 4 + j, content[i][j])
wb.save(r'd:\自动化测试.xls')    
