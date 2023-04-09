import pytest

class Test_01:

    def cake(self):
        a = 'anjing'
        b = 'test_anjing'
        assert  a == b

    def test_001(self):
        print('Test_01下的用例001')
        with pytest.raises(AssertionError):
            self.cake()
#raises：
# 在断言一些代码块或者函数时会引发意料之中的异常或者其他失败的异常，导致程序无法运行时，使用 raises 捕获匹配到的异常，可以继续让代码正常运行。

