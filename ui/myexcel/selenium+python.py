# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from pymysql import connect



driver = webdriver.Chrome()
driver.get('http://192.168.1.4/ecshop/admin/privilege.php?act=login')
driver.maximize_window()


driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_class_name('btn-a').click()

sleep(1)
driver.switch_to.frame('menu-frame')
driver.find_element_by_link_text('商品列表').click()
driver.switch_to.default_content()
driver.switch_to.frame('main-frame')

sleep(2)
driver.find_element_by_name('keyword').send_keys('车')
driver.find_element_by_xpath("//input[@value=' 搜索 ']").click()

#driver.find_element_by_css_selector('.caichang')
#driver.find_element_by_tag_name(name)
#//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span
sleep(1)
search_text = driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span').text
search_total = driver.find_element_by_id('totalRecords').text
# print(search_total)
# print(type(search_total))
conn  = connect('192.168.1.4','root','root','ecshop',3306)
cursor = conn.cursor()
cursor.execute("select goods_name from ecs_goods where goods_name like '%车%'")


rs = cursor.fetchall()
# print(rs)

cursor.execute("select count(*) from ecs_goods where goods_name like '%车%'")
total = cursor.fetchone()
# print(total)
# print(type(total[0]))
if search_text==rs[0][0] and int(search_total) ==total[0] :
    print('测试通过')
else:
    print("测试不通过")
cursor.close()
conn.close()


  
