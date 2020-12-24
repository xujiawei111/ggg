# -*-coding:UTF-8 -*-
from selenium import webdriver
from time import sleep
from pymysql import connect
driver=webdriver.Chrome("../chromedrive/chromedriver")    
driver.get("http://192.168.1.4/ecshop/admin/privilege.php?act=login")
driver.maximize_window()
driver.find_element_by_name("username").send_keys("caichang")
driver.find_element_by_name("password").send_keys("caichang1")
driver.find_element_by_class_name("btn-a").click( )
sleep(1)
driver.switch_to.frame("menu-frame")
driver.find_element_by_xpath('//*[@id="menu-ul"]/li[2]/ul/li[1]/a').click()
driver.switch_to_default_content()
driver.switch_to_frame("main-frame")
goods_name = driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span').text

print(goods_name)
# driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[12]/a[2]/img').click()
# driver.find_element_by_name("shop_price").clear()
# driver.find_element_by_name("shop_price").send_keys("4000")
# driver.find_element_by_xpath('//*[@id="tabbody-div"]/form/div/input[2]').click()
# sleep(3)
# conn=connect('192.168.1.4','root','root','ecshop',3306)
# cursor=conn.cursor()
# cursor.execute("select shop_price from ecs_goods where goods_name='iphone'")
# result=cursor.fetchone()
# # print(result)
# if result[0]==4000:
#     print("编辑通过")
# else:
#     print("编辑不通过")
#     
# conn.close()
# cursor.close()    
#     
#     
