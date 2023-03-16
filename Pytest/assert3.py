import pytest

def test_raises():
    with pytest.raises(ZeroDivisionError):
        2 / 0
    assert eval("1 + 2") == 3