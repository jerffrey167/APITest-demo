import pytest

myskip = pytest.mark.skipif(1 == 1, reason='skip赋值给变量，可多处调用')


class Test099:
    @myskip
    def test_one(self):
        assert 1 == 2

    def test_two(self):
        print('test_02')
        assert 1 == 1


if __name__ == '__main__':
    pytest.main()
