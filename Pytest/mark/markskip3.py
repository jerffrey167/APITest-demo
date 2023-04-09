import pytest

myskip = pytest.mark.skipif(1 == 1, reason='skip赋值给变量，可多处调用')


class Test099(object):
    @myskip
    def test_one(self):
        assert 1 == 2

    def test_two(self):
        pytest.skip(reason="2222222")
        # 该用例被跳过
        print('test_02')
        assert 1 == 1

    def test_three(self):
        print('test_03')
        assert 1 == 1

    def test_four(self):
        for i in range(10):
            print(f"输出第【{i}】个数")
            if i == 3:
                pytest.skip("i 到达 3用例跳过")


if __name__ == '__main__':
    pytest.main()
