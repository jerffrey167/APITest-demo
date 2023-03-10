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
        driver.get('http://120.46.215.163:3000/user/login')

    def test_010login(self):
        driver.find_element(By.XPATH, '//input[@type="text"]').send_keys('jsh')
        driver.find_element(By.XPATH, '//input[@type="password"]').send_keys('123456')
        driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        sleep(10)


    def test_011PageOpen(self):
        driver.find_element(By.XPATH, "//span[text()='采购管理']/../..").click()
        sleep(1)
        driver.find_element(By.XPATH, "//span[text()='采购订单']/../..").click()

    def test_012Lingout(self):
        driver.find_element(By.CSS_SELECTOR, ".logout_title").click()
        sleep(1)
        driver.find_element(By.XPATH, "//span[text()='确 定']/..").click()
        sleep(1)

    @classmethod
    def tearDownClass(self):
        driver.quit()

if __name__ == '__main__':
    unittest.main()