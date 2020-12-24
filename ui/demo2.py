# -*-coding:UTF-8 -*-
from selenium import webdriver

driver=webdriver.Chrome("..\chromedrive\chromedriver.exe")
driver.get("https://kehu51.com/")
driver.maximize_window()
driver.find_element_by_id("username").send_keys("zhongxiu")
driver.find_element_by_id("password").send_keys("111111")
driver.find_element_by_class_name("btn").click()

