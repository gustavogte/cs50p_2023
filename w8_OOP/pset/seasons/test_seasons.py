# PC
from seasons import minutes_lived
import sys

def main():
    test_1()
    test_2()
    test_3()


def test_1():
    assert minutes_lived(1971, 3, 15) == "Twenty-seven million, five hundred sixty-one thousand, six hundred minutes"
    assert minutes_lived(2023, 8, 8) == "One thousand, four hundred forty minutes"

def test_2():
    # minutes_lived return a boolean value
    try:
        minutes_lived(20, 8, 8)
    except ValueError:
        sys.exit("Invalid date")

def test_3():
    try:
        minutes_lived(20, 8, 8)
    except sys.SytemExit as e:
        assert e.args[0] == "Invalid Date"
