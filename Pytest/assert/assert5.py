import pytest


def exc(x):
    if x == 0:
        raise ValueError("value not 0")
    return 2 / x

def test_raises():
    with pytest.raises(ValueError) as exec_info:
        exc(0)

    print("exec_info.type = ", exec_info.type)
    print("exec_info.value.args = ", exec_info.value.args)

    assert exec_info.type == ValueError
    assert exec_info.value.args[0] == "value not 0"


#在捕获异常后，可以从上下文管理器中获取异常的一些详细信息，可以辅助我们更好的去断言。
