import unittest
from  selenium import  webdriver
from  time import  sleep
from  selenium.webdriver.common.by import By
from  selenium import  webdriver
from  time import  sleep
from  selenium.webdriver.common.by import By

class setupteardown(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        driver = webdriver.Chrome()
        # 打开浏览器
        driver.maximize_window()
        # 浏览器窗口最大化
        driver.get('https://www.baidu.com/')
        # 浏览器打开baidu网站
        sleep(2)

    @classmethod
    def tearDownClass(self):
        print("end")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        self.assertNotEqual('foo'.upper(), 'FOO2')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def testssss(self):
        print("ssss")


if __name__ == '__main__':
    unittest.main()