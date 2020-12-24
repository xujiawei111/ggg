# -*-coding:UTF-8 -*-
from xlrd import open_workbook
from xlutils.copy import copy
from xlwt.Formatting import Borders
from xlwt.Style import XFStyle

yuanshi_biao=open_workbook(r"d:\原始表.xls",formatting_info=True) 
new_biao=copy(yuanshi_biao)
sheet=new_biao.get_sheet(0)
content_style = XFStyle()
border = Borders()
border.left = border.THIN
border.right = border.THIN
border.top = border.THIN
border.bottom = border.THIN

content_style.borders = border


sheet.write(3,5,"许佳伟",content_style) 
sheet.write(3,8,"哈哈哈",content_style)
new_biao.save(r"d:\新表.xls")