import pytest


@pytest.mark.webtest
def test_1():
    print("web case1")


def test_2():
    print("web case2")


def test_3():
    print("web case3")


@pytest.mark.apptest
class TestClass:
    def test_4(self):
        print("app case1")

    def test_5(self):
        print("app case2")


if __name__ == "__main__":
    pytest.main(["-m", "webtest"])
