import pytest

#fixture的作用域

#定义了登录的fixture，尽量避免以test_开头
#@pytest.fixture(scope='module')
@pytest.fixture(scope='function')
#@pytest.fixture(scope='class')
def login():
    print('完成登录操作')

def test_search(login):
    print('搜索')

def test_cart(login):
    print('购物车')

def test_order(login):
    print('下单')

class TestDemo:

    def test_case1(self,login):
        print('case1')

    def test_case2(self,login):
        print('case2')