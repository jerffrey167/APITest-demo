import pytest


class Test099():

    @pytest.mark.skip
    def test_one(self):
        print('test_01')
        assert 1 == 1

    @pytest.mark.skip(reason="2222")
    def test_two(self):
        print('test_02')
        assert 2 == 2

    @pytest.mark.skipif(2 == 2, reason="2222")
    def test_three(self):
        print('test_03')
        assert 3 == 3

    def test_four(self):
        print('test_04')
        assert 4 == 4


if __name__ == '__main__':
    pytest.main()
