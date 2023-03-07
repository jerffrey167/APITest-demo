import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
#检查预期的输出
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
#验证一个条件
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
# 验证抛出了一个特定的异常
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
if __name__ == '__main__':
    unittest.main()