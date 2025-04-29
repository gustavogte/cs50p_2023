from um import count


def main():
    test_times()
    test_words()
    test_char()
    test_case()


def test_times():
    assert count("um, um, um") == 3
    assert count("um, um") != 3
    assert count("um, um, um, uk") == 3

def test_words():
    assert count("hum, yum, umy") == 0
    assert count("hum, yum, umy, um, um") == 2

def test_char():
    assert count("um..., um, um.") == 3
    assert count("um..., hum, um?") == 2

def test_case():
    assert count("uM..., Um, um.") == 3
    assert count("UM um Um?") == 3
