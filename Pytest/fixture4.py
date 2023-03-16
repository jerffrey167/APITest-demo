import pytest

def test_search(login):
    token,username=login
    print(f'token:{token};username:{username}')
    print('搜索')

def test_cart(login):
    print('购物车')

def test_order(login):
    print('下单')

def test_share(connectDB):
    print('分享')

class TestDemo:

    def test_case1(self,login):
        print('case1')

    def test_case2(self,login):
        print('case2')