import pytest
#
#
# @pytest.fixture(scope='session',autouse=True)
# def login9():
#     print('完成登录操作')
#     token='qrredfdsasddsaw'
#     username='kobe'
#     yield token,username
#     print('完成退出登录')
#
#
# @pytest.fixture()
# def connectDB():
#     print('连接数据库')
#     yield
#     print('断开数据库')