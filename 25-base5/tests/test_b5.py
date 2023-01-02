
import importlib

base5 = importlib.import_module("base5")


def test_int_2_base5():
    assert "0" == base5.int_to_base5(0)
    assert "1" == base5.int_to_base5(1)
    assert "2" == base5.int_to_base5(2)
    assert "1=" == base5.int_to_base5(3)
    assert "1-" == base5.int_to_base5(4)
    assert "10" == base5.int_to_base5(5)
    assert "11" == base5.int_to_base5(6)
    assert "1-=" == base5.int_to_base5(18)


def test_base5_2_int():
    assert 0 == base5.base5_to_int("0")
    assert 1 == base5.base5_to_int("1")
    assert 2 == base5.base5_to_int("2")
    assert 3 == base5.base5_to_int("1=")
    assert 4 == base5.base5_to_int("1-")
    assert 5 == base5.base5_to_int("10")
    assert 6 == base5.base5_to_int("11")
    assert 9 == base5.base5_to_int("2-")
    assert 12 == base5.base5_to_int("22")
