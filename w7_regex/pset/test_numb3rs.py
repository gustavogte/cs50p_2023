from numb3rs import validate

def main():
    test_val_numbers()
    test_val_alpha_4()


def test_val_numbers():
    assert validate("255.255.255.0") == True
    assert validate("255.255.255.300") == False
    assert validate("255.255.255") == False

def test_val_alpha_4():
    assert validate("cat") == False
    assert validate("255.2.") == False
    assert validate("3-23-3-3") == False
