# -*- coding: utf-8 -*-
from pymysql import connect
conn = connect(host='192.168.1.4', user='root', password="root", database='cms', port=3306)
cursor = conn.cursor()
#执行sql语句
cursor.execute('select * from _cai_student_cai')
result = cursor.fetchall()
#fetchone返回一个
#fetchmany指定返回的条数
#fetchall返回所有
print(result)
#用完一定记得关闭游标和连接
cursor.close()
conn.close()