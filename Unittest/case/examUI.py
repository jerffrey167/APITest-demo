from  selenium import  webdriver
from  time import  sleep
from  selenium.webdriver.common.by import By
import unittest

class Test_UI(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get('http://120.46.215.163:8102/#/login')

    def test_003login(self):
        driver.find_element(By.XPATH, '//input[@type="text"]').send_keys('admin')
        driver.find_element(By.XPATH, '//input[@type="password"]').send_keys('admin')
        driver.find_element(By.XPATH, '//button[@type="button"]').click()


    def test_004PageOpen(self):
        driver.find_element(By.XPATH, "//*[starts-with(@style,'padding-left: 20px')]/span[text()='考试管理']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//*[starts-with(@style,'padding-left: 40px')]/span[text()='考试管理']").click()

    def test_005Lingout(self):
        driver.find_element(By.XPATH, "//div[text()=' 超管A ']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//span[text()='退出登录']//..").click()
        sleep(1)

    @classmethod
    def tearDownClass(self):
        driver.quit()

if __name__ == '__main__':
    unittest.main()