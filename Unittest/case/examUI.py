from  selenium.webdriver.support.wait import WebDriverWait
from  selenium import  webdriver
from  time import  sleep
from  selenium.webdriver.common.by import By
import unittest

driver = webdriver.Chrome()
# 打开浏览器
driver.maximize_window()

driver.implicitly_wait(5)
#浏览器窗口最大化
driver.get('http://120.46.215.163:8102/#/login')
#浏览器打开考试系统
driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('admin')
#用户名
driver.find_element(By.XPATH,'//input[@type="password"]').send_keys('admin')
#密码
driver.find_element(By.XPATH,'//button[@type="button"]').click()
#登录按钮

driver.find_element(By.XPATH,"//*[starts-with(@style,'padding-left: 20px')]/span[text()='考试管理']").click()
#点击考试管理模块
sleep(1)
driver.find_element(By.XPATH,"//*[starts-with(@style,'padding-left: 40px')]/span[text()='考试管理']").click()
sleep(1)
driver.find_element(By.XPATH,"//div[text()=' 超管A ']").click()
sleep(1)
driver.find_element(By.XPATH,"//span[text()='退出登录']//..").click()

driver.quit()
#关闭浏览器