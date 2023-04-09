import pytest


# fixture的作用域

# 定义了登录的fixture，尽量避免以test_开头
# @pytest.fixture(scope='class')
#@pytest.fixture(scope='function')
@pytest.fixture(scope='module',autouse=True)
def login2():
    print('登录操作')
    yield
    print("退出登录")

def test_search():
    print('搜索')


def test_cart():
    print('购物车')


def test_order():
    print('下单')


class TestDemo:

    def test_case1(self):
        print('case1')

    def test_case2(self):
        print('case2')


if __name__ == "__main__":
    pytest.main()
