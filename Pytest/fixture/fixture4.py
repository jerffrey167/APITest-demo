import pytest


@pytest.fixture(params=["curry", "kobe", "kd"], ids=["3", "4", "5"], name="abc")
def login(request):
    print(f'用户名:{request.param}')
    yield request.param


def test_demo1(abc):
    print(f'demo1 case:{abc}')


if __name__ == "__main__":
    pytest.main()
