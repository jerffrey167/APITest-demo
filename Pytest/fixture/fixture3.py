import pytest


@pytest.fixture(params=["curry", "kobe", "kd"])
def login(request):
    print(f'用户名:{request.param}')
    yield request.param


def test_demo1(login):
    print(f'demo1 case:{login}')


if __name__ == "__main__":
    pytest.main()
