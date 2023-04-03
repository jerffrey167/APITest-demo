import unittest
from  selenium import  webdriver
from  time import  sleep


class setupteardown(unittest.TestCase):

    # def tearDown(self):
    #     print("end")
    #
    # def setUp(self):
    #     driver = webdriver.Chrome()
    #     # 打开浏览器
    #     driver.maximize_window()
    #     # 浏览器窗口最大化
    #     driver.get('https://www.baidu.com/')
    #     # 浏览器打开baidu网站
    #     sleep(2)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        self.assertNotEqual('foo'.upper(), 'FOO2')

    def test_isupper(self):
        self.assertIn('a','aaaa')
        self.assertNotIn('aabba','aaaa')

    def testssss(self):
        print("ssss")


if __name__ == '__main__':
    unittest.main()