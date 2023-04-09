import pytest


# 定义了登录的fixture
@pytest.fixture()
def loging1():
    print('登录操作')
    yield
    print("退出登录")

def test_search():
    print('搜索')


def test_cart(loging1):
    print('购物车')


def test_order(loging1):
    print('下单')


if __name__ == "__main__":
    pytest.main()
