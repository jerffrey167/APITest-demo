import pytest

@pytest.mark.webtest
def test_send_http():
    print("mark web test")

def test_something_quick():
    pass

def test_another():
    pass

@pytest.mark.apptest
class TestClass:
    def test_case1(self):
        print("app case1")

    def test_case2(self):
        print("app case2")

if __name__ == "__main__":
    pytest.main()