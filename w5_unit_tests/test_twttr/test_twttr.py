import pytest
from twttr import shorten

def main():
    test_letters()
    test_numbers()
    test_punctuation()

def test_letters():
    assert shorten('Gustavo') == 'Gstv'
    assert shorten('GUSTAVO') == 'GSTV'
    assert shorten('Jennifer') == 'Jnnfr'
    assert shorten('JENNIFER') == 'JNNFR'
    assert shorten('ULDarico') == 'LDrc'

def test_numbers():
    assert shorten('Gustavo1') == 'Gstv1'


def test_punctuation():
    assert shorten('Gustavo!') == 'Gstv!'
