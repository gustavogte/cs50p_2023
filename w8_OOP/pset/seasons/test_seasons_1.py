#GG
from datetime import date
from seasons_1 import count_minutes
import sys

def main():
    test_minutes()
    test_format()
    test_input()

def test_minutes():
    assert count_minutes(date(1971, 3, 15)) == "Twenty-seven million, five hundred sixty-one thousand, six hundred minutes"
    assert count_minutes(date(2023, 8, 8)) == "One thousand, four hundred forty minutes"

def test_format():
    try:
        count_minutes(date(20, 8, 8))
    except ValueError:
        sys.exit("Invalid date")


def test_input():
    try:
        count_minutes(date(20, 8, 8))
    except sys.SytemExit as e:
        assert e.args[0] == "Invalid Date"