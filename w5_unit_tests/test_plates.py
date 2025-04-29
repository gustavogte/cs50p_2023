from plates import is_valid

def main():
    test_len()
    test_alpha()
    test_chr()
    test_numberP()
    test_zero()

def test_len():
    assert is_valid("1") == False
    assert is_valid("AB23456789") == False

def test_alpha():
    assert is_valid("AA3456") == True
    assert is_valid("123456") == False

def test_chr():
    assert is_valid("AA345!") == False

def test_numberP():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_zero():
    assert is_valid("AA0000") == False
