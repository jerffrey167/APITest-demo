import unittest

class TestDemo(unittest.TestCase):

    def test_case1(self):
        print('test_case1')

    # skip无条件跳过
    @unittest.skip('跳过用例test_case2')
    def test_case2(self):
        print('test_case2')

    # skipIf当condition为True时跳过
    @unittest.skipIf(0>1, '不跳过用例test_case3')
    def test_case3(self):
        print('test_case3')

    # skipIf当condition为True时跳过
    @unittest.skipIf(0<1, '跳过用例test_case4')
    def test_case4(self):
        print('test_case4')

    # skipUnless当condition为False时跳过
    @unittest.skipUnless(0>1, '跳过用例test_case5')
    def test_case5(self):
        print('test_case5')

    # skipUnless当condition为False时跳过
    @unittest.skipUnless(0<1, '不跳过用例test_case6')
    def test_case6(self):
        print('test_case6')

    # 测试标记为失败
    @unittest.expectedFailure
    def test_case7(self):
        print('test_case7')

if __name__ == '__main__':
    unittest.main()