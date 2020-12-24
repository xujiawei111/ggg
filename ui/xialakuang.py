# -*-coding:UTF-8 -*-
from time import sleep
from selenium import webdriver
from pymysql import connect


driver=webdriver.Chrome("../chromedrive/chromedriver.exe")
driver.get("http://192.168.1.4/ecshop/admin/privilege.php?act=login")
driver.maximize_window()
driver.find_element_by_name("username").send_keys("caichang")
driver.find_element_by_name("password").send_keys("caichang1")
driver.find_element_by_class_name("btn-a").click()
driver.switch_to.frame("menu-frame")
driver.find_element_by_link_text("商品列表").click()
driver.switch_to_default_content()
driver.switch_to_frame("main-frame") 
             
driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[5]/img').click()

sleep(4)
conn=connect('192.168.1.4','root','root','ecshop',3306)
cursor=conn.cursor()
cursor.execute("select is_on_sale from ecs_goods where goods_name='medlar'")
rs=cursor.fetchone()
print(rs[0])
sleep(4)
if rs[0]==0:
    print("上架成功")
else:
    print("下架成功")    

conn.close()
cursor.close()

