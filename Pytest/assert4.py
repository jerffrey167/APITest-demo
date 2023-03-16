import pytest

def exc(x):
    if x == 0:
        raise ValueError("value not 0 or None")
## 自定义异常
    return 2 / x

def test_raises():
    with pytest.raises(ValueError, match="value not 0 or None"):
        exc(0)
    assert eval("1 + 2") == 3