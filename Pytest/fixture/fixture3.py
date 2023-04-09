import pytest

@pytest.fixture(scope='class')
def login():
    print('完成登录操作')
    token='xxxxxxxxxxxxxxx'
    username='kobe'
    #yield默认返回None
    yield token,username
    print('完成退出登录3')

def test_search(login):
    token,username=login
    print(f'token:{token};username:{username}')
    print('搜索')

def test_cart(login):
    print('购物车')

def test_order(login):
    print('下单')